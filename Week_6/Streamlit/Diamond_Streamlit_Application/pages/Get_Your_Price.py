import streamlit as st
from Home import load_model, load_encoder, load_scaler
import numpy as np

st.sidebar.markdown("# Saurav Panchal 👨🏻‍💻")
st.sidebar.markdown("[LinkedIn 💼](https://linkedin.com/in/sauravpanchal) | [Twitter 🕊️](https://twitter.com/sauravpanchhal) | [GitHub ❣️](https://github.com/sauravpanchal)")
st.sidebar.markdown("***")
st.sidebar.markdown("###### [Issues | Bugs | Features ⚒️](https://github.com/sauravpanchal/irl/tree/main/Week_6/Streamlit/Diamond_Streamlit_Application)")

model_option = st.selectbox("Select Model To Apply", ("LinearRegression", "KNeighborsRegressors", "DecisionTreeRegressor", "RandomForestRegressor"))
st.write(model_option)

model_obj = load_model(model_option)
cut_encoder_obj = load_encoder("Cut_LabelEncoder")
color_encoder_obj = load_encoder("Color_LabelEncoder")
clarity_encoder_obj = load_encoder("Clarity_LabelEncoder")
scaler_obj = load_scaler()

st.subheader("Enter your Diamond features to get the price")

carat = st.slider("Carat", 0.00, 5.00)
length = st.slider("Length", 0.00, 11.00)
width = st.slider("Width", 0.00, 60.00)
depth = st.slider("Depth", 0.00, 32.00)
cut = st.selectbox("Cut", ("Fair", "Good", "Very Good", "Premium", "Ideal"))
color = st.selectbox("Color", ("J", "I", "H", "G", "F", "E", "D"))
st.caption("NOTE: J (worst) -> D (best)")
clarity = st.selectbox("Clarity", ("I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"))
st.caption("NOTE: I1 (worst) -> IF (best)")

button = st.button("Get Price")

if button:
    if carat and length and width and depth and cut and color and clarity:
        cut_encoded = cut_encoder_obj.transform([cut])
        color_encoded = color_encoder_obj.transform([color])
        clarity_encoded = clarity_encoder_obj.transform([clarity])
        
        pred_point = np.array([float(carat), float(cut_encoded), float(color_encoded), float(clarity_encoded), float(length), float(width), float(depth)])
        pred_point_rescaled = scaler_obj.transform(pred_point.reshape(1, -1))
        pred = model_obj.predict(pred_point_rescaled)
        st.success(round(pred[0], 2))
        st.balloons()
    else:
        st.error("Invalid values entered !")
        st.snow()