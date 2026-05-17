import streamlit as st
import numpy as np
import joblib

model5=joblib.load("random_forest_model.pkl")
st.title("California Housing Price Predictor")
st.write("Enter housing details below: ")

MedInc=st.number_input("Median Income")
HouseAge=st.number_input("House Age")
AveRooms = st.number_input("Average Rooms")
AveBedrms = st.number_input("Average Bedrooms")
Population = st.number_input("Population")
AveOccup = st.number_input("Average Occupancy")
Latitude = st.number_input("Latitude")
Longitude = st.number_input("Longitude")

if st.button("Predict House Price"):
  input_data=np.array([[MedInc, HouseAge, AveRooms,
                            AveBedrms, Population,
                            AveOccup, Latitude, Longitude]])
  prediction=model5.predict(input_data)
  st.success(f"Predicted House Price: ${prediction[0] * 100000:.2f}")
