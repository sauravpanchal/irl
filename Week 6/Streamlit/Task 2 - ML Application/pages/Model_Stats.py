import streamlit as st
from Home import get_model_snippet

st.sidebar.markdown("# Saurav Panchal 👨🏻‍💻")
st.sidebar.markdown("[Edit here ⚒️](https://github.com/sauravpanchal/irl/tree/main/Week%206/Streamlit)")

model_option = st.selectbox("Select Model To Know The Statistics", ("LinearRegression", "KNeighborsRegressors", "DecisionTreeRegressor", "RandomForestRegressor"))
st.write(model_option + " Sample Code")

model_code_and_metrics = get_model_snippet(model_option)

code = model_code_and_metrics[:-6]
metrics = model_code_and_metrics[-6:]

st.code("".join(code))

st.write("Output")
st.code("\n".join(metrics))