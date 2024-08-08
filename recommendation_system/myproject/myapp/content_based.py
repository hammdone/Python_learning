import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import OneHotEncoder


# DATA LOADING
def load_data():
    user_interactions = pd.read_csv('myapp/user_interactions.csv')
    vendor_clusters = pd.read_csv('myapp/vendor_clusters.csv')
    vendor_metadata = pd.read_csv('myapp/vendor_metadata.csv')
    return user_interactions, vendor_clusters, vendor_metadata


# PROCESSING DATA
def process_data(user_interactions, vendor_metadata):
    combined_data = pd.merge(user_interactions, vendor_metadata, on='vendor_id', how='left')
    features = combined_data[['category', 'type_of_event', 'price_range']]
    target = combined_data['vendor_id']
    encoder = OneHotEncoder(handle_unknown='ignore', sparse_output=False) # converts into a numerical format
    features_transformed = encoder.fit_transform(features)
    return features_transformed, target, encoder 


# MODEL
def model(input_shape):
    # using a binary classification, predicts whether user will 
    # interact with a certain vendor or not
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(64, activation='relu', input_shape=(input_shape,)),
        tf.keras.layers.Dense(32, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model


# TRAINING
def training(model, x_train, y_train):
    model.fit(x_train, y_train, epochs=10, batch_size=32, validation_split=0.2)


# SAVE AND LOAD
def save_model(model):
    model.save('myapp/recommendation_model.h5')

def load_model():
    return tf.keras.models.load_model('myapp/recommendation_model.h5')