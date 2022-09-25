import streamlit as st
from Home import get_df, remove_na

st.sidebar.markdown("# Saurav Panchal 👨🏻‍💻")
st.sidebar.markdown("[Edit here ⚒️](https://github.com/sauravpanchal/irl/tree/main/Week%206/Streamlit/Project%20-%20Find%20the%20Nearest%20Pub)")

df = get_df()
remove_na(df)

st.header("Pub Locations 🗺️")
option = st.selectbox(
     'Your Local Authority ?',
     (tuple(df["local_authority"].value_counts().index)))

st.write('You selected:', option)
temp_df = df[df["local_authority"] == option]
st.map(temp_df[["lat", "lon"]])