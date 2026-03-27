# 🛒 Retail Sales Analysis & Prediction System

## 📌 Project Overview

This project focuses on analyzing retail sales data and building a machine learning model to predict total sales. It combines data analysis, visualization, and predictive modeling to generate meaningful business insights.

---

## 🎯 Objectives

* Analyze sales trends across categories, products, and time
* Identify key factors influencing sales
* Build a machine learning model to predict total sales
* Provide actionable business insights

---

## 📊 Dataset Description

The dataset contains retail transaction details:

* Invoice_ID: Unique transaction ID
* Customer_ID: Unique customer ID
* Product_Name: Name of product
* Category: Product category
* Quantity: Number of units sold
* Price: Price per unit
* Total_Sales: Total transaction value
* Date: Transaction date

---

## 🔍 Exploratory Data Analysis (EDA)

Performed detailed analysis including:

* Category-wise sales distribution
* Monthly sales trends
* Top-selling products
* Customer purchase behavior
* Correlation analysis

---

## ⚙️ Feature Engineering

* Extracted Month, Day, Year from Date
* Created Revenue_per_Unit feature
* Encoded categorical variables
* Applied feature scaling

---

## 🤖 Machine Learning Models Used

* Linear Regression
* Decision Tree Regressor
* Random Forest Regressor
* Tuned Random Forest (GridSearchCV)

---

## 📈 Model Evaluation Metrics

* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)
* R² Score

---

## 🏆 Results

* Tuned Random Forest achieved the best performance
* Improved prediction accuracy after hyperparameter tuning

---

## 💡 Key Insights

* Certain categories contribute significantly to revenue
* Sales show seasonal trends across months
* Customer purchasing patterns impact revenue
* Quantity and price are major influencing factors

---

## 🚀 Future Improvements

* Deploy model using Streamlit (Web App)
* Use larger and real-time datasets
* Implement deep learning models
* Add recommendation system

---

## 🧑‍💻 Technologies Used

* Python
* Pandas, NumPy
* Matplotlib, Seaborn
* Scikit-learn
* Streamlit

---

## 📦 How to Run

1. Clone repository
2. Install dependencies
3. Run notebook or Streamlit app

```bash
pip install -r requirements.txt
streamlit run app_sales.py
```

---

## 📁 Project Structure

```
├── RetailSales.csv
├── Retail_Sales_Analysis.ipynb
├── app_sales.py
├── retail_sales_model.pkl
├── README.md
```

---

## 👤 Author

Viraj Shreenath Shinde

---

## ⭐ Acknowledgment

This project is part of internship work and demonstrates practical application of data science and machine learning concepts.
