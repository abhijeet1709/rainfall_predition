import pickle
import pandas as pd
import streamlit as st

# Load model
model = pickle.load(open("trained_model.sav", "rb"))

# UI
st.title("🌧️ Rainfall Prediction App")

pressure = st.number_input("Pressure", value=1015.9)
dewpoint = st.number_input("Dew Point", value=19.9)
humidity = st.number_input("Humidity", value=95.0)
cloud = st.number_input("Cloud", value=81.0)
sunshine = st.number_input("Sunshine", value=0.0)
winddirection = st.number_input("Wind Direction", value=40.0)
windspeed = st.number_input("Wind Speed", value=13.7)

if st.button("Predict Rainfall"):

    input_df = pd.DataFrame(
        [[pressure, dewpoint, humidity, cloud, sunshine, winddirection, windspeed]],
        columns=['pressure', 'dewpoint', 'humidity', 'cloud', 'sunshine','winddirection', 'windspeed']
    )

    prediction = model.predict(input_df)

    if prediction[0] == 1:
        st.success("🌧️ Rainfall Expected")
    else:
        st.success("☀️ No Rainfall")