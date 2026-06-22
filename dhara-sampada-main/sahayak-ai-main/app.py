# ================= IMPORTS =================

import streamlit as st
import pandas as pd
import time
from fpdf import FPDF

# ================= PAGE CONFIG =================

st.set_page_config(
    page_title="Dhara Sampada",
    page_icon="🌾",
    layout="wide"
)

# ================= SESSION STATE INIT =================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "users" not in st.session_state:
    st.session_state.users = {
        "admin": "1234"
    }

if "lands" not in st.session_state:
    st.session_state.lands = []

# ================= AUTHENTICATION PAGE =================

def auth_page():
    st.title("🌾 DHARA SAMPADA")
    st.subheader("AI Powered Smart Agriculture Platform")

    option = st.radio("Select Action", ["🔐 Login", "📝 Sign Up"])

    # ---------- LOGIN ----------
    if option == "🔐 Login":
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            if username in st.session_state.users:
                if st.session_state.users[username] == password:
                    st.session_state.logged_in = True
                    st.success("Login Successful!")
                    time.sleep(0.5)
                    st.rerun()
                else:
                    st.error("Incorrect Password")
            else:
                st.error("User Not Found")

    # ---------- SIGNUP ----------
    else:
        username = st.text_input("Create Username")
        password = st.text_input("Create Password", type="password")
        confirm = st.text_input("Confirm Password", type="password")

        if st.button("Sign Up"):
            if not username:
                st.error("Username cannot be empty")
            elif password != confirm:
                st.error("Passwords do not match")
            elif username in st.session_state.users:
                st.error("Username already exists")
            else:
                st.session_state.users[username] = password
                st.success("Account Created Successfully! Please switch to Login.")

# ================= MAIN APPLICATION =================

def main_app():
    st.sidebar.title("🌾 Dhara Sampada")
    
    if st.sidebar.button("🚪 Logout"):
        st.session_state.logged_in = False
        st.rerun()

    menu = st.sidebar.radio(
        "Navigation",
        [
            "🏠 Dashboard",
            "🌦 Weather Forecast",
            "🌾 Smart Crop Advisory",
            "📈 Market Prices",
            "🌱 Soil Health",
            "📑 Land Records",
            "📊 Reports",
            "🔔 Notifications",
            "🏛 Government Schemes",
            "🛒 Farmer Marketplace",
            "🚜 Farm Calculator",
            "📚 Farming Tips",
            "🌐 Multilingual",
            "👤 Profile"
        ]
    )

    # ================= DASHBOARD =================
    if menu == "🏠 Dashboard":
        st.title("🌾 Dhara Sampada Dashboard")
        
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("👨‍🌾 Registered Farmers", "12,500+")
        c2.metric("🌾 Tracked Land Records", len(st.session_state.lands))
        c3.metric("📈 Model Accuracy", "96%")
        c4.metric("🌦 System Alerts", "Active (24/7)")

    # ================= WEATHER =================
    elif menu == "🌦 Weather Forecast":
        st.title("🌦 Weather Forecast")
        city = st.text_input("Enter City Name", "Bangalore")

        if st.button("Get Weather"):
            st.info(f"Displaying mockup weather information for {city}")
            w_c1, w_c2, w_c3 = st.columns(3)
            w_c1.metric("Temperature", "30°C")
            w_c2.metric("Humidity", "65%")
            w_c3.metric("Condition", "Sunny")

    # ================= CROP =================
    elif menu == "🌾 Smart Crop Advisory":
        st.title("🌾 AI Crop Recommendation")
        soil = st.selectbox("Select Soil Type", ["Black", "Red", "Alluvial"])

        if st.button("Recommend Crops"):
            if soil == "Black":
                st.success("Recommended: Cotton, Jowar")
            elif soil == "Red":
                st.success("Recommended: Groundnut, Ragi")
            else:
                st.success("Recommended: Paddy, Sugarcane")

    # ================= MARKET =================
    elif menu == "📈 Market Prices":
        st.title("📈 Live Market Prices")
        
        df = pd.DataFrame({
            "Crop": ["Cotton", "Jowar", "Paddy", "Ragi"],
            "Price (per Quintal)": [7600, 3200, 2400, 4500]
        })
        
        st.dataframe(df, use_container_width=True)
        st.bar_chart(df.set_index("Crop"))

    # ================= SOIL =================
    elif menu == "🌱 Soil Health":
        st.title("🌱 Soil Health Analysis")
        
        ph = st.slider("pH Value", 1.0, 14.0, 7.0, step=0.1)
        moisture = st.slider("Moisture %", 0, 100, 50)

        if st.button("Analyze Soil"):
            if 6.0 <= ph <= 7.5:
                st.success(f"Healthy Soil (pH: {ph})")
            else:
                st.warning(f"Suboptimal Soil Chemistry (pH: {ph}). Optimization required.")
            st.write(f"Current Moisture Level: **{moisture}%**")

    # ================= LAND RECORDS =================
    elif menu == "📑 Land Records":
        st.title("📑 Land Registration Records")
        
        survey = st.text_input("Survey Number")
        owner = st.text_input("Owner Name")
        area = st.number_input("Area (Acres)", min_value=0.0, step=0.1)
        village = st.text_input("Village")

        if st.button("Save Land Record"):
            if survey and owner and village and area > 0:
                st.session_state.lands.append({
                    "Survey No": survey,
                    "Owner": owner,
                    "Area": area,
                    "Village": village
                })
                st.success("Record Saved Successfully!")
            else:
                st.error("Please fill in all details before saving.")

        if st.session_state.lands:
            st.write("### Registered Plots")
            st.dataframe(pd.DataFrame(st.session_state.lands), use_container_width=True)

    # ================= REPORTS =================
    elif menu == "📊 Reports":
        st.title("📊 Dhara Sampada Insights & Reports")

        if not st.session_state.lands:
            st.warning("No Land Records available to compile metrics or generate files.")
        else:
            df = pd.DataFrame(st.session_state.lands)

            c1, c2, c3 = st.columns(3)
            c1.metric("Total Records", len(df))
            c2.metric("Unique Villages", df["Village"].nunique())
            c3.metric("Total Covered Area", f"{df['Area'].sum()} Acres")

            st.dataframe(df, use_container_width=True)

            st.subheader("Area Distribution by Village")
            area_df = df.groupby("Village")["Area"].sum().reset_index()
            st.bar_chart(area_df.set_index("Village"))

            # CSV Data Export
            csv_data = df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="⬇️ Download Data as CSV",
                data=csv_data,
                file_name="Dhara_Sampada_Report.csv",
                mime="text/csv"
            )

            # In-Memory PDF Generation (Fixes multi-step download buttons)
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", "B", 16)
            pdf.cell(200, 10, "DHARA SAMPADA AGRI-REPORT", ln=True, align="C")
            pdf.ln(10)
            pdf.set_font("Arial", size=11)

            for idx, row in df.iterrows():
                text = (
                    f"Record {idx+1} -> Survey No: {row['Survey No']} | "
                    f"Owner: {row['Owner']} | Area: {row['Area']} Acres | "
                    f"Village: {row['Village']}"
                )
                pdf.multi_cell(0, 8, text)
                
            # Render directly to string/bytes output stream safely 
            pdf_bytes = pdf.output(dest='S').encode('latin-1')

            st.download_button(
                label="📄 Download Compiled PDF Report",
                data=pdf_bytes,
                file_name="Dhara_Sampada_Report.pdf",
                mime="application/pdf"
            )

    # ================= NOTIFICATIONS =================
    elif menu == "🔔 Notifications":
        st.title("🔔 Real-time Advisories")
        st.success("🌧️ Heavy Rain Expected over South Peninsula regions within 48 hours.")
        st.info("💰 PM-KISAN installment funds have been credited to registered accounts.")
        st.warning("🌾 Cotton Market Alert: Price index decreased marginally by 2.1%.")

    # ================= SCHEMES =================
    elif menu == "🏛 Government Schemes":
        st.title("🏛 Active Agriculture Schemes")
        st.info("**PM-KISAN:** ₹6,000 yearly income support directly routed to farmers.")
        st.info("**KUSUM Scheme:** High-subsidy solar power pumps installation processing.")
        st.info("**NABARD Subsidies:** Institutional low-interest microfinancing for farm infrastructure.")

    # ================= MARKETPLACE =================
    elif menu == "🛒 Farmer Marketplace":
        st.title("🛒 B2B Farmer Marketplace")
        
        farmer = st.text_input("Farmer/Seller Name")
        product = st.text_input("Product Name (e.g., Organic Wheat)")
        quantity = st.number_input("Quantity (Quintals)", min_value=1)

        if st.button("List Product"):
            if farmer and product:
                st.success(f"Success: {quantity} unit(s) of '{product}' listed under {farmer}.")
            else:
                st.error("Please completely fill listing specifications.")

    # ================= CALCULATOR =================
    elif menu == "🚜 Farm Calculator":
        st.title("🚜 Budget & Profit Projections")
        
        seed = st.number_input("Seed Procurement Cost (₹)", min_value=0)
        fertilizer = st.number_input("Fertilizers & Nutrients Cost (₹)", min_value=0)
        labor = st.number_input("Labor Operation Cost (₹)", min_value=0)
        income = st.number_input("Target Expected Gross Revenue (₹)", min_value=0)

        if st.button("Calculate Operating Metrics"):
            expense = seed + fertilizer + labor
            profit = income - expense
            
            st.metric("Total Operational Expense", f"₹{expense}")
            if profit >= 0:
                st.metric("Net Projected Profit", f"₹{profit}")
            else:
                st.metric("Net Projected Deficit", f"₹{abs(profit)}", delta="-Loss")

    # ================= TIPS =================
    elif menu == "📚 Farming Tips":
        st.title("📚 Agronomy Practices Best Practices")
        st.markdown("""
        * **🌱 Precision Irrigation:** Deploy Drip or Sprinkler systems to conserve up to 40% water.
        * **🌾 Crop Rotation:** Alternate Legumes with cereals to keep nitrogen-fixation active.
        * **🚜 Diagnostics:** Test soil composition every 2 seasons to calibrate nutrient feed.
        """)

    # ================= LANGUAGE =================
    elif menu == "🌐 Multilingual":
        st.title("🌐 Language Selection / ಭಾಷೆ / भाषा")
        lang = st.selectbox("Choose Interface Language", ["English", "Kannada", "Hindi"])

        if lang == "Kannada":
            st.success("ಧಾರಾ ಸಂಪದಕ್ಕೆ ಸ್ವಾಗತ — ಉತ್ತಮ ಕೃಷಿ ನಿರ್ವಹಣೆ ವ್ಯವಸ್ಥೆ.")
        elif lang == "Hindi":
            st.success("धारा संपदा में आपका स्वागत है — उन्नत कृषि प्रबंधन मंच।")
        else:
            st.success("Welcome to Dhara Sampada — Smart Farm Optimization Platform.")

    # ================= PROFILE =================
    elif menu == "👤 Profile":
        st.title("👤 User Profile Details")
        st.text("Status     : Active Verified User")
        st.text("Access Tier: Core Member Application")

# ================= CORE APP CONTROLLER =================

if st.session_state.logged_in:
    main_app()
else:
    auth_page()
