from django.http import JsonResponse
from .content_based import load_data, process_data, model, training, load_model, save_model
from .collaborative_filtering import load_2, prep_2, build_2, model_2, pred_2
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

def get_recommendations(request, user_id):
    # RUNNING RECOMMENDATION ENGINE
    user_interactions, vendor_clusters, vendor_metadata = load_data()
    
    # USER INTERACTIONS EXIST OR NOT
    if user_id not in user_interactions['user_id'].values:
        print("No data available for the user")
        return JsonResponse({'error': 'No data available for the user'}, status=404)
    
    # CONTENT BASED FILTERING
    features, target, encoder = process_data(user_interactions, vendor_metadata)
    
    try:
        cb_model = load_model()
    except Exception as e:
        print(f"Error loading model: {e}")
        cb_model = model(features.shape[1])
        x_train = features
        y_train = target
        training(cb_model, x_train, y_train)
        save_model(cb_model)
    
    user_data = user_interactions[user_interactions['user_id'] == user_id]
    user_data_full = pd.merge(user_data, vendor_metadata, on='vendor_id', how='left')
    user_features = encoder.transform(user_data_full[['category', 'type_of_event', 'price_range']])
    vendor_features = encoder.transform(vendor_metadata[['category', 'type_of_event', 'price_range']])
    similarity_scores = cosine_similarity(user_features, vendor_features).mean(axis=0)
    vendor_metadata['content_based_score'] = similarity_scores

    # COLLABORATIVE FILTERING
    user_item_matrix, num_users, num_items = prep_2(user_interactions)
    cf_model = build_2(num_users, num_items)
    model_2(cf_model, user_item_matrix)
    predictions = pred_2(cf_model, num_users, num_items)
    cf_scores = predictions[user_id - 1]
    vendor_clusters['collaborative_filtering_score'] = pd.Series(cf_scores, index=range(num_items)).reindex(vendor_clusters.index).values


    # COMBINE BOTH SCORES
    combined_scores = vendor_metadata[['vendor_id']].copy()
    combined_scores = combined_scores.merge(vendor_metadata[['vendor_id', 'content_based_score']], on='vendor_id')
    combined_scores = combined_scores.merge(vendor_clusters[['vendor_id', 'collaborative_filtering_score']], on='vendor_id', how='left')
    combined_scores['combined_score'] = 0.5 * combined_scores['content_based_score'] + 0.5 * combined_scores['collaborative_filtering_score'].fillna(0)

    # RANKING AND EXLUDING VISITED VENDORS
    ranked_vendors = combined_scores.sort_values(by='combined_score', ascending=False)
    visited_vendors = user_data['vendor_id'].unique()
    final_recommendations = ranked_vendors[~ranked_vendors['vendor_id'].isin(visited_vendors)].head(10)
    
    # RETURN
    final_recommendations = final_recommendations.merge(vendor_metadata[['vendor_id', 'category', 'type_of_event', 'price_range', 'description']], on='vendor_id')
    final_response = final_recommendations[['vendor_id', 'category', 'type_of_event', 'price_range', 'description']]
    return JsonResponse(final_response.to_dict(orient='records'), safe=False)
