import streamlit as st
import requests
import pandas as pd
import time

# ================= PAGE CONFIG =================

st.set_page_config(
    page_title="Dhara Sampada",
    page_icon="🌾",
    layout="wide"
)

# ================= SESSION =================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ================= LOGIN PAGE =================

def login_page():

    st.markdown(
        """
        <h1 style='text-align:center;color:green;'>
        🌾 DHARA SAMPADA
        </h1>
        <h3 style='text-align:center;'>
        AI Powered Smart Agriculture Platform
        </h3>
        """,
        unsafe_allow_html=True
    )

    st.image(
        "https://images.unsplash.com/photo-1500937386664-56d1dfef3854",
        use_container_width=True
    )

    st.markdown("---")

    username = st.text_input("👤 Username")
    password = st.text_input("🔒 Password", type="password")

    if st.button("🚀 Login"):

        if username == "admin" and password == "1234":

            st.session_state.logged_in = True
            st.success("✅ Login Successful")
            time.sleep(1)
            st.rerun()

        else:
            st.error("❌ Invalid Username or Password")

# ================= MAIN APP =================

def main_app():

    # ================= SIDEBAR =================

    st.sidebar.title("🌾 Dhara Sampada")

    menu = st.sidebar.radio(
        "📌 Navigation",
        [
            "🏠 Dashboard",
            "🌦 Weather Forecast",
            "🌾 Smart Crop Advisory",
            "📈 Market Prices",
            "🏛 Government Schemes",
            "🛒 Farmer Marketplace",
            "🚜 Farm Calculator",
            "🌱 Soil Health",
            "🚨 Weather Alerts",
            "📚 Farming Tips",
            "🌐 Multilingual"
        ]
    )

    # ================= DASHBOARD =================

    if menu == "🏠 Dashboard":

        st.title("🌾 Dhara Sampada Dashboard")

        col1, col2, col3, col4 = st.columns(4)

        col1.metric("👨‍🌾 Farmers", "12,500+")
        col2.metric("🌾 Crops", "150+")
        col3.metric("📈 Market Accuracy", "96%")
        col4.metric("🌦 Weather Alerts", "24/7")

        st.markdown("---")

        st.subheader("🌟 Smart Agriculture Services")

        c1, c2, c3 = st.columns(3)

        with c1:
            st.success("🌦 Live Weather Forecast")
            st.success("🌾 AI Crop Recommendation")
            st.success("🚨 Disaster Alerts")

        with c2:
            st.success("📈 Market Price Tracking")
            st.success("🛒 Farmer Marketplace")
            st.success("🏛 Government Schemes")

        with c3:
            st.success("🌱 Soil Health Analysis")
            st.success("🚜 Farm Expense Calculator")
            st.success("🌐 Multilingual Support")

        st.image(
            "https://images.unsplash.com/photo-1464226184884-fa280b87c399",
            use_container_width=True
        )

    # ================= WEATHER =================

    elif menu == "🌦 Weather Forecast":

        st.title("🌦 Live Weather Forecast")

        city = st.text_input("Enter City", "Bangalore")

        if st.button("Get Weather"):

            api_key = "YOUR_OPENWEATHER_API_KEY"

            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

            response = requests.get(url)

            if response.status_code == 200:

                data = response.json()

                col1, col2, col3, col4 = st.columns(4)

                col1.metric(
                    "🌡 Temperature",
                    f"{data['main']['temp']} °C"
                )

                col2.metric(
                    "💧 Humidity",
                    f"{data['main']['humidity']} %"
                )

                col3.metric(
                    "☁ Condition",
                    data['weather'][0]['description']
                )

                col4.metric(
                    "💨 Wind Speed",
                    f"{data['wind']['speed']} m/s"
                )

            else:
                st.error("Weather data not found")

    # ================= WEATHER ALERTS =================

    elif menu == "🚨 Weather Alerts":

        st.title("🚨 Smart Weather Alerts")

        rainfall = st.slider("Rainfall Level", 0, 100)

        if rainfall > 70:
            st.error("⚠ Heavy Rain Alert")

        elif rainfall > 40:
            st.warning("⚠ Moderate Rainfall Expected")

        else:
            st.success("✅ Weather Safe")

    # ================= CROP ADVISORY =================

    elif menu == "🌾 Smart Crop Advisory":

        st.title("🌾 AI Crop Recommendation")

        soil = st.selectbox(
            "Select Soil Type",
            ["Black", "Red", "Alluvial"]
        )

        water = st.selectbox(
            "Water Availability",
            ["Low", "Moderate", "High"]
        )

        season = st.selectbox(
            "Season",
            ["Summer", "Winter", "Monsoon"]
        )

        if st.button("Recommend Crops"):

            crops = []

            if soil == "Black" and water == "Low":
                crops = ["Jowar", "Ragi", "Tur Dal"]

            elif soil == "Red":
                crops = ["Groundnut", "Cotton"]

            else:
                crops = ["Sugarcane", "Pomegranate"]

            st.success("🌱 Recommended Crops")

            for crop in crops:
                st.write(f"✅ {crop}")

    # ================= MARKET PRICES =================

    elif menu == "📈 Market Prices":

        st.title("📈 Live Market Price Dashboard")

        data = {
            "Crop": ["Jowar", "Ragi", "Cotton", "Tur Dal"],
            "Price": [3200, 4500, 7600, 8900]
        }

        df = pd.DataFrame(data)

        st.dataframe(df, use_container_width=True)

        st.bar_chart(df.set_index("Crop"))

    # ================= GOVERNMENT SCHEMES =================

    elif menu == "🏛 Government Schemes":

        st.title("🏛 Government Schemes Awareness")

        schemes = {
            "PM-KISAN": "₹6000 Support Per Year",
            "KUSUM": "Solar Pump Subsidy",
            "PMEGP": "Business Loan Support",
            "NABARD": "Agriculture Funding"
        }

        for scheme, details in schemes.items():
            st.info(f"✅ {scheme} → {details}")

    # ================= MARKETPLACE =================

    elif menu == "🛒 Farmer Marketplace":

        st.title("🛒 Farmer to Buyer Connectivity")

        farmer = st.text_input("Farmer Name")
        product = st.text_input("Product Name")
        quantity = st.number_input("Quantity", min_value=1)

        if st.button("Add Product"):

            st.success(
                f"✅ {product} Added Successfully"
            )

    # ================= SOIL HEALTH =================

    elif menu == "🌱 Soil Health":

        st.title("🌱 Soil Health Checker")

        ph = st.slider("Soil pH", 1.0, 14.0, 7.0)

        if ph < 6:
            st.warning("⚠ Soil is Acidic")

        elif ph > 8:
            st.warning("⚠ Soil is Alkaline")

        else:
            st.success("✅ Soil Health is Good")

    # ================= FARM CALCULATOR =================

    elif menu == "🚜 Farm Calculator":

        st.title("🚜 Farm Expense Calculator")

        seeds = st.number_input("Seed Cost", 0)
        fertilizer = st.number_input("Fertilizer Cost", 0)
        labor = st.number_input("Labor Cost", 0)
        income = st.number_input("Expected Income", 0)

        if st.button("Calculate Profit"):

            expense = seeds + fertilizer + labor
            profit = income - expense

            st.success(f"💰 Total Expense: ₹{expense}")
            st.success(f"📈 Estimated Profit: ₹{profit}")

    # ================= FARMING TIPS =================

    elif menu == "📚 Farming Tips":

        st.title("📚 Daily Farming Tips")

        tips = [
            "🌱 Use drip irrigation to save water",
            "🌾 Rotate crops for better soil fertility",
            "🐄 Organic manure improves yield",
            "☀ Monitor weather before irrigation",
            "🚜 Test soil before sowing"
        ]

        for tip in tips:
            st.success(tip)

    # ================= MULTILINGUAL =================

    elif menu == "🌐 Multilingual":

        st.title("🌐 Multilingual Support")

        language = st.selectbox(
            "Choose Language",
            ["English", "Kannada", "Hindi"]
        )

        if language == "Kannada":

            st.success("🌾 ಧಾರಾ ಸಂಪದಕ್ಕೆ ಸ್ವಾಗತ")

            st.write("✅ ಹವಾಮಾನ ಮುನ್ಸೂಚನೆ")
            st.write("✅ ಬೆಳೆ ಸಲಹೆ")
            st.write("✅ ಮಾರುಕಟ್ಟೆ ಬೆಲೆ")

        elif language == "Hindi":

            st.success("🌾 धारा संपदा में आपका स्वागत है")

            st.write("✅ मौसम पूर्वानुमान")
            st.write("✅ फसल सलाह")
            st.write("✅ बाजार मूल्य")

        else:

            st.success("🌾 Welcome to Dhara Sampada")

            st.write("✅ Weather Forecast")
            st.write("✅ Crop Advisory")
            st.write("✅ Market Prices")

# ================= APP CONTROL =================

if st.session_state.logged_in:
    main_app()
else:
    login_page()
