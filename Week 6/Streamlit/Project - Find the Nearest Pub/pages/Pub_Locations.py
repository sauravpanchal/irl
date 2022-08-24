import streamlit as st
import pandas as pd
from Home import get_df, remove_na

st.sidebar.markdown("# Pub Locations 🎈")

df = get_df()
remove_na(df)

st.header("Pub Locations")
print(tuple(df["local_authority"].value_counts().index))
option = st.selectbox(
     'Your Local Authority ?',
     (tuple(df["local_authority"].value_counts().index)))

st.write('You selected:', option)
temp_df = df[df["local_authority"] == option]
print(temp_df)
st.map(temp_df[["lat", "lon"]])