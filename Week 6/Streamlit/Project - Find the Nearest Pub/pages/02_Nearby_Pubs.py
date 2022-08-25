import streamlit as st
import numpy as np
from Home import get_df, remove_na

st.sidebar.markdown("# Saurav Panchal 👨🏻‍💻")
st.sidebar.markdown("[Edit here ⚒️](https://github.com/sauravpanchal/irl/tree/main/Week%206/Streamlit/Project%20-%20Find%20the%20Nearest%20Pub)")

df = get_df()
remove_na(df)

st.header("Nearby Pubs 🥂")

lat = st.text_input("Enter your latitude", "51.970379")
lon = st.text_input("Enter your longitude", "0.979340")
near = st.number_input("Enter how nearby pubs you are searching", 5)
lat = np.array(float(lat))
lon = np.array(float(lon))

df["calculated_lat_lon"] = np.array((((lat - df["lat"]) ** 2) + ((lon - df["lon"]) ** 2)) ** 0.5)
temp_df = df.sort_values(by = "calculated_lat_lon")[ : near]
st.map(temp_df[["lat", "lon"]])