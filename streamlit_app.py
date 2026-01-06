import streamlit as st
import pickle
import numpy as np

# Page configuration
st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="centered"
)

# Load trained model
model = pickle.load(open('model/house_model.pkl', 'rb'))

# Styling
st.markdown("""
<style>
.stApp {
    background-image: url("https://images.unsplash.com/photo-1568605114967-8130f3a36994");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}

/* Main card */
.card {
    background: rgba(255, 255, 255, 0.95);
    padding: 35px;
    border-radius: 18px;
    box-shadow: 0 8px 30px rgba(0,0,0,0.3);
    max-width: 500px;
    margin: 80px auto;
}

/* Title */
.title {
    font-size: 36px;
    font-weight: bold;
    color: #2C3E50;
    text-align: center;
}

/* Subtitle */
.subtitle {
    font-size: 17px;
    color: #555;
    text-align: center;
    margin-bottom: 25px;
}

/* Input highlight box */
.input-box {
    background-color: #EBF5FB;
    padding: 15px;
    border-radius: 12px;
    border-left: 6px solid #3498DB;
    margin-bottom: 20px;
    font-weight: bold;
}

/* Result red box */
.result-box {
    background-color: #FDEDEC;
    padding: 18px;
    border-radius: 12px;
    border-left: 8px solid #E74C3C;
    font-size: 22px;
    font-weight: bold;
    color: #922B21;
    text-align: center;
    margin-top: 20px;
}

/* Button styling */
div.stButton > button {
    background-color: #2ECC71;
    color: white;
    font-size: 18px;
    padding: 10px 24px;
    border-radius: 10px;
    border: none;
}

div.stButton > button:hover {
    background-color: #27AE60;
}
</style>
""", unsafe_allow_html=True)

# UI card
st.markdown("""
<div class="card">
    <div class="title">🏠 House Price Prediction</div>
    <div class="subtitle">Predict house prices using Machine Learning</div>
</div>
""", unsafe_allow_html=True)

# Highlighted input label
st.markdown("""
<div class="input-box">
📐 Enter House Area (in sq.ft)
</div>
""", unsafe_allow_html=True)

# Input
area = st.number_input(
    "",
    min_value=100,
    max_value=10000,
    step=50
)

# Prediction
if st.button("💰 Predict Price"):
    prediction = model.predict(np.array([[area]]))
    st.markdown(
        f"""
        <div class="result-box">
            🏷️ Predicted House Price <br><br>
            ₹ {int(prediction[0])}
        </div>
        """,
        unsafe_allow_html=True
    )