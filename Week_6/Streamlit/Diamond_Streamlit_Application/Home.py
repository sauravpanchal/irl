import streamlit as st
import pandas as pd, numpy as np
from pickle import load
import matplotlib.pyplot as plt, seaborn as sns

st.sidebar.markdown("# Saurav Panchal 👨🏻‍💻")
st.sidebar.markdown("[Edit here ⚒️](https://github.com/sauravpanchal/irl/tree/main/Week%206/Streamlit)")

def load_model(model_name):
    '''
    Deserializes the given model name from models directory

    Parameters
    ----------
    model_name: str
        name of model to load

    Returns
    -------
    model_name: Object
        Deserialized model object
    '''
    return load(open("models/" + model_name + ".pkl", "rb"))

def load_encoder(encoder):
    '''
    Deserializes the given encoder name from models directory

    Parameters
    ----------
    encoder: str
        name of encoder to load

    Returns
    -------
    encoder: Object
        Deserialized encoder object
    '''
    return load(open("models/" + encoder + ".pkl", "rb"))

def load_scaler(scaler = "StandardScaler"):
    '''
    Deserializes the given scaler name from models directory

    Parameters
    ----------
    encoder: str
        name of scaler to load
        Default: StandardScaler
    
    Returns
    -------
    scaler: Object
        Deserialized scaler object
    '''
    return load(open("models/" + scaler + ".pkl", "rb"))

def get_model_snippet(model):
    '''
    Parameters
    ----------
    model: str
        name of model to get it's code snippet
    
    Returns
    -------
    list
        list of strings consisting of model code snippet 
    '''
    code = list()

    lr = "from sklearn.linear_model import LinearRegression\n"
    knn = "from sklearn.neighbors import KNeighborsRegressor\n"
    dt = "from sklearn.tree import DecisionTreeRegressor\n"
    rf = "from sklearn.ensemble import RandomForestRegressor\n"
    
    if model == "LinearRegression":
        code.extend(["# Importing {} from sklearn\n".format(model),
        lr,
        "model = {}\n".format(model),
        "model.fit(X_train_rescaled, y_train)\n",
        "\n",
        "# Making prediction on test set\n",
        "y_pred_model = model.predict(X_test_rescaled)\n",
        "\n",
        "# Model evaluation metrics\n",
        "import numpy as np, from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error\n",
        "print(Accuracy - Train : , model.score(X_train_rescaled, y_train))\n",
        "print(Accuracy - Test : , model.score(X_test_rescaled, y_test))\n",
        "print(R2 Score : , r2_score(y_test, y_pred_model))\n",
        "print(MAE : , mean_absolute_error(y_test, y_pred_model))\n",
        "print(MSE : , mean_squared_error(y_test, y_pred_model))\n",
        "print(RMSE : , np.sqrt(mean_squared_error(y_test, y_pred_model)))\n",
        "Accuracy - Train : 88.81 %",
        "Accuracy - Test : 88.95 %",
        "R2 Score : 0.8895",
        "MAE : 844.03",
        "MSE : 1759583.50",
        "RMSE : 1326.49"])

    if model == "KNeighborsRegressors":
        code.extend(["# Importing {} from sklearn\n".format(model),
        knn,
        "model = {}\n".format(model),
        "model.fit(X_train_rescaled, y_train)\n",
        "\n",
        "# Making prediction on test set\n",
        "y_pred_model = model.predict(X_test_rescaled)\n",
        "\n",
        "# Model evaluation metrics\n",
        "import numpy as np, from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error\n",
        "print(Accuracy - Train : , model.score(X_train_rescaled, y_train))\n",
        "print(Accuracy - Test : , model.score(X_test_rescaled, y_test))\n",
        "print(R2 Score : , r2_score(y_test, y_pred_model))\n",
        "print(MAE : , mean_absolute_error(y_test, y_pred_model))\n",
        "print(MSE : , mean_squared_error(y_test, y_pred_model))\n",
        "print(RMSE : , np.sqrt(mean_squared_error(y_test, y_pred_model)))\n",
        "Accuracy - Train : 98.41 %",
        "Accuracy - Test : 97.60 %",
        "R2 Score : 0.9760",
        "MAE : 307.65",
        "MSE : 381020.50",
        "RMSE : 617.27"])

    if model == "DecisionTreeRegressor":
        code.extend(["# Importing {} from sklearn\n".format(model),
        dt,
        "model = {}\n".format(model),
        "model.fit(X_train_rescaled, y_train)\n",
        "\n",
        "# Making prediction on test set\n",
        "y_pred_model = model.predict(X_test_rescaled)\n",
        "\n",
        "# Model evaluation metrics\n",
        "import numpy as np, from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error\n",
        "print(Accuracy - Train : , model.score(X_train_rescaled, y_train))\n",
        "print(Accuracy - Test : , model.score(X_test_rescaled, y_test))\n",
        "print(R2 Score : , r2_score(y_test, y_pred_model))\n",
        "print(MAE : , mean_absolute_error(y_test, y_pred_model))\n",
        "print(MSE : , mean_squared_error(y_test, y_pred_model))\n",
        "print(RMSE : , np.sqrt(mean_squared_error(y_test, y_pred_model)))\n",
        "Accuracy - Train : 99.99 %",
        "Accuracy - Test : 96.46 %",
        "R2 Score : 0.9646",
        "MAE : 368.34",
        "MSE : 564191.59",
        "RMSE : 751.13"])
    
    if model == "RandomForestRegressor":
        code.extend(["# Importing {} from sklearn\n".format(model),
        rf,
        "model = {}\n".format(model),
        "model.fit(X_train_rescaled, y_train)\n",
        "\n",
        "# Making prediction on test set\n",
        "y_pred_model = model.predict(X_test_rescaled)\n",
        "\n",
        "# Model evaluation metrics\n",
        "import numpy as np, from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error\n",
        "print(Accuracy - Train : , model.score(X_train_rescaled, y_train))\n",
        "print(Accuracy - Test : , model.score(X_test_rescaled, y_test))\n",
        "print(R2 Score : , r2_score(y_test, y_pred_model))\n",
        "print(MAE : , mean_absolute_error(y_test, y_pred_model))\n",
        "print(MSE : , mean_squared_error(y_test, y_pred_model))\n",
        "print(RMSE : , np.sqrt(mean_squared_error(y_test, y_pred_model)))\n",
        "Accuracy - Train : 99.73 %",
        "Accuracy - Test : 98.06 %",
        "R2 Score : 0.9806",
        "MAE : 278.16",
        "MSE : 309501.40",
        "RMSE : 556.33"])

    return code

df = pd.read_csv("https://media.githubusercontent.com/media/sauravpanchal/irl/main/Week_6/Streamlit/Diamond_Streamlit_Application/diamonds.csv")
df.rename(columns={'x':'length', 'y':'width', 'z':'depth', 'depth':'depth%'}, inplace = True)
df[["length", "width", "depth"]] = df[["length", "width", "depth"]].replace(0, np.nan)
df.dropna(inplace = True)
df_features = df.drop(["price"], axis = 1)
fig, ax = plt.subplots(figsize=(15,10))

st.title("Diamond Price Prediction")
st.subheader("Get your diamond prices now !")

st.caption("Dataframe")
st.dataframe(df)

st.caption("Shape")
st.write(df.shape)

st.caption("Available Features")
st.write(list(df.columns.drop(["price"])))

st.caption("Description")
st.write(df.describe())

st.caption("Correlation between numerical features")
sns.heatmap(df.corr(), annot = True)
st.pyplot(fig)