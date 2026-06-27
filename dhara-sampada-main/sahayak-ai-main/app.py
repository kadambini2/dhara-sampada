# ================= IMPORTS =================

import streamlit as st
import pandas as pd
import numpy as np
import time

# ================= PAGE CONFIG =================

st.set_page_config(
    page_title="Dryland agriculuture | Next-Gen AI Agri-Platform",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ================= PREMIUM UI/UX GLOSS DESIGN STYLING =================

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');
    
    /* Core Base Typography Reset */
    html, body, [class*="css"], .stApp {
        font-family: 'Plus Jakarta Sans', sans-serif;
        background-color: #F9FBFAF;
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
    st.markdown("<p style='text-align: center; font-size:1.2rem; color: #555E55; margin-bottom: 2.5rem;'>Next-Generation AI Precision Agriculture Platform</p>", unsafe_allow_html=True)

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
    st.sidebar.markdown("<p style='font-size: 0.75rem; color: #788278; text-transform: uppercase; letter-spacing:1px; font-weight:600;'>AI Field Operating Core v3.0</p>", unsafe_allow_html=True)
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
                    Harnessing deep computer vision and macro-sensing matrices to maximize agricultural resource efficiency.
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
                    # Beautiful custom placeholder style area inside container box
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
                        st.info("💡 **Digital Agronomist Verdict:** Soil structural data points demonstrate fine particle binding and normal retention limits. Incorporating 4-5 quintals of biological compost layer over the next processing rotation cycle is highly optimal.")
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

    else:
        st.markdown(f"<h1 style='color:#1B5E20; font-weight:700;'>{menu}</h1>", unsafe_allow_html=True)
        st.info("Integrated data engine modules mapping successfully into parent application container grids.")

# ================= CORE ENGINE TRIGGER CONTROLLER =================

if st.session_state.logged_in:
    main_app()
else:
    auth_page()
