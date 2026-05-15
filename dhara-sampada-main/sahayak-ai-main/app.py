import streamlit as st
import requests
import pandas as pd
import time
from twilio.rest import Client
import yagmail

# ================= PAGE CONFIG =================

st.set_page_config(
    page_title="Dhara Sampada",
    page_icon="🌾",
    layout="wide"
)

# ================= API & ALERT CONFIG =================

OPENWEATHER_API_KEY = "YOUR_OPENWEATHER_API_KEY"

TWILIO_ACCOUNT_SID = "YOUR_TWILIO_ACCOUNT_SID"
TWILIO_AUTH_TOKEN = "YOUR_TWILIO_AUTH_TOKEN"
TWILIO_PHONE_NUMBER = "YOUR_TWILIO_PHONE_NUMBER"

SENDER_EMAIL = "YOUR_GMAIL@gmail.com"
SENDER_APP_PASSWORD = "YOUR_GMAIL_APP_PASSWORD"

# ================= SESSION =================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "users" not in st.session_state:
    st.session_state.users = {
        "admin": "1234"
    }

# ================= SMS FUNCTION =================

def send_sms_alert(message, phone_number):

    try:

        client = Client(
            TWILIO_ACCOUNT_SID,
            TWILIO_AUTH_TOKEN
        )

        client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=phone_number
        )

        return True

    except Exception as e:

        st.error(f"SMS Error: {e}")
        return False

# ================= EMAIL FUNCTION =================

def send_email_alert(subject, message, receiver_email):

    try:

        yag = yagmail.SMTP(
            user=SENDER_EMAIL,
            password=SENDER_APP_PASSWORD
        )

        yag.send(
            to=receiver_email,
            subject=subject,
            contents=message
        )

        return True

    except Exception as e:

        st.error(f"Email Error: {e}")
        return False

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

        password = st.text_input(
            "🔒 Password",
            type="password"
        )

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

    # ================= WEATHER FORECAST =================

    elif menu == "🌦 Weather Forecast":

        st.title("🌦 Live Weather Forecast")

        st.info(
            "Get real-time weather updates and alerts."
        )

        city = st.text_input(
            "🏙 Enter City Name",
            "Bangalore"
        )

        phone_number = st.text_input(
            "📱 Enter Mobile Number with Country Code",
            "+91"
        )

        email = st.text_input(
            "📧 Enter Gmail Address"
        )

        if st.button("🌦 Get Weather Report"):

            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"

            response = requests.get(url)

            if response.status_code == 200:

                data = response.json()

                temperature = data['main']['temp']
                humidity = data['main']['humidity']
                weather_condition = data['weather'][0]['description']
                wind_speed = data['wind']['speed']
                pressure = data['main']['pressure']

                rainfall = data.get(
                    'rain',
                    {}
                ).get('1h', 0)

                # ================= METRICS =================

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
                    "🌧 Rainfall",
                    f"{rainfall} mm"
                )

                col4, col5, col6 = st.columns(3)

                col4.metric(
                    "☁ Condition",
                    weather_condition.title()
                )

                col5.metric(
                    "💨 Wind Speed",
                    f"{wind_speed} m/s"
                )

                col6.metric(
                    "📊 Pressure",
                    f"{pressure} hPa"
                )

                st.markdown("---")

                # ================= ALERTS =================

                st.subheader("🚨 Smart Weather Alerts")

                if temperature > 38:

                    st.error("⚠ High Temperature Alert")

                elif temperature < 15:

                    st.warning("⚠ Cold Weather Alert")

                else:

                    st.success("✅ Weather Conditions Normal")

                if humidity > 85:

                    st.warning(
                        "⚠ High Humidity may damage crops"
                    )

                if rainfall > 20:

                    st.error("⚠ Heavy Rainfall Alert")

                # ================= FARMING SUGGESTIONS =================

                st.subheader("🌾 Farming Suggestions")

                if rainfall > 20:

                    st.warning(
                        "⚠ Avoid fertilizer spraying"
                    )

                    st.info(
                        "🌱 Protect crops from heavy rain"
                    )

                elif temperature > 35:

                    st.warning(
                        "⚠ Use drip irrigation"
                    )

                    st.info(
                        "🌱 Grow heat-resistant crops"
                    )

                else:

                    st.success(
                        "✅ Suitable Weather for Farming"
                    )

                # ================= WEATHER SUMMARY =================

                st.subheader("📋 Weather Summary")

                weather_df = pd.DataFrame({

                    "Parameter": [
                        "Temperature",
                        "Humidity",
                        "Condition",
                        "Wind Speed",
                        "Pressure",
                        "Rainfall"
                    ],

                    "Value": [
                        f"{temperature} °C",
                        f"{humidity}%",
                        weather_condition,
                        f"{wind_speed} m/s",
                        f"{pressure} hPa",
                        f"{rainfall} mm"
                    ]
                })

                st.dataframe(
                    weather_df,
                    use_container_width=True
                )

                # ================= ALERT MESSAGE =================

                alert_message = f"""
🌾 Dhara Sampada Weather Alert

City: {city}

Temperature: {temperature}°C
Humidity: {humidity}%
Condition: {weather_condition}
Wind Speed: {wind_speed} m/s
Pressure: {pressure} hPa
Rainfall: {rainfall} mm

Stay Safe & Plan Farming Accordingly.
"""

                # ================= SEND ALERT =================

                if st.button("📨 Send SMS & Gmail Alert"):

                    sms_sent = False
                    email_sent = False

                    if phone_number.strip() != "+91":

                        sms_sent = send_sms_alert(
                            alert_message,
                            phone_number
                        )

                    if email.strip() != "":

                        email_sent = send_email_alert(
                            "Dhara Sampada Weather Alert",
                            alert_message,
                            email
                        )

                    if sms_sent:
                        st.success("✅ SMS Alert Sent")

                    if email_sent:
                        st.success("✅ Email Alert Sent")

            else:

                st.error(
                    "❌ Unable to Fetch Weather Data"
                )

    # ================= WEATHER ALERTS =================

    elif menu == "🚨 Weather Alerts":

        st.title("🚨 Smart Weather Alerts")

        rainfall = st.slider(
            "Rainfall Level",
            0,
            100
        )

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

        if st.button("Recommend Crops"):

            if soil == "Black":

                crops = ["Jowar", "Ragi"]

            elif soil == "Red":

                crops = ["Groundnut", "Cotton"]

            else:

                crops = ["Sugarcane"]

            st.success("🌱 Recommended Crops")

            for crop in crops:

                st.write(f"✅ {crop}")

    # ================= MARKET PRICES =================

    elif menu == "📈 Market Prices":

        st.title("📈 Market Prices")

        df = pd.DataFrame({

            "Crop": [
                "Jowar",
                "Ragi",
                "Cotton"
            ],

            "Price": [
                3200,
                4500,
                7600
            ]
        })

        st.dataframe(
            df,
            use_container_width=True
        )

        st.bar_chart(
            df.set_index("Crop")
        )

    # ================= GOVERNMENT SCHEMES =================

    elif menu == "🏛 Government Schemes":

        st.title("🏛 Government Schemes")

        st.info("✅ PM-KISAN → ₹6000 Support")

        st.info("✅ KUSUM → Solar Subsidy")

        st.info("✅ NABARD → Agriculture Funding")

    # ================= MARKETPLACE =================

    elif menu == "🛒 Farmer Marketplace":

        st.title("🛒 Farmer Marketplace")

        farmer = st.text_input("Farmer Name")

        product = st.text_input("Product Name")

        quantity = st.number_input(
            "Quantity",
            min_value=1
        )

        if st.button("Add Product"):

            st.success(
                f"✅ {product} Added Successfully"
            )

    # ================= SOIL HEALTH =================

    elif menu == "🌱 Soil Health":

        st.title("🌱 Soil Health")

        ph = st.slider(
            "🧪 Soil pH",
            1.0,
            14.0,
            7.0
        )

        if ph < 6:

            st.warning("⚠ Soil is Acidic")

        elif ph > 8:

            st.warning("⚠ Soil is Alkaline")

        else:

            st.success("✅ Soil Health is Good")

    # ================= FARM CALCULATOR =================

    elif menu == "🚜 Farm Calculator":

        st.title("🚜 Farm Calculator")

        seeds = st.number_input(
            "Seed Cost",
            0
        )

        fertilizer = st.number_input(
            "Fertilizer Cost",
            0
        )

        labor = st.number_input(
            "Labor Cost",
            0
        )

        income = st.number_input(
            "Expected Income",
            0
        )

        if st.button("Calculate Profit"):

            expense = seeds + fertilizer + labor

            profit = income - expense

            st.success(
                f"💰 Total Expense: ₹{expense}"
            )

            st.success(
                f"📈 Estimated Profit: ₹{profit}"
            )

    # ================= FARMING TIPS =================

    elif menu == "📚 Farming Tips":

        st.title("📚 Daily Farming Tips")

        tips = [

            "🌱 Use drip irrigation",

            "🌾 Rotate crops",

            "🐄 Use organic manure",

            "☀ Monitor weather before irrigation"
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

            st.success(
                "🌾 ಧಾರಾ ಸಂಪದಕ್ಕೆ ಸ್ವಾಗತ"
            )

        elif language == "Hindi":

            st.success(
                "🌾 धारा संपदा में आपका स्वागत है"
            )

        else:

            st.success(
                "🌾 Welcome to Dhara Sampada"
            )

# ================= APP CONTROL =================

if st.session_state.logged_in:

    main_app()

else:

    auth_page()
