# ================= IMPORTS =================

import streamlit as st
import pandas as pd
import numpy as np
import time

# ================= PAGE CONFIG =================

st.set_page_config(
    page_title="Dhara Sampada | Next-Gen Agri-Platform",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ================= CUSTOM CSS FOR PREMIUM UI/UX =================

st.markdown("""
    <style>
    /* Main Background & Font Tweaks */
    .stApp {
        background-color: #fcfdfa;
    }
    
    /* Custom Card Design */
    .metric-card {
        background-color: #ffffff;
        border: 1px solid #e1e8dc;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.02);
        margin-bottom: 15px;
    }
    
    /* Status indicators */
    .status-good {
        color: #2e7d32;
        font-weight: bold;
    }
    .status-warn {
        color: #ef6c00;
        font-weight: bold;
    }
    </style>
""", unsafe_index=True)

# ================= SESSION STATE INIT =================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "users" not in st.session_state:
    st.session_state.users = {"admin": "1234"}

if "lands" not in st.session_state:
    # Adding mock data initially for a vibrant UI/UX on first load
    st.session_state.lands = [
        {"Survey No": "SRV-201", "Owner": "Ramesh Kumar", "Area": 4.5, "Village": "Malur", "Soil": "Black"},
        {"Survey No": "SRV-404", "Owner": "Suresh Gowda", "Area": 2.2, "Village": "Channapatna", "Soil": "Red"}
    ]

# ================= AUTHENTICATION PAGE =================

def auth_page():
    st.markdown("<h1 style='text-align: center; color: #2e7d32;'>🌾 DHARA SAMPADA</h1>", unsafe_html=True)
    st.markdown("<p style='text-align: center; font-size:1.2rem; color: #555;'>Next-Generation AI Precision Agriculture Platform</p>", unsafe_html=True)
    st.markdown("---")

    col1, col2, col3 = st.columns([1, 1.5, 1])
    with col2:
        option = st.radio("Select Action", ["🔐 Secure Login", "📝 Farmer Registration"], horizontal=True)
        st.write("")
        
        if option == "🔐 Secure Login":
            username = st.text_input("Username / Mobile Number")
            password = st.text_input("Password", type="password")

            if st.button("Access Dashboard", use_container_width=True):
                if username in st.session_state.users:
                    if st.session_state.users[username] == password:
                        st.session_state.logged_in = True
                        st.success("Authentication successful! Loading control center...")
                        time.sleep(0.5)
                        st.rerun()
                    else:
                        st.error("Invalid password security credentials.")
                else:
                    st.error("User profile not identified.")

        else:
            username = st.text_input("Create Username")
            password = st.text_input("Create Password", type="password")
            confirm = st.text_input("Confirm Password", type="password")

            if st.button("Register Account", use_container_width=True):
                if not username:
                    st.error("Username cannot be empty.")
                elif password != confirm:
                    st.error("Passwords do not match.")
                elif username in st.session_state.users:
                    st.error("Username profile already exists.")
                else:
                    st.session_state.users[username] = password
                    st.success("Registration complete! Switch to Login option above.")

# ================= MAIN APPLICATION =================

def main_app():
    # Sidebar Navigation Styling
    st.sidebar.markdown("<h2 style='color: #2e7d32; padding-bottom: 0;'>🌾 Dhara Sampada</h2>", unsafe_html=True)
    st.sidebar.markdown("<p style='font-size: 0.85rem; color: #777;'>Precision Operating Matrix</p>", unsafe_html=True)
    
    if st.sidebar.button("🚪 Terminate Session", use_container_width=True):
        st.session_state.logged_in = False
        st.rerun()

    st.sidebar.markdown("---")
    menu = st.sidebar.radio(
        "⚡ CONTROL PANELS",
        [
            "🏠 Executive Dashboard",
            "🛰️ Satellite Crop Monitor",
            "🪲 AI Pest Diagnostic",
            "💧 Precision Irrigation",
            "🌾 Smart Crop Advisory",
            "🌦 Weather Forecast",
            "📈 Live Market Prices",
            "🌱 Soil Health Matrix",
            "📑 Land Ledger Records",
            "📊 Analytics & Reports",
            "🔔 Advisory Bulletins",
            "🏛 Gov Schemes Hub",
            "🛒 Farm Marketplace",
            "🚜 Cost-Profit Calculator",
            "📚 Agronomy Library",
            "🌐 Localization Settings",
            "👤 Operator Profile"
        ]
    )

    # ================= EXECUTIVE DASHBOARD =================
    if menu == "🏠 Executive Dashboard":
        st.title("🏠 Executive Command Center")
        st.markdown("Real-time telemetry and agricultural indicators across your operational domain.")
        st.write("")

        # Custom Premium Metric Cards Layout
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            st.markdown("<div class='metric-card'><h5>👨‍🌾 Active Grid Ecosystem</h5><h2>12,500+</h2><span style='color:green;'>↑ 4.2% MoM</span></div>", unsafe_html=True)
        with c2:
            st.markdown(f"<div class='metric-card'><h5>📑 Ledgered Land Plots</h5><h2>{len(st.session_state.lands)} Plots</h2><span>Verified State Records</span></div>", unsafe_html=True)
        with c3:
            st.markdown("<div class='metric-card'><h5>📈 Machine Inference</h5><h2>96.4%</h2><span style='color:green;'>Model Optimized</span></div>", unsafe_html=True)
        with c4:
            st.markdown("<div class='metric-card'><h5>🌦 Active System Alerts</h5><h2>3 Alerts</h2><span style='color:red;'>Action Required</span></div>", unsafe_html=True)

        # Main Layout Columns
        col_left, col_right = st.columns([2, 1])
        with col_left:
            st.subheader("📊 Spatial Land Yield Distribution Forecast")
            if st.session_state.lands:
                df = pd.DataFrame(st.session_state.lands)
                st.bar_chart(df.set_index("Village")["Area"])
            else:
                st.info("No land assets registered yet. Navigate to Land Ledger Records to add fields.")
        
        with col_right:
            st.subheader("🔔 Critical Advisories")
            st.warning("**Weather Alert:** Unseasonal downpour detected via satellite paths near Southern Hub.")
            st.info("**Subsidy Window:** KUSUM Solar infrastructure window closing in 4 days.")

    # ================= NEW FEATURE: SATELLITE CROP MONITOR =================
    elif menu == "🛰️ Satellite Crop Monitor":
        st.title("🛰️ Satellite Remote Sensing Analytics (Simulated NDVI)")
        st.markdown("Visualizing Normalized Difference Vegetation Index trends to identify field stress anomalies early.")
        
        if not st.session_state.lands:
            st.warning("Please register a land plot first to initiate remote sensing mapping.")
        else:
            lands_df = pd.DataFrame(st.session_state.lands)
            selected_plot = st.selectbox("Select Plot Area Grid Location", lands_df["Survey No"])
            
            st.markdown("### NDVI Crop Health Timeline (Current Season)")
            # Generate dummy telemetry waveform
            chart_data = pd.DataFrame(
                np.random.uniform(0.4, 0.85, size=(20, 1)),
                columns=['NDVI Biomass Index']
            )
            st.line_chart(chart_data)
            
            st.markdown("""
                * **0.0 - 0.2:** Bare Soil / Rock
                * **0.2 - 0.5:** Sparse / Stressed Vegetation (Requires immediate water/nutrient boost)
                * **0.5 - 1.0:** Highly Dense, Healthy Crop Canopy 🌱
            """)

    # ================= NEW FEATURE: AI PEST DIAGNOSTIC =================
    elif menu == "🪲 AI Pest Diagnostic":
        st.title("🪲 AI Phytosanitary Pest & Disease Diagnostic Suite")
        st.markdown("Identify vector infestations and plant pathogen symptoms systematically.")
        
        st.markdown("### Step 1: Select Visual Symptom Profile")
        symptom_leaf = st.checkbox("Leaf Anomalies (Yellowing, necrotic spotting, white powder)")
        symptom_stem = st.checkbox("Stem Structural Degradation (Wilting, tunneling, boring signs)")
        symptom_root = st.checkbox("Root/Stunting issues (Galls, immediate unexplained wilting)")

        if st.button("Run Diagnostic Scan Pipeline"):
            with st.spinner("Analyzing plant pathology vectors..."):
                time.sleep(0.8)
                if symptom_leaf and not symptom_stem:
                    st.error("💥 Potential Diagnosis: **Powdery Mildew / Fungal Rust**")
                    st.info("💡 **Organic Rx:** 0.5% Neem Oil foliar application.\n\n🔬 **Chemical Alternative:** Apply Propiconazole 25% EC according to safety rules.")
                elif symptom_stem:
                    st.error("💥 Potential Diagnosis: **Stem Borer Larvae / Fall Armyworm**")
                    st.info("💡 **Biological Rx:** Introduce *Trichogramma* wasp parasitoids.\n\n🔬 **Chemical Alternative:** Chlorantraniliprole 18.5% SC application.")
                else:
                    st.success("✅ Pathogen profile safe. Maintain routine prophylactic spray scheduling.")

    # ================= NEW FEATURE: PRECISION IRRIGATION =================
    elif menu == "💧 Precision Irrigation":
        st.title("💧 Smart Hydro-Scheduling Matrix")
        st.markdown("Avoid root-rot and unnecessary pumping utility overhead costs.")
        
        c1, c2 = st.columns(2)
        with c1:
            crop_type = st.selectbox("Active Field Crop Type", ["Paddy/Rice", "Cotton", "Sugarcane", "Millets/Ragi"])
            stage = st.selectbox("Growth Stage Phase", ["Initial Seedling", "Vegetative Development", "Flowering / Grain Fill", "Harvest Ripening"])
        with c2:
            ambient_temp = st.slider("Current Regional Temperature (°C)", 15, 48, 30)
            soil_moist = st.slider("Current Soil Moisture Sensor Value (%)", 0, 100, 35)

        if st.button("Compute Precise Volumetric Irrigation Load"):
            # Mock agronomic equation output
            base_water = {"Paddy/Rice": 45, "Cotton": 20, "Sugarcane": 60, "Millets/Ragi": 10}
            calc_need = max(0, (base_water[crop_type] + (ambient_temp * 0.5)) - soil_moist)
            
            st.metric("Required Direct Irrigation Depth", f"{round(calc_need, 1)} mm / Hectare")
            if calc_need > 20:
                st.warning("⚠️ High Evapotranspiration deficit. Initiate drip irrigation run sequence immediately.")
            else:
                st.success("✅ Moisture profile acceptable. Postpone next water cycle by 24 hours.")

    # ================= SMART CROP ADVISORY =================
    elif menu == "🌾 Smart Crop Advisory":
        st.title("🌾 AI Crop Suite Advisor")
        soil = st.selectbox("Select Soil Type Profile", ["Black Cotton Soil", "Red Sandy Loam", "Alluvial River Basin"])

        if st.button("Recommend Crops"):
            if "Black" in soil:
                st.success("🔥 High Yield Potential: Cotton, Jowar, Soybeans")
            elif "Red" in soil:
                st.success("🔥 High Yield Potential: Groundnut, Ragi, Horsegram")
            else:
                st.success("🔥 High Yield Potential: Paddy, Sugarcane, Wheat")

    # ================= WEATHER =================
    elif menu == "🌦 Weather Forecast":
        st.title("🌦 Weather Forecast")
        city = st.text_input("Enter City Target", "Bangalore")

        if st.button("Fetch Forecast Data"):
            st.info(f"Displaying localized micro-climate array metrics for {city}")
            w_c1, w_c2, w_c3 = st.columns(3)
            w_c1.metric("Atmospheric Temperature", "30°C")
            w_c2.metric("Relative Humidity", "65%")
            w_c3.metric("Sky Condition", "Clear Sunny Space")

    # ================= MARKET PRICES =================
    elif menu == "📈 Live Market Prices":
        st.title("📈 MSP Market Price Matrices")
        df = pd.DataFrame({
            "Crop Asset": ["Cotton", "Jowar", "Paddy", "Ragi"],
            "Price (₹ per Quintal)": [7600, 3200, 2400, 4500]
        })
        st.dataframe(df, use_container_width=True)
        st.bar_chart(df.set_index("Crop Asset"))

    # ================= SOIL HEALTH =================
    elif menu == "🌱 Soil Health Matrix":
        st.title("🌱 Soil Chemical & Structural Profile")
        ph = st.slider("pH Spectrum Scale", 1.0, 14.0, 7.0, step=0.1)
        moisture = st.slider("Moisture Saturation %", 0, 100, 50)

        if st.button("Verify Soil Balance"):
            if 6.0 <= ph <= 7.5:
                st.success(f"Optimal Biological Availability Range (pH: {ph})")
            else:
                st.warning(f"pH Imbalance detected ({ph}). Lime treatment or Sulfur additive correction required.")

    # ================= LAND RECORDS =================
    elif menu == "📑 Land Ledger Records":
        st.title("📑 Sovereign Land Registry Ledger")
        
        c1, c2 = st.columns(2)
        with c1:
            survey = st.text_input("Survey Index / Plot Number")
            owner = st.text_input("Registered Landholder Name")
        with c2:
            area = st.number_input("Area Scale (Acres)", min_value=0.0, step=0.1)
            village = st.text_input("Village Jurisdiction")

        if st.button("Commit Record to Session Ledger"):
            if survey and owner and village and area > 0:
                st.session_state.lands.append({
                    "Survey No": survey, "Owner": owner, "Area": area, "Village": village
                })
                st.success("Record permanently committed to local session ledger!")
            else:
                st.error("Required fields missing data configurations.")

        if st.session_state.lands:
            st.write("### Registered Cadastral Registry Plots")
            st.dataframe(pd.DataFrame(st.session_state.lands), use_container_width=True)

    # ================= ANALYTICS & REPORTS =================
    elif menu == "📊 Analytics & Reports":
        st.title("📊 Compiled Agro-Business Reports")

        if not st.session_state.lands:
            st.warning("No data found in local state ledger to evaluate reports.")
        else:
            df = pd.DataFrame(st.session_state.lands)
            st.dataframe(df, use_container_width=True)

            # Native, zero-dependency data print capability
            csv_data = df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="⬇️ Export Raw Data Asset (.CSV)",
                data=csv_data,
                file_name="Dhara_Sampada_Master_Report.csv",
                mime="text/csv"
            )
            
            st.markdown("---")
            st.subheader("🖨️ Web & PDF Physical Hardcopy Output")
            st.info("💡 **UX Printing Tip:** Use the button below to prompt your OS printing window. Set your destination option to **'Save as PDF'** to instantly cache a clean digital document without complex server packages.")
            if st.button("🖨️ Open Native OS Print & PDF Dialog Launcher"):
                st.components.v1.html("<script>window.print();</script>", height=0, width=0)

    # ================= NOTIFICATIONS =================
    elif menu == "🔔 Advisory Bulletins":
        st.title("🔔 Centralized Broadcast Array")
        st.success("🌧️ Weather Bulletin: High probability rain event inbound over Southern Hub sectors.")
        st.info("💰 Banking Bulletin: Central DB Direct Benefit Funds released to micro-accounts.")

    # ================= GOV SCHEMES =================
    elif menu == "🏛 Gov Schemes Hub":
        st.title("🏛 Direct Sovereign Welfare Schemes Portal")
        st.info("**PM-KISAN Core Framework:** Direct ₹6000 income transfer mechanism.")
        st.info("**PM-KUSUM Infrastructure Initiative:** 60%+ direct financial help for off-grid clean solar irrigation arrays.")

    # ================= MARKETPLACE =================
    elif menu == "🛒 Farmer Marketplace":
        st.title("🛒 Decentralized Agri-Trade Marketplace")
        farmer = st.text_input("Farmer/Seller Profile Name")
        product = st.text_input("Produce Category (e.g. Basmati Rice)")
        quantity = st.number_input("Quantity Volumetric Scale (Quintals)", min_value=1)

        if st.button("Broadcast Listing to Market"):
            if farmer and product:
                st.success(f"Offer Successfully Listed: {quantity} Quintal(s) of '{product}' posted to current wholesale bids.")

    # ================= COST-PROFIT CALCULATOR =================
    elif menu == "🚜 Cost-Profit Calculator":
        st.title("🚜 Operational Farm Ledger & ROI Projections")
        seed = st.number_input("Input Seed Capital Cost (₹)", min_value=0)
        fert = st.number_input("Nutrients & Biological Crop Inputs Cost (₹)", min_value=0)
        labor = st.number_input("Mechanical & Labor Hire Payroll Cost (₹)", min_value=0)
        income = st.number_input("Target Expected Harvest Gross Income (₹)", min_value=0)

        if st.button("Process Fiscal Bottom-Line Balance"):
            expense = seed + fert + labor
            profit = income - expense
            st.metric("Total Operating Expenditure (OpEx)", f"₹{expense}")
            if profit >= 0:
                st.metric("Projected Operational Surplus (Net Profit)", f"₹{profit}")
            else:
                st.metric("Projected Financial Deficit (Net Loss)", f"₹{abs(profit)}", delta="- Net Loss")

    # ================= AGRONOMY LIBRARY =================
    elif menu == "📚 Agronomy Library":
        st.title("📚 Professional Agronomy Best Practices")
        st.markdown("""
        * **💧 Precision Drip Architecture:** Reduces localized weed vector creation and yields water conservation optimization by up to 45%.
        * **🔄 Dynamic Crop Intercropping:** Always couple legumes with deep-root crop matrices to keep topsoil nitrogen reserves high.
        """)

    # ================= LOCALIZATION =================
    elif menu == "🌐 Localization Settings":
        st.title("🌐 Localization & Linguistic Engines")
        lang = st.selectbox("Set Core UI Interface Language", ["English", "Kannada", "Hindi"])
        if lang == "Kannada":
            st.success("ಧಾರಾ ಸಂಪದಕ್ಕೆ ಸ್ವಾಗತ — ಉತ್ತಮ ಕೃಷಿ ನಿರ್ವಹಣೆ ವ್ಯವಸ್ಥೆ.")
        elif lang == "Hindi":
            st.success("धारा संपदा में आपका स्वागत है — उन्नत कृषि प्रबंधन मंच।")
        else:
            st.success("Core UI updated to default system English matrices.")

    # ================= PROFILE =================
    elif menu == "👤 Operator Profile":
        st.title("👤 System Operator Identity Configuration")
        st.text("Operator Status: Verified Agronomist Network Terminal")
        st.text("Platform Tier   : Enterprise Core Framework Access")

# ================= CORE APP CONTROLLER =================

if st.session_state.logged_in:
    main_app()
else:
    auth_page()
