import requests
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY=os.getenv("Weather_API_KEY")

st.set_page_config(page_title="Weather App", page_icon="🌈")

st.title("Weather App 🌧️")

st.write("Enter a city name and click on the button to get the weather data")

city=st.text_input("Enter city name: ")

API_URL=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

if st.button("Fetch Weather Data"):
    response=requests.get(API_URL)

    if(response.status_code==200):
        st.success("Weather data fetched successfully")
        data=response.json()

        # Fetch the weather data in variables
        Temperature=data["main"]["temp"]
        Humidity=data["main"]["humidity"]
        Wind_speed=data["wind"]["speed"]
        Weather=data["weather"][0]["main"]

        col1, col2 = st.columns(2)
        col3, col4 = st.columns(2)
        col1.metric("Temperature",f"🌡️{Temperature}°C")   
        col2.metric("Humidity",f"💧{Humidity}%")
        col3.metric("Wind Speed",f"💨{Wind_speed}m/s")
        col4.metric("Weather",f"☁️{Weather}")
    else:
        st.error("Invalid City Name")

