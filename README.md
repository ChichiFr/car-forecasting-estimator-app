# 🚗 Customer Car Price Estimator App

This app helps estimate an appropriate car price for a customer based on their age, salary, and net worth. The goal is to suggest a price range of cars that fits the customer's profile.

## 📸 App Screenshot
![image](https://github.com/user-attachments/assets/ea38961f-9726-4ff6-8979-f4daf09f2eac)

## 📌 Features
- Takes customer **age**, **salary**, and **net worth** as input.
- Predicts a suitable car price using a pre-trained model.
- Provides advice on car pricing range for the customer.

## ⚙️ Technologies used
- [Streamlit](https://streamlit.io/) for building the web app.
- [Joblib](https://joblib.readthedocs.io/) for loading the scaler and model.
- [NumPy](https://numpy.org/) for numerical operations.

## 🚀 How to run the app
1️⃣ Clone this repository:
```bash
git clone https://github.com/ChichiFr/car-forecasting-estimator-app.git
cd car-forecasting-estimator-app
```

2️⃣ Make sure you have the required libraries installed:
pip install streamlit joblib numpy

3️⃣ Run the app:
bash
Copy code
streamlit run app.py

📂 Files
app.py — main Streamlit application.
scaler.pkl — pre-trained scaler for input data.
model.pkl — pre-trained machine learning model.

📝 Example
When you open the app, you can:
Input age (e.g., 40)
Input salary (e.g., 30,000)
Input net worth (e.g., 100,000)
Click Calculate → The app will output an estimated car price and advice.

❗ Notes
Ensure scaler.pkl and model.pkl are in the same directory as app.py.
The model should have been trained beforehand to suit your specific use case.
