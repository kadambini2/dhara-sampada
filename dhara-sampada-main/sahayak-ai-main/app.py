import streamlit as st
import requests

st.set_page_config(
    page_title="Sahayak AI",
    layout="wide"
)

st.title("🌾 Sahayak AI")
st.subheader("Smart Agriculture Assistant")

# ================= WEATHER =================

st.header("🌦 Weather Forecast")

city = st.text_input("Enter City", "Bangalore")

if st.button("Get Weather"):

    api_key = "YOUR_OPENWEATHER_API_KEY"

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        st.success(f"Weather in {city}")

        st.write(f"🌡 Temperature: {data['main']['temp']} °C")
        st.write(f"💧 Humidity: {data['main']['humidity']} %")
        st.write(f"☁ Condition: {data['weather'][0]['description']}")

    else:
        st.error("Weather data not found")

# ================= CROP ADVISORY =================

st.header("🌾 Smart Crop Advisory")

soil = st.selectbox(
    "Select Soil Type",
    ["Black", "Red", "Alluvial"]
)

water = st.selectbox(
    "Water Availability",
    ["Low", "Moderate", "High"]
)

if st.button("Recommend Crops"):

    crops = []

    if soil == "Black" and water == "Low":
        crops = ["Jowar", "Ragi", "Tur Dal"]

    elif soil == "Red":
        crops = ["Groundnut", "Cotton"]

    else:
        crops = ["Sugarcane", "Pomegranate"]

    st.success("Recommended Crops")

    for crop in crops:
        st.write(f"✅ {crop}")

# ================= MARKET PRICES =================

st.header("📈 Market Prices")

market_prices = {
    "Jowar": 3200,
    "Ragi": 4500,
    "Cotton": 7600,
    "Tur Dal": 8900
}

for crop, price in market_prices.items():
    st.write(f"🌱 {crop} : ₹{price}")

# ================= GOVERNMENT SCHEMES =================

st.header("🏛 Government Schemes")

schemes = [
    "PM-KISAN",
    "KUSUM",
    "PMEGP",
    "NABARD"
]

for scheme in schemes:
    st.write(f"✅ {scheme}")

# ================= FARMER MARKETPLACE =================

st.header("🛒 Farmer to Buyer Marketplace")

farmer = st.text_input("Farmer Name")
product = st.text_input("Product")
quantity = st.number_input("Quantity", min_value=1)

if st.button("Add Product"):

    st.success(
        f"{product} added successfully by {farmer}"
    )

# ================= FARM CALCULATOR =================

st.header("🚜 Farm Management Tool")

seeds = st.number_input("Seed Cost", 0)
fertilizer = st.number_input("Fertilizer Cost", 0)
labor = st.number_input("Labor Cost", 0)
income = st.number_input("Expected Income", 0)

if st.button("Calculate Profit"):

    expense = seeds + fertilizer + labor
    profit = income - expense

    st.write(f"💰 Total Expense: ₹{expense}")
    st.write(f"📈 Estimated Profit: ₹{profit}")

# ================= MULTILINGUAL =================

st.header("🌐 Language")

language = st.selectbox(
    "Select Language",
    ["English", "Kannada", "Hindi"]
)

if language == "Kannada":
    st.success("ಸಹಾಯಕ AI ಗೆ ಸ್ವಾಗತ")

elif language == "Hindi":
    st.success("सहायक AI में आपका स्वागत है")

else:
    st.success("Welcome to Sahayak AI")
