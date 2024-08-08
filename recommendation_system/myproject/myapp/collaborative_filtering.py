import numpy as np
import tensorflow as tf
import pandas as pd
from sklearn.model_selection import train_test_split


# DATA LOADING
def load_2():
    user_interactions = pd.read_csv('myapp/user_interactions.csv')
    print('cf: ', user_interactions.head())
    return user_interactions


# PREPPING DATA
def prep_2(user_interactions):
    user_item_matrix = user_interactions.pivot_table(index='user_id', columns='vendor_id', aggfunc='size', fill_value=0)
    user_item_matrix = user_item_matrix.values
    num_users, num_items = user_item_matrix.shape
    return user_item_matrix, num_users, num_items


# MATRIX FACTORIZATION
def build_2(num_users, num_items, latent_dim=10):
    # predicts interaction by computing dot product of user and item embeddings
    user_input = tf.keras.layers.Input(shape=(), dtype=tf.int32, name='user_input')
    item_input = tf.keras.layers.Input(shape=(), dtype=tf.int32, name='item_input')
    user_embedding = tf.keras.layers.Embedding(num_users, latent_dim, name='user_embedding')(user_input)
    item_embedding = tf.keras.layers.Embedding(num_items, latent_dim, name='item_embedding')(item_input)
    dot_product = tf.keras.layers.Dot(axes=1)([user_embedding, item_embedding])
    output = tf.keras.layers.Reshape((1,))(dot_product)
    model = tf.keras.Model(inputs=[user_input, item_input], outputs=output)
    model.compile(optimizer='adam', loss='mean_squared_error') # minimizes prediction error
    print(f"Number of users: {num_users}, Number of items: {num_items}")  # Debugging
    return model


# MODEL TRAINING
def model_2(model, user_item_matrix):
    # trains using user-item interactions
    user_matrix = np.arange(user_item_matrix.shape[0])
    item_matrix = np.arange(user_item_matrix.shape[1])
    X = np.array(np.meshgrid(user_matrix, item_matrix)).T.reshape(-1, 2)
    y = user_item_matrix[X[:, 0], X[:, 1]]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)
    model.fit([X_train[:, 0], X_train[:, 1]], y_train, epochs=10, batch_size=64, validation_data=([X_test[:, 0], X_test[:, 1]], y_test))
    print("Model training complete")

# PREDICTION
def pred_2(model, num_users, num_items):
    # generates predictions for all user-item
    user_matrix = np.arange(num_users)
    item_matrix = np.arange(num_items)
    X = np.array(np.meshgrid(user_matrix, item_matrix)).T.reshape(-1, 2)
    predictions = model.predict([X[:, 0], X[:, 1]])
    print(f"Predictions shape: {predictions.shape}")  
    return predictions.reshape(num_users, num_items)