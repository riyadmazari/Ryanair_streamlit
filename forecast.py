import streamlit as st
from utils import load_model_for_product, preprocess_input_for_product, load_airport_data, generate_identifier, get_model_names

def render_forecast():
    st.title("Product Sales Forecast")
    
    # Access MODEL_NAMES here
    MODEL_NAMES = get_model_names()

    # Load airport data for selection
    airport_data = load_airport_data()
    airports_list = list(airport_data.keys())

    departure_airport = st.selectbox("Departure Airport", airports_list)
    arrival_airport = st.selectbox("Arrival Airport", airports_list)
    date = st.date_input("Date of Flight")

    # Generate or derive Lof_ID based on the inputs
    lof_id = generate_identifier(departure_airport, arrival_airport, date)

    if st.button("Predict Sales"):
        predictions = {}
        for product_name in MODEL_NAMES.keys():
            model = load_model_for_product(product_name)
            # Assume preprocessing requires these inputs; adjust as necessary
            input_data = preprocess_input_for_product({
                "departure_airport": departure_airport,
                "arrival_airport": arrival_airport,
                "date": date,
                "lof_id": lof_id
            }, product_name)
            prediction = model.predict(input_data)
            predictions[product_name] = prediction[0]

        # Display predictions
        for product_name, prediction in predictions.items():
            st.write(f"Predicted sales for {product_name}: {prediction} units")