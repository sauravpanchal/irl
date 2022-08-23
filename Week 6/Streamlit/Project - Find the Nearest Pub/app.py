import streamlit as st
import pandas as pd
import numpy as np
import io # to maintain buffers

df = pd.read_csv("open_pubs.csv", na_values = "\\N")

st.title("Open Pub Application")

st.header("Home")
st.caption("Below are some statistics about the dataset")

st.caption("Sum of null values in dataset")
st.text(sum(df.isna().sum()))
df.dropna(inplace = True)

st.subheader("Dataset")
st.write(df.head())

st.subheader("Shape of dataset")
st.write(df.shape)

buffer = io.StringIO()
df.info(buf = buffer)
st.subheader("Basic information about all the columns present in dataset")
st.text(buffer.getvalue())

st.subheader("Columns present in dataset")
st.write(df.columns)

st.subheader("Size of dataset (Number of elements present)")
st.write(df.size)

st.subheader("Basic statistics of dataset columns")
st.write(df.describe())

st.subheader("Unique values in categorical columns of dataset")

st.caption("Name")
st.text(df["name"].nunique())
st.caption("Address")
st.text(df["address"].nunique())
st.caption("Postcode")
st.text(df["postcode"].nunique())
st.caption("Local Authority")
st.text(df["local_authority"].nunique())