import streamlit as st
import joblib 
import numpy as np

scaler = joblib.load("scaler.pkl")
model = joblib.load("model.pkl")

st.title("Customer Car Price Estimator App")

st.divider()

st.write("""This app is for getting a price estimation for the customer,
          so a car with the price range given can be adviced to the customer""")

age = st.number_input("Enter the age", min_value = 18, max_value = 90, value = 40, step = 10)
salary = st.number_input("Enter the salary", min_value = 1000, max_value = 999999999, step = 5000, value = 30000)
networth = st.number_input("Enter the net worth", min_value = 0, max_value = 999999999, step = 20000)

X = [[age, salary, networth]]

calculatebutton = st.button("Calculate")

if calculatebutton:
    X_scaled = scaler.transform(X)

    X_array = np.array(X_scaled)

    prediction = model.predict(X_array)

    st.write(f"Prediction is {prediction[0][0]:,.2f}")
    st.write("Advice: Look for cars around this value.")


else:
    st.write("Please enter the values and press the calculate button")

