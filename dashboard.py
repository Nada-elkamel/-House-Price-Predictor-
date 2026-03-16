import streamlit as st
import pandas as pd
import pickle
import os

# Page configuration
st.set_page_config(
    page_title="House Price Predictor",
    page_icon="🏠",
    layout="wide"
)

# ---------- COMPACT CSS (NO SCROLL) ----------
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
header {visibility: hidden;}
footer {visibility: hidden;}

.stApp {
    background: linear-gradient(135deg,#0f2027,#203a43,#2c5364);
    color:white;
}

/* Force container to fit screen height */
.block-container {
    padding-top: 1.5rem !important;
    padding-bottom: 0rem !important;
    height: 100vh;
}

/* Compact inputs */
div.stNumberInput, div.stSelectbox {
    margin-bottom: -10px;
}

.result-container {
    background: rgba(255,255,255,0.08);
    padding: 40px;
    border-radius: 20px;
    text-align: center;
    border: 1px solid rgba(255,255,255,0.2);
    height: 80vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.price-text {
    font-size: 5rem;
    font-weight: bold;
    color: #00ffcc;
    margin: 0;
}
</style>
""", unsafe_allow_html=True)

# ---------- LOAD MODEL ----------
base_dir = os.path.dirname(__file__)
model_path = os.path.join(base_dir, "house_model.pkl")
columns_path = os.path.join(base_dir, "model_columns.pkl")

@st.cache_resource
def load_assets():
    with open(model_path, "rb") as f:
        model = pickle.load(f)
    with open(columns_path, "rb") as f:
        model_columns = pickle.load(f)
    return model, model_columns

try:
    model, model_columns = load_assets()
except Exception:
    st.error("Model files not found.")
    st.stop()

# ---------- TWO-PART LAYOUT ----------
left_col, right_col = st.columns([1.2, 1], gap="large")

with left_col:
    st.markdown("### 📐 Property Details")
    
    # Nested columns to keep input rows tight
    r1c1, r1c2 = st.columns(2)
    area = r1c1.number_input("Area (sqft)", 200, 10000, 1500)
    bedrooms = r1c2.number_input("Bedrooms", 1, 10, 3)
    
    r2c1, r2c2 = st.columns(2)
    bathrooms = r2c1.number_input("Bathrooms", 1, 10, 2)
    stories = r2c2.number_input("Stories", 1, 4, 1)
    
    r3c1, r3c2 = st.columns(2)
    parking = r3c1.number_input("Parking Spots", 0, 5, 1)
    mainroad = r3c2.selectbox("Main Road Access", ["Yes", "No"])

    st.markdown("---")
    st.markdown("### 🏡 Amenities")
    
    r4c1, r4c2, r4c3 = st.columns(3)
    guestroom = r4c1.selectbox("Guest Room", ["Yes", "No"])
    basement = r4c2.selectbox("Basement", ["Yes", "No"])
    airconditioning = r4c3.selectbox("AC", ["Yes", "No"])
    
    r5c1, r5c2, r5c3 = st.columns(3)
    hotwaterheating = r5c1.selectbox("Hot Water", ["Yes", "No"])
    prefarea = r5c2.selectbox("Pref. Area", ["Yes", "No"])
    furnishingstatus = r5c3.selectbox("Furnishing", ["Furnished", "Semi-Furnished", "Unfurnished"])

# ---------- PREDICTION LOGIC ----------
input_dict = {
    "area": area, "bedrooms": bedrooms, "bathrooms": bathrooms, "stories": stories, "parking": parking,
    "mainroad_yes": 1 if mainroad == "Yes" else 0,
    "guestroom_yes": 1 if guestroom == "Yes" else 0,
    "basement_yes": 1 if basement == "Yes" else 0,
    "airconditioning_yes": 1 if airconditioning == "Yes" else 0,
    "hotwaterheating_yes": 1 if hotwaterheating == "Yes" else 0,
    "prefarea_yes": 1 if prefarea == "Yes" else 0,
    "furnishingstatus_semi-furnished": 1 if furnishingstatus == "Semi-Furnished" else 0,
    "furnishingstatus_unfurnished": 1 if furnishingstatus == "Unfurnished" else 0,
}

features = pd.DataFrame([input_dict]).reindex(columns=model_columns, fill_value=0)
prediction = model.predict(features)[0]

# ---------- RIGHT COLUMN: THE RESULT ----------
with right_col:
    st.markdown(f"""
    <div class="result-container">
        <h2 style="margin-bottom:0;">🏠 House Price Predictor</h2>
        <p style="opacity:0.7;">Instant Live Valuation</p>
        <hr style="width:50%; border-color:rgba(255,255,255,0.1);">
        <p style="font-size:1.2rem; margin-top:20px;">Estimated Market Value</p>
        <p class="price-text">${prediction:,.0f}</p>
        <div style="margin-top:30px; padding:15px; background:rgba(0,0,0,0.2); border-radius:10px; width:80%;">
            <small>Adjust any value on the left to see the price update in real-time.</small>
        </div>
    </div>
    """, unsafe_allow_html=True)