import pandas as pd
from catboost import CatBoostRegressor
import streamlit as st
import json

# Assuming you have a CSV file for your dataset
DATASET_DIR = '/Users/riyadmazari/Desktop/Ryanair_streamlit/dataset/'
# Directory where your models are stored
MODEL_DIR = '/Users/riyadmazari/Desktop/Ryanair_streamlit/models/'

MODEL_NAMES = {
    'Ham_Cheese_Panini_qt': 'model_Ham_Cheese_Panini_qt.cbm',
    'Chicken_Seeded_Panini_qt': 'model_Chicken_Seeded_Panini_qt.cbm',
    'Ham_Cheese_Croissant_qt': 'model_Ham_Cheese_Croissant_qt.cbm',
    'Fresh_Sandwich_qt': 'model_Fresh_Sandwich_qt.cbm',
    'Choc_Croissant_qt': 'model_Choc_Croissant_qt.cbm',
    'Bacon_Baguette_qt': 'model_Bacon_Baguette_qt.cbm'
}

@st.cache(allow_output_mutation=True)
def load_model_for_product(product_name):
    model_path = f"{MODEL_DIR}{MODEL_NAMES[product_name]}"
    model = CatBoostRegressor()
    model.load_model(model_path)
    return model

def preprocess_input_for_product(input_data, product_name):
    # Implement the actual preprocessing steps here, tailored to how your model was trained
    # Placeholder for preprocessing logic
    preprocessed_input = input_data
    return preprocessed_input

@st.cache
def load_dataset(file_name):
    dataset_path = f"{DATASET_DIR}{file_name}"
    return pd.read_csv(dataset_path)

@st.cache
def load_airport_data():
    with open(f"{DATASET_DIR}final_map.json") as file:
        data = json.load(file)
    return data

# Add a function to generate Lof_ID or similar identifiers based on existing dataset if needed
def generate_identifier(departure, arrival, date):
    # Placeholder for logic to generate or select a suitable Lof_ID or similar identifier
    
    # This could involve querying your dataset to find a matching or creating a new one
    return "20.01.2023_102FR123"

# Make sure to include functions to export MODEL_NAMES if needed
def get_model_names():
    return MODEL_NAMES