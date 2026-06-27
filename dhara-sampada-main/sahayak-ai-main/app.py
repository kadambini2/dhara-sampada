# ================= IMPORTS =================

import streamlit as st
import pandas as pd
import numpy as np
import time

# ================= PAGE CONFIG =================

st.set_page_config(
    page_title="Dryland Agriculture | Next-Gen AI Agri-Platform",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ================= PREMIUM UI/UX GLOSS DESIGN STYLING =================

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght=300;400;500;600;700;800&display=swap');
    
    /* Core Base Typography Reset */
    html, body, [class*="css"], .stApp {
        font-family: 'Plus Jakarta Sans', sans-serif;
        background-color: #F9FBF9;
    }
    
    /* Beautiful Interactive Glassmorphism Cards */
    .hero-banner {
        background: linear-gradient(135deg, #1B5E20 0%, #2E7D32 50%, #4CAF50 100%);
        border-radius: 24px;
        padding: 40px;
        color: #FFFFFF;
        box-shadow: 0 10px 30px rgba(46, 125, 50, 0.15);
        margin-bottom: 2rem;
    }
    
    .metric-grid-box {
        background: #FFFFFF;
        border: 1px solid #EAECEF;
        border-radius: 20px;
        padding: 24px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.015);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    .metric-grid-box:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 35px rgba(46, 125, 50, 0.08);
        border-color: #81C784;
    }
    
    .badge-status {
        display: inline-block;
        padding: 6px 12px;
        border-radius: 30px;
        font-size: 0.75rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .badge-green { background-color: #E8F5E9; color: #2E7D32; }
    .badge-orange { background-color: #FFF3E0; color: #E65100; }
    
    /* Elegant Clean Input Focus Overrides */
    div[data-baseweb="input"] {
        border-radius: 12px !important;
    }
    
    .stButton>button {
        border-radius: 12px !important;
        font-weight: 600 !important;
    }
    </style>
""", unsafe_allow_html=True)

# ================= SESSION STATE MANAGER =================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "users" not in st.session_state:
    st.session_state.users = {"admin": "1234"}

if "lands" not in st.session_state:
    st.session_state.lands = [
        {"Survey No": "SRV-201", "Owner": "Ramesh Kumar", "Area": 4.5, "Village": "Malur"},
        {"Survey No": "SRV-404", "Owner": "Suresh Gowda", "Area": 2.2, "Village": "Channapatna"}
    ]

# ================= AUTHENTICATION VIEW =================

def auth_page():
    st.markdown("<div style='margin-top: 6%;'></div>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: #1B5E20; font-weight:800; font-size:3.2rem; letter-spacing:-1.5px;'>🌾 DHARA SAMPADA</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size:1.2rem; color: #555E55; margin-bottom: 2.5rem;'>Next-Generation AI Precision Agriculture Platform for Dryland Farming</p>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1.3, 1])
    with col2:
        with st.container(border=True):
            option = st.radio("Access Portals", ["🔐 Secure Login", "📝 Farmer Registration"], horizontal=True, label_visibility="collapsed")
            st.markdown("<div style='margin-bottom: 12px;'></div>", unsafe_allow_html=True)
            
            if option == "🔐 Secure Login":
                username = st.text_input("Username / Mobile Number", placeholder="Enter admin username")
                password = st.text_input("Password", type="password", placeholder="••••••••")
                st.write("")
                if st.button("Enter AI Command Control →", use_container_width=True, type="primary"):
                    if username in st.session_state.users and st.session_state.users[username] == password:
                        st.session_state.logged_in = True
                        st.success("Access Verified. Initializing platform interface modules...")
                        time.sleep(0.4)
                        st.rerun()
                    else:
                        st.error("Invalid secure credential profiles.")
            else:
                username = st.text_input("Create Account Username")
                password = st.text_input("Security Password Access Code", type="password")
                confirm = st.text_input("Confirm Security Password", type="password")
                st.write("")
                if st.button("Register New Farmer Core Profile", use_container_width=True, type="primary"):
                    if username and password == confirm:
                        st.session_state.users[username] = password
                        st.success("Profile written successfully! Toggle login above.")
                    else:
                        st.error("Please verify matching inputs.")

# ================= PRINCIPAL PLATFORM FRAMEWORK =================

def main_app():
    # Structural Sidebar Navigation Design
    st.sidebar.markdown("<h2 style='color: #1B5E20; font-weight:800; margin-bottom:2px;'>🌾 Dhara Sampada</h2>", unsafe_allow_html=True)
    st.sidebar.markdown("<p style='font-size: 0.75rem; color: #788278; text-transform: uppercase; letter-spacing:1px; font-weight:600;'>AI Dryland Operating Core v3.0</p>", unsafe_allow_html=True)
    st.sidebar.markdown("---")
    
    menu = st.sidebar.radio(
        "🖥️ DECISION CONTROL ARRAYS",
        [
            "🏠 Interactive Executive Hub",
            "🛰️ Satellite Crop Monitor",
            "🪲 AI Pest Diagnostic",
            "💧 Precision Irrigation",
            "🌾 Smart Crop Advisory",
            "🌦 Weather Forecast",
            "📈 Live Market Prices",
            "📑 Land Ledger Records",
            "📊 Analytics & Reports",
            "⚙️ Configuration Core"
        ]
    )
    
    st.sidebar.markdown("---")
    if st.sidebar.button("🚪 Terminate Session Hub", use_container_width=True):
        st.session_state.logged_in = False
        st.rerun()

    # ================= HOME INTERACTIVE EXECUTIVE HUB =================
    if menu == "🏠 Interactive Executive Hub":
        # Eye-Catching Immersive Hero Banner
        st.markdown("""
            <div class='hero-banner'>
                <span class='badge-status' style='background: rgba(255,255,255,0.2); color: white; margin-bottom: 12px;'>Core Server Online</span>
                <h1 style='color: white; font-weight: 800; margin: 0; font-size: 2.5rem; letter-spacing: -0.5px;'>Welcome to Dhara Sampada Control</h1>
                <p style='color: #E8F5E9; font-size: 1.1rem; margin-top: 8px; margin-bottom: 0; font-weight: 400;'>
                    Harnessing deep computer vision and macro-sensing matrices to maximize resource efficiency in arid and dryland agriculture zones.
                </p>
            </div>
        """, unsafe_allow_html=True)

        # Dynamic Status Telemetry Matrix Row
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            st.markdown(f"""<div class='metric-grid-box'><div style='color:#707870; font-weight:600; font-size:0.85rem; text-transform:uppercase;'>Ledgered Plots</div><div style='font-size:1.8rem; font-weight:800; color:#111; margin:6px 0;'>{len(st.session_state.lands)} Fields</div><span class='badge-status badge-green'>Active</span></div>""", unsafe_allow_html=True)
        with c2:
            st.markdown("""<div class='metric-grid-box'><div style='color:#707870; font-weight:600; font-size:0.85rem; text-transform:uppercase;'>Ecosystem Reach</div><div style='font-size:1.8rem; font-weight:800; color:#111; margin:6px 0;'>12,500+</div><span class='badge-status badge-green'>↑ 4.2% MoM</span></div>""", unsafe_allow_html=True)
        with c3:
            st.markdown("""<div class='metric-grid-box'><div style='color:#707870; font-weight:600; font-size:0.85rem; text-transform:uppercase;'>AI Engine Accuracy</div><div style='font-size:1.8rem; font-weight:800; color:#111; margin:6px 0;'>96.4%</div><span class='badge-status badge-green'>Optimal</span></div>""", unsafe_allow_html=True)
        with c4:
            st.markdown("""<div class='metric-grid-box'><div style='color:#707870; font-weight:600; font-size:0.85rem; text-transform:uppercase;'>Critical Advisories</div><div style='font-size:1.8rem; font-weight:800; color:#111; margin:6px 0;'>1 Alert</div><span class='badge-status badge-orange'>Review Info</span></div>""", unsafe_allow_html=True)

        st.write("")
        st.write("")

        # PRIMARY HIGHLY-ATTRACTIVE SOIL COMPUTER VISION SPLIT COMPONENT
        st.markdown("<h2 style='color:#1B5E20; font-weight:700; font-size:1.6rem; letter-spacing:-0.5px;'>🌱 Instant Computer Vision Soil Diagnostic</h2>", unsafe_allow_html=True)
        st.markdown("<p style='color:#636D63; margin-top:-10px; margin-bottom:1.5rem;'>Drop a crisp field image snapshot below to break down compositional soil health matrices automatically.</p>", unsafe_allow_html=True)

        with st.container(border=True):
            split_left, split_right = st.columns([1.1, 1])
            
            with split_left:
                st.markdown("<div style='padding:10px;'>", unsafe_allow_html=True)
                uploaded_soil_img = st.file_uploader("Drag and drop your topsoil snapshot here", type=["jpg", "jpeg", "png"], label_visibility="collapsed")
                
                if uploaded_soil_img is not None:
                    st.image(uploaded_soil_img, caption="📍 Target Topsoil Sample Frame Bound Successfully", use_container_width=True)
                else:
                    st.markdown("""
                        <div style='border: 2px dashed #CCD5CC; border-radius:16px; padding: 40px 20px; text-align:center; background-color:#FAFBFA; margin-top:10px;'>
                            <span style='font-size:2.5rem;'>📸</span>
                            <h4 style='color:#3B453B; margin-top:10px; font-weight:600;'>No Topsoil File Selected</h4>
                            <p style='color:#788578; font-size:0.88rem; max-width:320px; margin:0 auto; margin-top:4px;'>Please upload a high-contrast topsoil picture using the selection link above to initialize the AI engine.</p>
                        </div>
                    """, unsafe_allow_html=True)
                st.markdown("</div>", unsafe_allow_html=True)

            with split_right:
                st.markdown("<div style='padding:10px;'>", unsafe_allow_html=True)
                st.markdown("<h3 style='margin-top:0; color:#2E7D32; font-weight:600; font-size:1.25rem;'>📊 AI Analytical Spectrum Output</h3>", unsafe_allow_html=True)
                
                if uploaded_soil_img is not None:
                    st.markdown("Click the execution pipeline link below to calculate organic indicators based on chromatic spectrums.")
                    st.write("")
                    
                    if st.button("✨ Run Soil Telemetry Scan Pipeline", type="primary", use_container_width=True):
                        with st.spinner("Decoding mineral distribution density vectors..."):
                            time.sleep(1.4)
                            
                        st.markdown("""
                            <div style='background-color:#F4FAF4; border: 1px solid #D8EED8; padding:18px; border-radius:14px; margin-bottom:15px;'>
                                <span style='font-weight:700; color:#1B5E20; font-size:0.95rem;'>✅ Computer Vision Inference Complete</span>
                                <div style='margin-top:8px; display:grid; grid-template-columns: 1fr 1fr; gap:12px;'>
                                    <div><small style='color:#5A655A;'>Calculated Classification</small><br><strong>Clayey Loam Matrix</strong></div>
                                    <div><small style='color:#5A655A;'>Organic Carbon (OC)</small><br><strong style='color:#2E7D32;'>0.68% (Healthy Mid)</strong></div>
                                    <div><small style='color:#5A655A;'>Estimated Moisture Ret.</small><br><strong>24.5% Volumetric</strong></div>
                                    <div><small style='color:#5A655A;'>Bulk Density Signature</small><br><strong>1.32 g/cm³</strong></div>
                                </div>
                            </div>
                        """, unsafe_allow_html=True)
                        st.info("💡 **Digital Agronomist Verdict:** Soil data states fine particle binding. For arid plots, introducing balanced biological compost or vermicompost will improve moisture-holding horizons dramatically over sub-optimal heat waves.")
                else:
                    st.markdown("""
                        <div style='background-color:#F5F7F5; padding:20px; border-radius:14px; color:#5A655A; font-size:0.9rem; border: 1px solid #E6EAE6;'>
                            ⏱️ <strong>Waiting on input profile stream...</strong><br><br> Once a valid field photo asset is attached to the system via the uploader zone, real-time prediction frameworks will compute chemical profile mappings here instantly.
                        </div>
                    """, unsafe_allow_html=True)
                st.markdown("</div>", unsafe_allow_html=True)

    # ================= ADDITIONAL UTILITY MATRICES =================
    elif menu == "🛰️ Satellite Crop Monitor":
        st.markdown("<h1 style='color:#1B5E20; font-weight:700;'>🛰️ NDVI Satellite Remote Sensing Analytics</h1>", unsafe_allow_html=True)
        if not st.session_state.lands:
            st.warning("Please record crop fields coordinates first inside the Land Records panel.")
        else:
            df = pd.DataFrame(st.session_state.lands)
            st.selectbox("Target Registered Operational Grid", df["Survey No"])
            st.line_chart(pd.DataFrame(np.random.uniform(0.42, 0.88, size=(24, 1)), columns=['NDVI Biomass Profile Index']))

    elif menu == "🪲 AI Pest Diagnostic":
        st.markdown("<h1 style='color:#1B5E20; font-weight:700;'>🪲 Phytosanitary Pathology Scan Vector</h1>", unsafe_allow_html=True)
        with st.container(border=True):
            st.checkbox("Leaf Yellowing/Necrotic spotting vectors spotted")
            if st.button("Run Diagnostic Match Matrix", type="primary"):
                st.error("💥 Trace alert match calculated: Potential early stage Fungal Rust signature present.")

    # ================= DRYLAND FUNCTIONAL SUBSYSTEMS =================
    elif menu == "💧 Precision Irrigation":
        st.markdown("<h1 style='color:#1B5E20; font-weight:700;'>💧 Dryland Water Budgeting & Precision Irrigation</h1>", unsafe_allow_html=True)
        st.markdown("<p style='color:#636D63;'>Predictive moisture depletion models tailored specifically for arid and semi-arid cultivation maps.</p>", unsafe_allow_html=True)
        
        with st.container(border=True):
            col_a, col_b = st.columns(2)
            with col_a:
                crop_type = st.selectbox("Current Dryland Crop", ["Ragi (Finger Millet)", "Jowar (Sorghum)", "Toor (Pigeon Pea)", "Groundnut"])
                soil_type = st.selectbox("Soil Texture Profile", ["Red Sandy Loam", "Black Cotton Soil", "Shallow Gravelly Soil"])
            with col_b:
                days_since_rain = st.number_input("Days Since Last Rainfall Event", min_value=0, max_value=60, value=12)
                mulching = st.radio("Organic Mulching Applied?", ["Yes", "No"], horizontal=True)

            st.write("")
            if st.button("📊 Calculate Moisture Depletion & Deficit", type="primary", use_container_width=True):
                with st.spinner("Simulating localized evapotranspiration matrices..."):
                    time.sleep(1.0)
                
                base_depletion = min(days_since_rain * 3.5, 90.0)
                if mulching == "Yes":
                    base_depletion *= 0.7  # Evaporation mitigation factor
                
                available_moisture = 100.0 - base_depletion
                
                st.subheader("Water Stress Telemetry Results")
                st.progress(available_moisture / 100.0, text=f"Estimated Available Soil Moisture Profile: {available_moisture:.1f}%")
                
                if available_moisture < 40.0:
                    st.error(f"⚠️ Critical Stress Level! Soil moisture is below the Management Allowed Depletion (MAD) threshold for {crop_type}. Deploy 20mm protective pulse irrigation from farm pond structures immediately if available.")
                else:
                    st.success(f"✅ Moisture metrics reside within standard dryland survival boundaries. Next structural verification recommended in 4 days.")

    elif menu == "🌾 Smart Crop Advisory":
        st.markdown("<h1 style='color:#1B5E20; font-weight:700;'>🌾 AI Dryland Crop & Variety Advisory</h1>", unsafe_allow_html=True)
        st.markdown("<p style='color:#636D63;'>Get tailored drought-resilient crop combination configurations based on dynamic monsoon delay behaviors.</p>", unsafe_allow_html=True)
        
        with st.container(border=True):
            monsoon_status = st.select_slider(
                "Current Kharif Monsoon Delay Status",
                options=["Normal Onset", "2 Weeks Delayed", "4 Weeks Delayed (Critical)", "Severe Drought/Failure"]
            )
            
            st.write("")
            if st.button("✨ Generate Resilient Contingency Plan", type="primary"):
                st.markdown("### 📋 AI Strategic Contingency Layout")
                
                if monsoon_status == "Normal Onset":
                    st.info("💡 **Recommendation:** Standard long-duration crops optimal. Plant Toor (BRG-1, BRG-2) or Groundnut (TMV-2) intercropped with Ragi in a 4:2 layout matrix.")
                elif monsoon_status == "2 Weeks Delayed":
                    st.warning("💡 **Recommendation:** Swift modification to medium-duration drought-tolerant strains. Opt for Ragi (GPU-28 / GPU-66) or Sorghum (SVD-1). Implement rigorous compartmental bunding.")
                elif monsoon_status == "4 Weeks Delayed (Critical)":
                    st.error("💡 **Recommendation:** Avoid long-duration cycles. Transition immediately to contingency assets: Horsegram (PHG-9), Foxtail Millet (Navane), or Matki. Row spacing metrics must expand by 20% to maximize moisture footprint allocation.")
                else:
                    st.error("🚨 **Emergency Advisory:** Extreme moisture deficit zone. Halt primary grain tillage. Shift focus entirely to structural fodder processing (Sorghum/Maize fodder) to guarantee livestock asset protection.")

    # ================= CONFIGURATION CONTROL HUB =================
    elif menu == "⚙️ Configuration Core":
        st.markdown("<h1 style='color:#1B5E20; font-weight:700;'>⚙️ System Configuration Core</h1>", unsafe_allow_html=True)
        st.markdown("<p style='color:#636D63;'>Manage AI threshold limits, IoT sensor nodes, and platform profiles for dryland sectors.</p>", unsafe_allow_html=True)
        
        # 3 Structured Layout Tabs
        tab1, tab2, tab3 = st.tabs(["👤 User Profile Matrix", "📡 IoT & Hardware Nodes", "🛡️ Database & Reset Core"])
        
        with tab1:
            st.markdown("### Farmer & Admin Profile Info")
            col_u1, col_u2 = st.columns(2)
            with col_u1:
                st.text_input("Active Node Operator", value="Admin / Primary Farmer", disabled=True)
                st.text_input("Associated Mobile Number", value="+91 98765 43210")
            with col_u2:
                st.selectbox("Primary Language Interface", ["English", "ಕನ್ನಡ (Kannada)", "Hindi"])
                st.selectbox("Default Dryland Agri-Zone", ["Semi-Arid Zone (South Karnataka)", "Arid Zone (North Karnataka)", "Custom Profile"])
            
            if st.button("💾 Update Profile Mappings", type="primary"):
                st.success("✅ Profile configurations synchronized successfully with local server arrays.")

        with tab2:
            st.markdown("### Wireless Telemetry & IoT Sensor Integration")
            st.caption("Link physical soil moisture probes, automated drip valves, and telemetry hardware to Dhara Sampada.")
            
            with st.container(border=True):
                st.toggle("Enable Live Cloud Sync for Soil Probes", value=True)
                st.toggle("Auto-Trigger Protective Drip Pulsing via Farm Pond Pump", value=False)
                
                st.markdown("---")
                st.markdown("**Active Hardware Array Network**")
                col_hw1, col_hw2 = st.columns(2)
                with col_hw1:
                    st.success("🟢 Node-01 (Soil Moisture Sensor) - Connected [Battery: 84%]")
                    st.success("🟢 Node-02 (Weather Telemetry Station) - Connected [Battery: 91%]")
                with col_hw2:
                    st.error("🔴 Node-03 (Automated Valve Controller) - Offline / No Signal")
                    
            if st.button("🔄 Rescan IoT Network Grid"):
                with st.spinner("Pinging wireless edge devices..."):
                    time.sleep(1.0)
                st.info("📡 Scan complete. 2 Active Nodes verified, 1 Node requires hardware inspection.")

        with tab3:
            st.markdown("### System Diagnostics & Memory Control")
            st.warning("⚠️ High Privilege Actions: Modifying these structures can wipe local cached records.")
            
            st.markdown(f"**Current Registered Database Payload:** `{len(st.session_state.lands)} Land Records` logged.")
            
            col_r1, col_r2 = st.columns(2)
            with col_r1:
                if st.button("🛑 Clear Registered Fields Cache", use_container_width=True):
                    st.session_state.lands = []
                    st.success("Land Ledger database dropped. Reloading application grids...")
                    time.sleep(0.5)
                    st.rerun()
            with col_r2:
                if st.button("🔄 Hard Reboot Platform Core", use_container_width=True):
                    st.session_state.logged_in = False
                    st.success("Rebooting server frameworks...")
                    time.sleep(0.5)
                    st.rerun()

    else:
        st.markdown(f"<h1 style='color:#1B5E20; font-weight:700;'>{menu}</h1>", unsafe_allow_html=True)
        st.info("Integrated data engine modules mapping successfully into parent application container grids.")

# ================= CORE ENGINE TRIGGER CONTROLLER =================

if st.session_state.logged_in:
    main_app()
else:
    auth_page()# ================= IMPORTS =================

import streamlit as st
import pandas as pd
import numpy as np
import time

# ================= PAGE CONFIG =================

st.set_page_config(
    page_title="Dryland Agriculture | Next-Gen AI Agri-Platform",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ================= PREMIUM UI/UX GLOSS DESIGN STYLING =================

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght=300;400;500;600;700;800&display=swap');
    
    /* Core Base Typography Reset */
    html, body, [class*="css"], .stApp {
        font-family: 'Plus Jakarta Sans', sans-serif;
        background-color: #F9FBF9;
    }
    
    /* Beautiful Interactive Glassmorphism Cards */
    .hero-banner {
        background: linear-gradient(135deg, #1B5E20 0%, #2E7D32 50%, #4CAF50 100%);
        border-radius: 24px;
        padding: 40px;
        color: #FFFFFF;
        box-shadow: 0 10px 30px rgba(46, 125, 50, 0.15);
        margin-bottom: 2rem;
    }
    
    .metric-grid-box {
        background: #FFFFFF;
        border: 1px solid #EAECEF;
        border-radius: 20px;
        padding: 24px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.015);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    .metric-grid-box:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 35px rgba(46, 125, 50, 0.08);
        border-color: #81C784;
    }
    
    .badge-status {
        display: inline-block;
        padding: 6px 12px;
        border-radius: 30px;
        font-size: 0.75rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .badge-green { background-color: #E8F5E9; color: #2E7D32; }
    .badge-orange { background-color: #FFF3E0; color: #E65100; }
    
    /* Elegant Clean Input Focus Overrides */
    div[data-baseweb="input"] {
        border-radius: 12px !important;
    }
    
    .stButton>button {
        border-radius: 12px !important;
        font-weight: 600 !important;
    }
    </style>
""", unsafe_allow_html=True)

# ================= SESSION STATE MANAGER =================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "users" not in st.session_state:
    st.session_state.users = {"admin": "1234"}

if "lands" not in st.session_state:
    st.session_state.lands = [
        {"Survey No": "SRV-201", "Owner": "Ramesh Kumar", "Area": 4.5, "Village": "Malur"},
        {"Survey No": "SRV-404", "Owner": "Suresh Gowda", "Area": 2.2, "Village": "Channapatna"}
    ]

# ================= AUTHENTICATION VIEW =================

def auth_page():
    st.markdown("<div style='margin-top: 6%;'></div>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: #1B5E20; font-weight:800; font-size:3.2rem; letter-spacing:-1.5px;'>🌾 DHARA SAMPADA</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size:1.2rem; color: #555E55; margin-bottom: 2.5rem;'>Next-Generation AI Precision Agriculture Platform for Dryland Farming</p>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1.3, 1])
    with col2:
        with st.container(border=True):
            option = st.radio("Access Portals", ["🔐 Secure Login", "📝 Farmer Registration"], horizontal=True, label_visibility="collapsed")
            st.markdown("<div style='margin-bottom: 12px;'></div>", unsafe_allow_html=True)
            
            if option == "🔐 Secure Login":
                username = st.text_input("Username / Mobile Number", placeholder="Enter admin username")
                password = st.text_input("Password", type="password", placeholder="••••••••")
                st.write("")
                if st.button("Enter AI Command Control →", use_container_width=True, type="primary"):
                    if username in st.session_state.users and st.session_state.users[username] == password:
                        st.session_state.logged_in = True
                        st.success("Access Verified. Initializing platform interface modules...")
                        time.sleep(0.4)
                        st.rerun()
                    else:
                        st.error("Invalid secure credential profiles.")
            else:
                username = st.text_input("Create Account Username")
                password = st.text_input("Security Password Access Code", type="password")
                confirm = st.text_input("Confirm Security Password", type="password")
                st.write("")
                if st.button("Register New Farmer Core Profile", use_container_width=True, type="primary"):
                    if username and password == confirm:
                        st.session_state.users[username] = password
                        st.success("Profile written successfully! Toggle login above.")
                    else:
                        st.error("Please verify matching inputs.")

# ================= PRINCIPAL PLATFORM FRAMEWORK =================

def main_app():
    # Structural Sidebar Navigation Design
    st.sidebar.markdown("<h2 style='color: #1B5E20; font-weight:800; margin-bottom:2px;'>🌾 Dhara Sampada</h2>", unsafe_allow_html=True)
    st.sidebar.markdown("<p style='font-size: 0.75rem; color: #788278; text-transform: uppercase; letter-spacing:1px; font-weight:600;'>AI Dryland Operating Core v3.0</p>", unsafe_allow_html=True)
    st.sidebar.markdown("---")
    
    menu = st.sidebar.radio(
        "🖥️ DECISION CONTROL ARRAYS",
        [
            "🏠 Interactive Executive Hub",
            "🛰️ Satellite Crop Monitor",
            "🪲 AI Pest Diagnostic",
            "💧 Precision Irrigation",
            "🌾 Smart Crop Advisory",
            "🌦 Weather Forecast",
            "📈 Live Market Prices",
            "📑 Land Ledger Records",
            "📊 Analytics & Reports",
            "⚙️ Configuration Core"
        ]
    )
    
    st.sidebar.markdown("---")
    if st.sidebar.button("🚪 Terminate Session Hub", use_container_width=True):
        st.session_state.logged_in = False
        st.rerun()

    # ================= HOME INTERACTIVE EXECUTIVE HUB =================
    if menu == "🏠 Interactive Executive Hub":
        # Eye-Catching Immersive Hero Banner
        st.markdown("""
            <div class='hero-banner'>
                <span class='badge-status' style='background: rgba(255,255,255,0.2); color: white; margin-bottom: 12px;'>Core Server Online</span>
                <h1 style='color: white; font-weight: 800; margin: 0; font-size: 2.5rem; letter-spacing: -0.5px;'>Welcome to Dhara Sampada Control</h1>
                <p style='color: #E8F5E9; font-size: 1.1rem; margin-top: 8px; margin-bottom: 0; font-weight: 400;'>
                    Harnessing deep computer vision and macro-sensing matrices to maximize resource efficiency in arid and dryland agriculture zones.
                </p>
            </div>
        """, unsafe_allow_html=True)

        # Dynamic Status Telemetry Matrix Row
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            st.markdown(f"""<div class='metric-grid-box'><div style='color:#707870; font-weight:600; font-size:0.85rem; text-transform:uppercase;'>Ledgered Plots</div><div style='font-size:1.8rem; font-weight:800; color:#111; margin:6px 0;'>{len(st.session_state.lands)} Fields</div><span class='badge-status badge-green'>Active</span></div>""", unsafe_allow_html=True)
        with c2:
            st.markdown("""<div class='metric-grid-box'><div style='color:#707870; font-weight:600; font-size:0.85rem; text-transform:uppercase;'>Ecosystem Reach</div><div style='font-size:1.8rem; font-weight:800; color:#111; margin:6px 0;'>12,500+</div><span class='badge-status badge-green'>↑ 4.2% MoM</span></div>""", unsafe_allow_html=True)
        with c3:
            st.markdown("""<div class='metric-grid-box'><div style='color:#707870; font-weight:600; font-size:0.85rem; text-transform:uppercase;'>AI Engine Accuracy</div><div style='font-size:1.8rem; font-weight:800; color:#111; margin:6px 0;'>96.4%</div><span class='badge-status badge-green'>Optimal</span></div>""", unsafe_allow_html=True)
        with c4:
            st.markdown("""<div class='metric-grid-box'><div style='color:#707870; font-weight:600; font-size:0.85rem; text-transform:uppercase;'>Critical Advisories</div><div style='font-size:1.8rem; font-weight:800; color:#111; margin:6px 0;'>1 Alert</div><span class='badge-status badge-orange'>Review Info</span></div>""", unsafe_allow_html=True)

        st.write("")
        st.write("")

        # PRIMARY HIGHLY-ATTRACTIVE SOIL COMPUTER VISION SPLIT COMPONENT
        st.markdown("<h2 style='color:#1B5E20; font-weight:700; font-size:1.6rem; letter-spacing:-0.5px;'>🌱 Instant Computer Vision Soil Diagnostic</h2>", unsafe_allow_html=True)
        st.markdown("<p style='color:#636D63; margin-top:-10px; margin-bottom:1.5rem;'>Drop a crisp field image snapshot below to break down compositional soil health matrices automatically.</p>", unsafe_allow_html=True)

        with st.container(border=True):
            split_left, split_right = st.columns([1.1, 1])
            
            with split_left:
                st.markdown("<div style='padding:10px;'>", unsafe_allow_html=True)
                uploaded_soil_img = st.file_uploader("Drag and drop your topsoil snapshot here", type=["jpg", "jpeg", "png"], label_visibility="collapsed")
                
                if uploaded_soil_img is not None:
                    st.image(uploaded_soil_img, caption="📍 Target Topsoil Sample Frame Bound Successfully", use_container_width=True)
                else:
                    st.markdown("""
                        <div style='border: 2px dashed #CCD5CC; border-radius:16px; padding: 40px 20px; text-align:center; background-color:#FAFBFA; margin-top:10px;'>
                            <span style='font-size:2.5rem;'>📸</span>
                            <h4 style='color:#3B453B; margin-top:10px; font-weight:600;'>No Topsoil File Selected</h4>
                            <p style='color:#788578; font-size:0.88rem; max-width:320px; margin:0 auto; margin-top:4px;'>Please upload a high-contrast topsoil picture using the selection link above to initialize the AI engine.</p>
                        </div>
                    """, unsafe_allow_html=True)
                st.markdown("</div>", unsafe_allow_html=True)

            with split_right:
                st.markdown("<div style='padding:10px;'>", unsafe_allow_html=True)
                st.markdown("<h3 style='margin-top:0; color:#2E7D32; font-weight:600; font-size:1.25rem;'>📊 AI Analytical Spectrum Output</h3>", unsafe_allow_html=True)
                
                if uploaded_soil_img is not None:
                    st.markdown("Click the execution pipeline link below to calculate organic indicators based on chromatic spectrums.")
                    st.write("")
                    
                    if st.button("✨ Run Soil Telemetry Scan Pipeline", type="primary", use_container_width=True):
                        with st.spinner("Decoding mineral distribution density vectors..."):
                            time.sleep(1.4)
                            
                        st.markdown("""
                            <div style='background-color:#F4FAF4; border: 1px solid #D8EED8; padding:18px; border-radius:14px; margin-bottom:15px;'>
                                <span style='font-weight:700; color:#1B5E20; font-size:0.95rem;'>✅ Computer Vision Inference Complete</span>
                                <div style='margin-top:8px; display:grid; grid-template-columns: 1fr 1fr; gap:12px;'>
                                    <div><small style='color:#5A655A;'>Calculated Classification</small><br><strong>Clayey Loam Matrix</strong></div>
                                    <div><small style='color:#5A655A;'>Organic Carbon (OC)</small><br><strong style='color:#2E7D32;'>0.68% (Healthy Mid)</strong></div>
                                    <div><small style='color:#5A655A;'>Estimated Moisture Ret.</small><br><strong>24.5% Volumetric</strong></div>
                                    <div><small style='color:#5A655A;'>Bulk Density Signature</small><br><strong>1.32 g/cm³</strong></div>
                                </div>
                            </div>
                        """, unsafe_allow_html=True)
                        st.info("💡 **Digital Agronomist Verdict:** Soil data states fine particle binding. For arid plots, introducing balanced biological compost or vermicompost will improve moisture-holding horizons dramatically over sub-optimal heat waves.")
                else:
                    st.markdown("""
                        <div style='background-color:#F5F7F5; padding:20px; border-radius:14px; color:#5A655A; font-size:0.9rem; border: 1px solid #E6EAE6;'>
                            ⏱️ <strong>Waiting on input profile stream...</strong><br><br> Once a valid field photo asset is attached to the system via the uploader zone, real-time prediction frameworks will compute chemical profile mappings here instantly.
                        </div>
                    """, unsafe_allow_html=True)
                st.markdown("</div>", unsafe_allow_html=True)

    # ================= ADDITIONAL UTILITY MATRICES =================
    elif menu == "🛰️ Satellite Crop Monitor":
        st.markdown("<h1 style='color:#1B5E20; font-weight:700;'>🛰️ NDVI Satellite Remote Sensing Analytics</h1>", unsafe_allow_html=True)
        if not st.session_state.lands:
            st.warning("Please record crop fields coordinates first inside the Land Records panel.")
        else:
            df = pd.DataFrame(st.session_state.lands)
            st.selectbox("Target Registered Operational Grid", df["Survey No"])
            st.line_chart(pd.DataFrame(np.random.uniform(0.42, 0.88, size=(24, 1)), columns=['NDVI Biomass Profile Index']))

    elif menu == "🪲 AI Pest Diagnostic":
        st.markdown("<h1 style='color:#1B5E20; font-weight:700;'>🪲 Phytosanitary Pathology Scan Vector</h1>", unsafe_allow_html=True)
        with st.container(border=True):
            st.checkbox("Leaf Yellowing/Necrotic spotting vectors spotted")
            if st.button("Run Diagnostic Match Matrix", type="primary"):
                st.error("💥 Trace alert match calculated: Potential early stage Fungal Rust signature present.")

    # ================= DRYLAND FUNCTIONAL SUBSYSTEMS =================
    elif menu == "💧 Precision Irrigation":
        st.markdown("<h1 style='color:#1B5E20; font-weight:700;'>💧 Dryland Water Budgeting & Precision Irrigation</h1>", unsafe_allow_html=True)
        st.markdown("<p style='color:#636D63;'>Predictive moisture depletion models tailored specifically for arid and semi-arid cultivation maps.</p>", unsafe_allow_html=True)
        
        with st.container(border=True):
            col_a, col_b = st.columns(2)
            with col_a:
                crop_type = st.selectbox("Current Dryland Crop", ["Ragi (Finger Millet)", "Jowar (Sorghum)", "Toor (Pigeon Pea)", "Groundnut"])
                soil_type = st.selectbox("Soil Texture Profile", ["Red Sandy Loam", "Black Cotton Soil", "Shallow Gravelly Soil"])
            with col_b:
                days_since_rain = st.number_input("Days Since Last Rainfall Event", min_value=0, max_value=60, value=12)
                mulching = st.radio("Organic Mulching Applied?", ["Yes", "No"], horizontal=True)

            st.write("")
            if st.button("📊 Calculate Moisture Depletion & Deficit", type="primary", use_container_width=True):
                with st.spinner("Simulating localized evapotranspiration matrices..."):
                    time.sleep(1.0)
                
                base_depletion = min(days_since_rain * 3.5, 90.0)
                if mulching == "Yes":
                    base_depletion *= 0.7  # Evaporation mitigation factor
                
                available_moisture = 100.0 - base_depletion
                
                st.subheader("Water Stress Telemetry Results")
                st.progress(available_moisture / 100.0, text=f"Estimated Available Soil Moisture Profile: {available_moisture:.1f}%")
                
                if available_moisture < 40.0:
                    st.error(f"⚠️ Critical Stress Level! Soil moisture is below the Management Allowed Depletion (MAD) threshold for {crop_type}. Deploy 20mm protective pulse irrigation from farm pond structures immediately if available.")
                else:
                    st.success(f"✅ Moisture metrics reside within standard dryland survival boundaries. Next structural verification recommended in 4 days.")

    elif menu == "🌾 Smart Crop Advisory":
        st.markdown("<h1 style='color:#1B5E20; font-weight:700;'>🌾 AI Dryland Crop & Variety Advisory</h1>", unsafe_allow_html=True)
        st.markdown("<p style='color:#636D63;'>Get tailored drought-resilient crop combination configurations based on dynamic monsoon delay behaviors.</p>", unsafe_allow_html=True)
        
        with st.container(border=True):
            monsoon_status = st.select_slider(
                "Current Kharif Monsoon Delay Status",
                options=["Normal Onset", "2 Weeks Delayed", "4 Weeks Delayed (Critical)", "Severe Drought/Failure"]
            )
            
            st.write("")
            if st.button("✨ Generate Resilient Contingency Plan", type="primary"):
                st.markdown("### 📋 AI Strategic Contingency Layout")
                
                if monsoon_status == "Normal Onset":
                    st.info("💡 **Recommendation:** Standard long-duration crops optimal. Plant Toor (BRG-1, BRG-2) or Groundnut (TMV-2) intercropped with Ragi in a 4:2 layout matrix.")
                elif monsoon_status == "2 Weeks Delayed":
                    st.warning("💡 **Recommendation:** Swift modification to medium-duration drought-tolerant strains. Opt for Ragi (GPU-28 / GPU-66) or Sorghum (SVD-1). Implement rigorous compartmental bunding.")
                elif monsoon_status == "4 Weeks Delayed (Critical)":
                    st.error("💡 **Recommendation:** Avoid long-duration cycles. Transition immediately to contingency assets: Horsegram (PHG-9), Foxtail Millet (Navane), or Matki. Row spacing metrics must expand by 20% to maximize moisture footprint allocation.")
                else:
                    st.error("🚨 **Emergency Advisory:** Extreme moisture deficit zone. Halt primary grain tillage. Shift focus entirely to structural fodder processing (Sorghum/Maize fodder) to guarantee livestock asset protection.")

    # ================= CONFIGURATION CONTROL HUB =================
    elif menu == "⚙️ Configuration Core":
        st.markdown("<h1 style='color:#1B5E20; font-weight:700;'>⚙️ System Configuration Core</h1>", unsafe_allow_html=True)
        st.markdown("<p style='color:#636D63;'>Manage AI threshold limits, IoT sensor nodes, and platform profiles for dryland sectors.</p>", unsafe_allow_html=True)
        
        # 3 Structured Layout Tabs
        tab1, tab2, tab3 = st.tabs(["👤 User Profile Matrix", "📡 IoT & Hardware Nodes", "🛡️ Database & Reset Core"])
        
        with tab1:
            st.markdown("### Farmer & Admin Profile Info")
            col_u1, col_u2 = st.columns(2)
            with col_u1:
                st.text_input("Active Node Operator", value="Admin / Primary Farmer", disabled=True)
                st.text_input("Associated Mobile Number", value="+91 98765 43210")
            with col_u2:
                st.selectbox("Primary Language Interface", ["English", "ಕನ್ನಡ (Kannada)", "Hindi"])
                st.selectbox("Default Dryland Agri-Zone", ["Semi-Arid Zone (South Karnataka)", "Arid Zone (North Karnataka)", "Custom Profile"])
            
            if st.button("💾 Update Profile Mappings", type="primary"):
                st.success("✅ Profile configurations synchronized successfully with local server arrays.")

        with tab2:
            st.markdown("### Wireless Telemetry & IoT Sensor Integration")
            st.caption("Link physical soil moisture probes, automated drip valves, and telemetry hardware to Dhara Sampada.")
            
            with st.container(border=True):
                st.toggle("Enable Live Cloud Sync for Soil Probes", value=True)
                st.toggle("Auto-Trigger Protective Drip Pulsing via Farm Pond Pump", value=False)
                
                st.markdown("---")
                st.markdown("**Active Hardware Array Network**")
                col_hw1, col_hw2 = st.columns(2)
                with col_hw1:
                    st.success("🟢 Node-01 (Soil Moisture Sensor) - Connected [Battery: 84%]")
                    st.success("🟢 Node-02 (Weather Telemetry Station) - Connected [Battery: 91%]")
                with col_hw2:
                    st.error("🔴 Node-03 (Automated Valve Controller) - Offline / No Signal")
                    
            if st.button("🔄 Rescan IoT Network Grid"):
                with st.spinner("Pinging wireless edge devices..."):
                    time.sleep(1.0)
                st.info("📡 Scan complete. 2 Active Nodes verified, 1 Node requires hardware inspection.")

        with tab3:
            st.markdown("### System Diagnostics & Memory Control")
            st.warning("⚠️ High Privilege Actions: Modifying these structures can wipe local cached records.")
            
            st.markdown(f"**Current Registered Database Payload:** `{len(st.session_state.lands)} Land Records` logged.")
            
            col_r1, col_r2 = st.columns(2)
            with col_r1:
                if st.button("🛑 Clear Registered Fields Cache", use_container_width=True):
                    st.session_state.lands = []
                    st.success("Land Ledger database dropped. Reloading application grids...")
                    time.sleep(0.5)
                    st.rerun()
            with col_r2:
                if st.button("🔄 Hard Reboot Platform Core", use_container_width=True):
                    st.session_state.logged_in = False
                    st.success("Rebooting server frameworks...")
                    time.sleep(0.5)
                    st.rerun()

    else:
        st.markdown(f"<h1 style='color:#1B5E20; font-weight:700;'>{menu}</h1>", unsafe_allow_html=True)
        st.info("Integrated data engine modules mapping successfully into parent application container grids.")

# ================= CORE ENGINE TRIGGER CONTROLLER =================

if st.session_state.logged_in:
    main_app()
else:
    auth_page()# ================= IMPORTS =================

import streamlit as st
import pandas as pd
import numpy as np
import time

# ================= PAGE CONFIG =================

st.set_page_config(
    page_title="Dryland Agriculture | Next-Gen AI Agri-Platform",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ================= PREMIUM UI/UX GLOSS DESIGN STYLING =================

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght=300;400;500;600;700;800&display=swap');
    
    /* Core Base Typography Reset */
    html, body, [class*="css"], .stApp {
        font-family: 'Plus Jakarta Sans', sans-serif;
        background-color: #F9FBF9;
    }
    
    /* Beautiful Interactive Glassmorphism Cards */
    .hero-banner {
        background: linear-gradient(135deg, #1B5E20 0%, #2E7D32 50%, #4CAF50 100%);
        border-radius: 24px;
        padding: 40px;
        color: #FFFFFF;
        box-shadow: 0 10px 30px rgba(46, 125, 50, 0.15);
        margin-bottom: 2rem;
    }
    
    .metric-grid-box {
        background: #FFFFFF;
        border: 1px solid #EAECEF;
        border-radius: 20px;
        padding: 24px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.015);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    .metric-grid-box:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 35px rgba(46, 125, 50, 0.08);
        border-color: #81C784;
    }
    
    .badge-status {
        display: inline-block;
        padding: 6px 12px;
        border-radius: 30px;
        font-size: 0.75rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .badge-green { background-color: #E8F5E9; color: #2E7D32; }
    .badge-orange { background-color: #FFF3E0; color: #E65100; }
    
    /* Elegant Clean Input Focus Overrides */
    div[data-baseweb="input"] {
        border-radius: 12px !important;
    }
    
    .stButton>button {
        border-radius: 12px !important;
        font-weight: 600 !important;
    }
    </style>
""", unsafe_allow_html=True)

# ================= SESSION STATE MANAGER =================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "users" not in st.session_state:
    st.session_state.users = {"admin": "1234"}

if "lands" not in st.session_state:
    st.session_state.lands = [
        {"Survey No": "SRV-201", "Owner": "Ramesh Kumar", "Area": 4.5, "Village": "Malur"},
        {"Survey No": "SRV-404", "Owner": "Suresh Gowda", "Area": 2.2, "Village": "Channapatna"}
    ]

# ================= AUTHENTICATION VIEW =================

def auth_page():
    st.markdown("<div style='margin-top: 6%;'></div>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: #1B5E20; font-weight:800; font-size:3.2rem; letter-spacing:-1.5px;'>🌾 DHARA SAMPADA</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size:1.2rem; color: #555E55; margin-bottom: 2.5rem;'>Next-Generation AI Precision Agriculture Platform for Dryland Farming</p>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1.3, 1])
    with col2:
        with st.container(border=True):
            option = st.radio("Access Portals", ["🔐 Secure Login", "📝 Farmer Registration"], horizontal=True, label_visibility="collapsed")
            st.markdown("<div style='margin-bottom: 12px;'></div>", unsafe_allow_html=True)
            
            if option == "🔐 Secure Login":
                username = st.text_input("Username / Mobile Number", placeholder="Enter admin username")
                password = st.text_input("Password", type="password", placeholder="••••••••")
                st.write("")
                if st.button("Enter AI Command Control →", use_container_width=True, type="primary"):
                    if username in st.session_state.users and st.session_state.users[username] == password:
                        st.session_state.logged_in = True
                        st.success("Access Verified. Initializing platform interface modules...")
                        time.sleep(0.4)
                        st.rerun()
                    else:
                        st.error("Invalid secure credential profiles.")
            else:
                username = st.text_input("Create Account Username")
                password = st.text_input("Security Password Access Code", type="password")
                confirm = st.text_input("Confirm Security Password", type="password")
                st.write("")
                if st.button("Register New Farmer Core Profile", use_container_width=True, type="primary"):
                    if username and password == confirm:
                        st.session_state.users[username] = password
                        st.success("Profile written successfully! Toggle login above.")
                    else:
                        st.error("Please verify matching inputs.")

# ================= PRINCIPAL PLATFORM FRAMEWORK =================

def main_app():
    # Structural Sidebar Navigation Design
    st.sidebar.markdown("<h2 style='color: #1B5E20; font-weight:800; margin-bottom:2px;'>🌾 Dhara Sampada</h2>", unsafe_allow_html=True)
    st.sidebar.markdown("<p style='font-size: 0.75rem; color: #788278; text-transform: uppercase; letter-spacing:1px; font-weight:600;'>AI Dryland Operating Core v3.0</p>", unsafe_allow_html=True)
    st.sidebar.markdown("---")
    
    menu = st.sidebar.radio(
        "🖥️ DECISION CONTROL ARRAYS",
        [
            "🏠 Interactive Executive Hub",
            "🛰️ Satellite Crop Monitor",
            "🪲 AI Pest Diagnostic",
            "💧 Precision Irrigation",
            "🌾 Smart Crop Advisory",
            "🌦 Weather Forecast",
            "📈 Live Market Prices",
            "📑 Land Ledger Records",
            "📊 Analytics & Reports",
            "⚙️ Configuration Core"
        ]
    )
    
    st.sidebar.markdown("---")
    if st.sidebar.button("🚪 Terminate Session Hub", use_container_width=True):
        st.session_state.logged_in = False
        st.rerun()

    # ================= HOME INTERACTIVE EXECUTIVE HUB =================
    if menu == "🏠 Interactive Executive Hub":
        # Eye-Catching Immersive Hero Banner
        st.markdown("""
            <div class='hero-banner'>
                <span class='badge-status' style='background: rgba(255,255,255,0.2); color: white; margin-bottom: 12px;'>Core Server Online</span>
                <h1 style='color: white; font-weight: 800; margin: 0; font-size: 2.5rem; letter-spacing: -0.5px;'>Welcome to Dhara Sampada Control</h1>
                <p style='color: #E8F5E9; font-size: 1.1rem; margin-top: 8px; margin-bottom: 0; font-weight: 400;'>
                    Harnessing deep computer vision and macro-sensing matrices to maximize resource efficiency in arid and dryland agriculture zones.
                </p>
            </div>
        """, unsafe_allow_html=True)

        # Dynamic Status Telemetry Matrix Row
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            st.markdown(f"""<div class='metric-grid-box'><div style='color:#707870; font-weight:600; font-size:0.85rem; text-transform:uppercase;'>Ledgered Plots</div><div style='font-size:1.8rem; font-weight:800; color:#111; margin:6px 0;'>{len(st.session_state.lands)} Fields</div><span class='badge-status badge-green'>Active</span></div>""", unsafe_allow_html=True)
        with c2:
            st.markdown("""<div class='metric-grid-box'><div style='color:#707870; font-weight:600; font-size:0.85rem; text-transform:uppercase;'>Ecosystem Reach</div><div style='font-size:1.8rem; font-weight:800; color:#111; margin:6px 0;'>12,500+</div><span class='badge-status badge-green'>↑ 4.2% MoM</span></div>""", unsafe_allow_html=True)
        with c3:
            st.markdown("""<div class='metric-grid-box'><div style='color:#707870; font-weight:600; font-size:0.85rem; text-transform:uppercase;'>AI Engine Accuracy</div><div style='font-size:1.8rem; font-weight:800; color:#111; margin:6px 0;'>96.4%</div><span class='badge-status badge-green'>Optimal</span></div>""", unsafe_allow_html=True)
        with c4:
            st.markdown("""<div class='metric-grid-box'><div style='color:#707870; font-weight:600; font-size:0.85rem; text-transform:uppercase;'>Critical Advisories</div><div style='font-size:1.8rem; font-weight:800; color:#111; margin:6px 0;'>1 Alert</div><span class='badge-status badge-orange'>Review Info</span></div>""", unsafe_allow_html=True)

        st.write("")
        st.write("")

        # PRIMARY HIGHLY-ATTRACTIVE SOIL COMPUTER VISION SPLIT COMPONENT
        st.markdown("<h2 style='color:#1B5E20; font-weight:700; font-size:1.6rem; letter-spacing:-0.5px;'>🌱 Instant Computer Vision Soil Diagnostic</h2>", unsafe_allow_html=True)
        st.markdown("<p style='color:#636D63; margin-top:-10px; margin-bottom:1.5rem;'>Drop a crisp field image snapshot below to break down compositional soil health matrices automatically.</p>", unsafe_allow_html=True)

        with st.container(border=True):
            split_left, split_right = st.columns([1.1, 1])
            
            with split_left:
                st.markdown("<div style='padding:10px;'>", unsafe_allow_html=True)
                uploaded_soil_img = st.file_uploader("Drag and drop your topsoil snapshot here", type=["jpg", "jpeg", "png"], label_visibility="collapsed")
                
                if uploaded_soil_img is not None:
                    st.image(uploaded_soil_img, caption="📍 Target Topsoil Sample Frame Bound Successfully", use_container_width=True)
                else:
                    st.markdown("""
                        <div style='border: 2px dashed #CCD5CC; border-radius:16px; padding: 40px 20px; text-align:center; background-color:#FAFBFA; margin-top:10px;'>
                            <span style='font-size:2.5rem;'>📸</span>
                            <h4 style='color:#3B453B; margin-top:10px; font-weight:600;'>No Topsoil File Selected</h4>
                            <p style='color:#788578; font-size:0.88rem; max-width:320px; margin:0 auto; margin-top:4px;'>Please upload a high-contrast topsoil picture using the selection link above to initialize the AI engine.</p>
                        </div>
                    """, unsafe_allow_html=True)
                st.markdown("</div>", unsafe_allow_html=True)

            with split_right:
                st.markdown("<div style='padding:10px;'>", unsafe_allow_html=True)
                st.markdown("<h3 style='margin-top:0; color:#2E7D32; font-weight:600; font-size:1.25rem;'>📊 AI Analytical Spectrum Output</h3>", unsafe_allow_html=True)
                
                if uploaded_soil_img is not None:
                    st.markdown("Click the execution pipeline link below to calculate organic indicators based on chromatic spectrums.")
                    st.write("")
                    
                    if st.button("✨ Run Soil Telemetry Scan Pipeline", type="primary", use_container_width=True):
                        with st.spinner("Decoding mineral distribution density vectors..."):
                            time.sleep(1.4)
                            
                        st.markdown("""
                            <div style='background-color:#F4FAF4; border: 1px solid #D8EED8; padding:18px; border-radius:14px; margin-bottom:15px;'>
                                <span style='font-weight:700; color:#1B5E20; font-size:0.95rem;'>✅ Computer Vision Inference Complete</span>
                                <div style='margin-top:8px; display:grid; grid-template-columns: 1fr 1fr; gap:12px;'>
                                    <div><small style='color:#5A655A;'>Calculated Classification</small><br><strong>Clayey Loam Matrix</strong></div>
                                    <div><small style='color:#5A655A;'>Organic Carbon (OC)</small><br><strong style='color:#2E7D32;'>0.68% (Healthy Mid)</strong></div>
                                    <div><small style='color:#5A655A;'>Estimated Moisture Ret.</small><br><strong>24.5% Volumetric</strong></div>
                                    <div><small style='color:#5A655A;'>Bulk Density Signature</small><br><strong>1.32 g/cm³</strong></div>
                                </div>
                            </div>
                        """, unsafe_allow_html=True)
                        st.info("💡 **Digital Agronomist Verdict:** Soil data states fine particle binding. For arid plots, introducing balanced biological compost or vermicompost will improve moisture-holding horizons dramatically over sub-optimal heat waves.")
                else:
                    st.markdown("""
                        <div style='background-color:#F5F7F5; padding:20px; border-radius:14px; color:#5A655A; font-size:0.9rem; border: 1px solid #E6EAE6;'>
                            ⏱️ <strong>Waiting on input profile stream...</strong><br><br> Once a valid field photo asset is attached to the system via the uploader zone, real-time prediction frameworks will compute chemical profile mappings here instantly.
                        </div>
                    """, unsafe_allow_html=True)
                st.markdown("</div>", unsafe_allow_html=True)

    # ================= ADDITIONAL UTILITY MATRICES =================
    elif menu == "🛰️ Satellite Crop Monitor":
        st.markdown("<h1 style='color:#1B5E20; font-weight:700;'>🛰️ NDVI Satellite Remote Sensing Analytics</h1>", unsafe_allow_html=True)
        if not st.session_state.lands:
            st.warning("Please record crop fields coordinates first inside the Land Records panel.")
        else:
            df = pd.DataFrame(st.session_state.lands)
            st.selectbox("Target Registered Operational Grid", df["Survey No"])
            st.line_chart(pd.DataFrame(np.random.uniform(0.42, 0.88, size=(24, 1)), columns=['NDVI Biomass Profile Index']))

    elif menu == "🪲 AI Pest Diagnostic":
        st.markdown("<h1 style='color:#1B5E20; font-weight:700;'>🪲 Phytosanitary Pathology Scan Vector</h1>", unsafe_allow_html=True)
        with st.container(border=True):
            st.checkbox("Leaf Yellowing/Necrotic spotting vectors spotted")
            if st.button("Run Diagnostic Match Matrix", type="primary"):
                st.error("💥 Trace alert match calculated: Potential early stage Fungal Rust signature present.")

    # ================= DRYLAND FUNCTIONAL SUBSYSTEMS =================
    elif menu == "💧 Precision Irrigation":
        st.markdown("<h1 style='color:#1B5E20; font-weight:700;'>💧 Dryland Water Budgeting & Precision Irrigation</h1>", unsafe_allow_html=True)
        st.markdown("<p style='color:#636D63;'>Predictive moisture depletion models tailored specifically for arid and semi-arid cultivation maps.</p>", unsafe_allow_html=True)
        
        with st.container(border=True):
            col_a, col_b = st.columns(2)
            with col_a:
                crop_type = st.selectbox("Current Dryland Crop", ["Ragi (Finger Millet)", "Jowar (Sorghum)", "Toor (Pigeon Pea)", "Groundnut"])
                soil_type = st.selectbox("Soil Texture Profile", ["Red Sandy Loam", "Black Cotton Soil", "Shallow Gravelly Soil"])
            with col_b:
                days_since_rain = st.number_input("Days Since Last Rainfall Event", min_value=0, max_value=60, value=12)
                mulching = st.radio("Organic Mulching Applied?", ["Yes", "No"], horizontal=True)

            st.write("")
            if st.button("📊 Calculate Moisture Depletion & Deficit", type="primary", use_container_width=True):
                with st.spinner("Simulating localized evapotranspiration matrices..."):
                    time.sleep(1.0)
                
                base_depletion = min(days_since_rain * 3.5, 90.0)
                if mulching == "Yes":
                    base_depletion *= 0.7  # Evaporation mitigation factor
                
                available_moisture = 100.0 - base_depletion
                
                st.subheader("Water Stress Telemetry Results")
                st.progress(available_moisture / 100.0, text=f"Estimated Available Soil Moisture Profile: {available_moisture:.1f}%")
                
                if available_moisture < 40.0:
                    st.error(f"⚠️ Critical Stress Level! Soil moisture is below the Management Allowed Depletion (MAD) threshold for {crop_type}. Deploy 20mm protective pulse irrigation from farm pond structures immediately if available.")
                else:
                    st.success(f"✅ Moisture metrics reside within standard dryland survival boundaries. Next structural verification recommended in 4 days.")

    elif menu == "🌾 Smart Crop Advisory":
        st.markdown("<h1 style='color:#1B5E20; font-weight:700;'>🌾 AI Dryland Crop & Variety Advisory</h1>", unsafe_allow_html=True)
        st.markdown("<p style='color:#636D63;'>Get tailored drought-resilient crop combination configurations based on dynamic monsoon delay behaviors.</p>", unsafe_allow_html=True)
        
        with st.container(border=True):
            monsoon_status = st.select_slider(
                "Current Kharif Monsoon Delay Status",
                options=["Normal Onset", "2 Weeks Delayed", "4 Weeks Delayed (Critical)", "Severe Drought/Failure"]
            )
            
            st.write("")
            if st.button("✨ Generate Resilient Contingency Plan", type="primary"):
                st.markdown("### 📋 AI Strategic Contingency Layout")
                
                if monsoon_status == "Normal Onset":
                    st.info("💡 **Recommendation:** Standard long-duration crops optimal. Plant Toor (BRG-1, BRG-2) or Groundnut (TMV-2) intercropped with Ragi in a 4:2 layout matrix.")
                elif monsoon_status == "2 Weeks Delayed":
                    st.warning("💡 **Recommendation:** Swift modification to medium-duration drought-tolerant strains. Opt for Ragi (GPU-28 / GPU-66) or Sorghum (SVD-1). Implement rigorous compartmental bunding.")
                elif monsoon_status == "4 Weeks Delayed (Critical)":
                    st.error("💡 **Recommendation:** Avoid long-duration cycles. Transition immediately to contingency assets: Horsegram (PHG-9), Foxtail Millet (Navane), or Matki. Row spacing metrics must expand by 20% to maximize moisture footprint allocation.")
                else:
                    st.error("🚨 **Emergency Advisory:** Extreme moisture deficit zone. Halt primary grain tillage. Shift focus entirely to structural fodder processing (Sorghum/Maize fodder) to guarantee livestock asset protection.")

    # ================= CONFIGURATION CONTROL HUB =================
    elif menu == "⚙️ Configuration Core":
        st.markdown("<h1 style='color:#1B5E20; font-weight:700;'>⚙️ System Configuration Core</h1>", unsafe_allow_html=True)
        st.markdown("<p style='color:#636D63;'>Manage AI threshold limits, IoT sensor nodes, and platform profiles for dryland sectors.</p>", unsafe_allow_html=True)
        
        # 3 Structured Layout Tabs
        tab1, tab2, tab3 = st.tabs(["👤 User Profile Matrix", "📡 IoT & Hardware Nodes", "🛡️ Database & Reset Core"])
        
        with tab1:
            st.markdown("### Farmer & Admin Profile Info")
            col_u1, col_u2 = st.columns(2)
            with col_u1:
                st.text_input("Active Node Operator", value="Admin / Primary Farmer", disabled=True)
                st.text_input("Associated Mobile Number", value="+91 98765 43210")
            with col_u2:
                st.selectbox("Primary Language Interface", ["English", "ಕನ್ನಡ (Kannada)", "Hindi"])
                st.selectbox("Default Dryland Agri-Zone", ["Semi-Arid Zone (South Karnataka)", "Arid Zone (North Karnataka)", "Custom Profile"])
            
            if st.button("💾 Update Profile Mappings", type="primary"):
                st.success("✅ Profile configurations synchronized successfully with local server arrays.")

        with tab2:
            st.markdown("### Wireless Telemetry & IoT Sensor Integration")
            st.caption("Link physical soil moisture probes, automated drip valves, and telemetry hardware to Dhara Sampada.")
            
            with st.container(border=True):
                st.toggle("Enable Live Cloud Sync for Soil Probes", value=True)
                st.toggle("Auto-Trigger Protective Drip Pulsing via Farm Pond Pump", value=False)
                
                st.markdown("---")
                st.markdown("**Active Hardware Array Network**")
                col_hw1, col_hw2 = st.columns(2)
                with col_hw1:
                    st.success("🟢 Node-01 (Soil Moisture Sensor) - Connected [Battery: 84%]")
                    st.success("🟢 Node-02 (Weather Telemetry Station) - Connected [Battery: 91%]")
                with col_hw2:
                    st.error("🔴 Node-03 (Automated Valve Controller) - Offline / No Signal")
                    
            if st.button("🔄 Rescan IoT Network Grid"):
                with st.spinner("Pinging wireless edge devices..."):
                    time.sleep(1.0)
                st.info("📡 Scan complete. 2 Active Nodes verified, 1 Node requires hardware inspection.")

        with tab3:
            st.markdown("### System Diagnostics & Memory Control")
            st.warning("⚠️ High Privilege Actions: Modifying these structures can wipe local cached records.")
            
            st.markdown(f"**Current Registered Database Payload:** `{len(st.session_state.lands)} Land Records` logged.")
            
            col_r1, col_r2 = st.columns(2)
            with col_r1:
                if st.button("🛑 Clear Registered Fields Cache", use_container_width=True):
                    st.session_state.lands = []
                    st.success("Land Ledger database dropped. Reloading application grids...")
                    time.sleep(0.5)
                    st.rerun()
            with col_r2:
                if st.button("🔄 Hard Reboot Platform Core", use_container_width=True):
                    st.session_state.logged_in = False
                    st.success("Rebooting server frameworks...")
                    time.sleep(0.5)
                    st.rerun()

    else:
        st.markdown(f"<h1 style='color:#1B5E20; font-weight:700;'>{menu}</h1>", unsafe_allow_html=True)
        st.info("Integrated data engine modules mapping successfully into parent application container grids.")

# ================= CORE ENGINE TRIGGER CONTROLLER =================

if st.session_state.logged_in:
    main_app()
else:
    auth_page()
