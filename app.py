import streamlit as st
from forecast import render_forecast
from dashboard import render_dashboard  # Uncomment and implement if you have this module
from creators import render_creators  # Uncomment and implement if you have this module

def main():
    st.set_page_config(page_title="Ryanair Datathon", layout="wide")

    menu_options = ["Forecast", "Dashboard", "Creators"]
    choice = st.sidebar.selectbox("Menu", menu_options)

    if choice == "Forecast":
        render_forecast()
    elif choice == "Dashboard":
        render_dashboard()  # Implement this function in a separate file
    elif choice == "Creators":
        render_creators()  # Implement this function in a separate file

if __name__ == "__main__":
    main()
