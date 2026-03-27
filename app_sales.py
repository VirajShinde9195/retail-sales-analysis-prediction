import streamlit as st
import numpy as np
import joblib

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(page_title="Retail Sales Predictor", layout="centered")

# -------------------------------
# Load Model
# -------------------------------
model = joblib.load('retail_sales_model.pkl')

# -------------------------------
# Title
# -------------------------------
st.title("🛒 Retail Sales Prediction System")
st.markdown("Predict total sales based on product and customer details")

# -------------------------------
# Sidebar Inputs
# -------------------------------
st.sidebar.header("📥 Input Features")

# Example categories (replace with your actual categories if needed)
category_dict = {
    "Electronics": 0,
    "Clothing": 1,
    "Grocery": 2,
    "Furniture": 3
}

day_dict = {
    "Monday": 0,
    "Tuesday": 1,
    "Wednesday": 2,
    "Thursday": 3,
    "Friday": 4,
    "Saturday": 5,
    "Sunday": 6
}

# Inputs
customer_id = st.sidebar.number_input("Customer ID", min_value=1, step=1)

category_name = st.sidebar.selectbox("Category", list(category_dict.keys()))
category = category_dict[category_name]

quantity = st.sidebar.slider("Quantity", 1, 20)

price = st.sidebar.number_input("Price", min_value=0.0)

month = st.sidebar.selectbox("Month", list(range(1, 13)))

# Feature engineering (same as training)
revenue_per_unit = price  # or price * 1 depending on your logic

# -------------------------------
# Prediction Button
# -------------------------------
if st.button("🔮 Predict Sales"):

    # Arrange input same as training
    input_data = np.array([[customer_id, category, quantity, price, revenue_per_unit, month]])

    prediction = model.predict(input_data)

    st.success(f"💰 Predicted Sales: ₹ {prediction[0]:.2f}")

# -------------------------------
# Footer
# -------------------------------
st.markdown("---")
st.markdown("⚡ Built with Streamlit | Advanced ML Project")