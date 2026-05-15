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

if "users" not in st.session_state:
    st.session_state.users = {
        "admin": "1234"
    }

# ================= AUTH PAGE =================

def auth_page():

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

    auth_option = st.radio(
        "Select Option",
        ["🔐 Login", "📝 Sign Up"]
    )

    # ================= LOGIN =================

    if auth_option == "🔐 Login":

        username = st.text_input("👤 Username")
        password = st.text_input("🔒 Password", type="password")

        if st.button("🚀 Login"):

            if username in st.session_state.users:

                if st.session_state.users[username] == password:

                    st.session_state.logged_in = True
                    st.success("✅ Login Successful")

                    time.sleep(1)

                    st.rerun()

                else:
                    st.error("❌ Incorrect Password")

            else:
                st.error("❌ User Not Found")

    # ================= SIGNUP =================

    else:

        st.subheader("📝 Create New Account")

        new_user = st.text_input("👤 Create Username")

        new_pass = st.text_input(
            "🔒 Create Password",
            type="password"
        )

        confirm_pass = st.text_input(
            "🔒 Confirm Password",
            type="password"
        )

        if st.button("✅ Sign Up"):

            if new_user == "" or new_pass == "":

                st.warning("⚠ Please Fill All Fields")

            elif new_user in st.session_state.users:

                st.error("❌ Username Already Exists")

            elif new_pass != confirm_pass:

                st.error("❌ Passwords Do Not Match")

            else:

                st.session_state.users[new_user] = new_pass

                st.success(
                    "✅ Account Created Successfully"
                )

                st.info(
                    "Now Login Using Your Credentials"
                )

# ================= MAIN APP =================

def main_app():

    # ================= SIDEBAR =================

    st.sidebar.title("🌾 Dhara Sampada")

    st.sidebar.success("✅ Logged In")

    if st.sidebar.button("🚪 Logout"):

        st.session_state.logged_in = False
        st.rerun()

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

        st.info("Get real-time weather updates, rainfall alerts, humidity, and farming suggestions.")

        city = st.text_input("🏙 Enter City Name", "Bangalore")

        if st.button("🌦 Get Weather Report"):

            api_key = "YOUR_OPENWEATHER_API_KEY"

            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

            response = requests.get(url)

            if response.status_code == 200:

                data = response.json()

                temperature = data['main']['temp']
                humidity = data['main']['humidity']
                weather_condition = data['weather'][0]['description']
                wind_speed = data['wind']['speed']
                pressure = data['main']['pressure']

                col1, col2, col3 = st.columns(3)

                col1.metric(
                    "🌡 Temperature",
                    f"{temperature} °C"
                )

                col2.metric(
                    "💧 Humidity",
                    f"{humidity}%"
                )

                col3.metric(
                    "💨 Wind Speed",
                    f"{wind_speed} m/s"
                )

                col4, col5 = st.columns(2)

                col4.metric(
                    "☁ Condition",
                    weather_condition.title()
                )

                col5.metric(
                    "📊 Pressure",
                    f"{pressure} hPa"
                )

                st.markdown("---")

                st.subheader("🚨 Smart Weather Alerts")

                if temperature > 38:
                    st.error("⚠ High Temperature Alert!")

                elif temperature < 15:
                    st.warning("⚠ Cold Weather Alert!")

                else:
                    st.success("✅ Weather Conditions are Normal")

                if humidity > 85:
                    st.warning("⚠ High Humidity may cause fungal diseases.")

                st.subheader("🌾 Farming Suggestions")

                if "rain" in weather_condition.lower():

                    st.success("✅ Good time for sowing crops")

                    st.write("🌱 Recommended Crops:")
                    st.write("- Paddy")
                    st.write("- Sugarcane")
                    st.write("- Cotton")

                elif temperature > 35:

                    st.warning("⚠ Use drip irrigation to save water")

                    st.write("🌱 Heat Resistant Crops:")
                    st.write("- Jowar")
                    st.write("- Bajra")
                    st.write("- Ragi")

                else:

                    st.success("✅ Suitable weather for farming")

                st.subheader("📋 Weather Summary")

                weather_df = {
                    "Parameter": [
                        "Temperature",
                        "Humidity",
                        "Condition",
                        "Wind Speed",
                        "Pressure"
                    ],

                    "Value": [
                        f"{temperature} °C",
                        f"{humidity}%",
                        weather_condition,
                        f"{wind_speed} m/s",
                        f"{pressure} hPa"
                    ]
                }

                df = pd.DataFrame(weather_df)

                st.dataframe(
                    df,
                    use_container_width=True
                )

            else:

                st.error("❌ Unable to Fetch Weather Data")

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

        st.title("🌱 Advanced Soil Analysis")

        st.info("Analyze soil nutrients and get smart crop & fertilizer recommendations.")

        ph = st.slider("🧪 Soil pH", 1.0, 14.0, 7.0)

        nitrogen = st.slider("🌿 Nitrogen (N)", 0, 100, 50)

        phosphorus = st.slider("🧬 Phosphorus (P)", 0, 100, 50)

        potassium = st.slider("⚡ Potassium (K)", 0, 100, 50)

        moisture = st.slider("💧 Soil Moisture (%)", 0, 100, 50)

        if st.button("🔍 Analyze Soil"):

            st.subheader("📊 Soil Health Report")

            if ph < 6:

                st.warning("⚠ Soil is Acidic")
                st.write("✅ Add lime to balance soil pH")

            elif ph > 8:

                st.warning("⚠ Soil is Alkaline")
                st.write("✅ Add organic compost or gypsum")

            else:

                st.success("✅ Soil pH is Ideal")

            st.subheader("🧪 Nutrient Analysis")

            if nitrogen < 40:
                st.error("⚠ Nitrogen is Low")
            else:
                st.success("✅ Nitrogen Level is Good")

            if phosphorus < 40:
                st.error("⚠ Phosphorus is Low")
            else:
                st.success("✅ Phosphorus Level is Good")

            if potassium < 40:
                st.error("⚠ Potassium is Low")
            else:
                st.success("✅ Potassium Level is Good")

            if moisture < 30:

                st.warning("⚠ Soil Moisture is Low")
                st.write("💧 Irrigation Recommended")

            else:

                st.success("✅ Soil Moisture is Sufficient")

            st.subheader("🌾 Recommended Crops")

            recommended_crops = []

            if ph >= 6 and ph <= 7.5:

                if moisture > 50:
                    recommended_crops.extend(
                        ["Paddy", "Sugarcane"]
                    )

                else:
                    recommended_crops.extend(
                        ["Wheat", "Maize"]
                    )

            elif ph < 6:

                recommended_crops.extend(
                    ["Potato", "Tea", "Groundnut"]
                )

            else:

                recommended_crops.extend(
                    ["Cotton", "Barley", "Ragi"]
                )

            for crop in recommended_crops:
                st.success(f"✅ {crop}")

            st.subheader("🧴 Fertilizer Recommendations")

            fertilizers = []

            if nitrogen < 40:
                fertilizers.append("Urea")

            if phosphorus < 40:
                fertilizers.append("DAP")

            if potassium < 40:
                fertilizers.append("MOP (Muriate of Potash)")

            if len(fertilizers) == 0:

                st.success(
                    "✅ No Major Fertilizer Needed"
                )

            else:

                for fert in fertilizers:
                    st.info(f"🌱 Recommended: {fert}")

            st.subheader("📋 Soil Summary")

            soil_data = {
                "Parameter": [
                    "pH",
                    "Nitrogen",
                    "Phosphorus",
                    "Potassium",
                    "Moisture"
                ],

                "Value": [
                    ph,
                    nitrogen,
                    phosphorus,
                    potassium,
                    f"{moisture}%"
                ]
            }

            soil_df = pd.DataFrame(soil_data)

            st.dataframe(
                soil_df,
                use_container_width=True
            )

            st.subheader("🏆 Overall Soil Health Score")

            score = (
                nitrogen +
                phosphorus +
                potassium +
                moisture
            ) / 4

            if score >= 75:
                st.success(f"🌟 Excellent Soil Health ({score:.1f}%)")

            elif score >= 50:
                st.warning(f"⚠ Moderate Soil Health ({score:.1f}%)")

            else:
                st.error(f"❌ Poor Soil Health ({score:.1f}%)")

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

        elif language == "Hindi":

            st.success("🌾 धारा संपदा में आपका स्वागत है")

        else:

            st.success("🌾 Welcome to Dhara Sampada")

# ================= APP CONTROL =================

if st.session_state.logged_in:
    main_app()
else:
    auth_page()
