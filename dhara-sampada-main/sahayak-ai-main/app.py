# ================= IMPORTS =================

import streamlit as st
import pandas as pd
import numpy as np
import time

# ================= PAGE CONFIG =================

st.set_page_config(
    page_title="Dhara Sampada | AI Dryland Platform",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ================= PREMIUM UI/UX GLOSS DESIGN STYLING =================

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght=300;400;500;600;700;800&display=swap');
    
    html, body, [class*="css"], .stApp {
        font-family: 'Plus Jakarta Sans', sans-serif;
        background-color: #F9FBF9;
    }
    
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
    .badge-blue { background-color: #E3F2FD; color: #0D47A1; }
    
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
    st.sidebar.markdown("<h2 style='color: #1B5E20; font-weight:800; margin-bottom:2px;'>🌾 Dhara Sampada</h2>", unsafe_allow_html=True)
    st.sidebar.markdown("<p style='font-size: 0.75rem; color: #788278; text-transform: uppercase; letter-spacing:1px; font-weight:600;'>AI Dryland Operating Core v3.5</p>", unsafe_allow_html=True)
    st.sidebar.markdown("---")
    
    menu = st.sidebar.radio(
        "🖥️ DECISION CONTROL ARRAYS",
        [
            "🏠 Interactive Executive Hub",
            "🛰️ Satellite Crop Monitor",
            "🪲 AI Pest Diagnostic",
            "💧 Precision Irrigation",
            "🌾 Smart Crop Advisory",
            "📊 ROI & Budget Generator",
            "🧵 Family Skills & Handicrafts",
            "🏛️ Government Applications",
            "📈 Live Market Prices",
            "📑 Land Ledger Records",
            "⚙️ Configuration Core"
        ]
    )
    
    st.sidebar.markdown("---")
    if st.sidebar.button("🚪 Terminate Session Hub", use_container_width=True):
        st.session_state.logged_in = False
        st.rerun()

    # ================= 🏠 HOME INTERACTIVE EXECUTIVE HUB =================
    if menu == "🏠 Interactive Executive Hub":
        st.markdown("""
            <div class='hero-banner'>
                <span class='badge-status' style='background: rgba(255,255,255,0.2); color: white; margin-bottom: 12px;'>Core Server Online</span>
                <h1 style='color: white; font-weight: 800; margin: 0; font-size: 2.5rem; letter-spacing: -0.5px;'>Welcome to Dhara Sampada Control</h1>
                <p style='color: #E8F5E9; font-size: 1.1rem; margin-top: 8px; margin-bottom: 0; font-weight: 400;'>
                    Harnessing deep computer vision and macro-sensing matrices to maximize resource efficiency in arid and dryland agriculture zones.
                </p>
            </div>
        """, unsafe_allow_html=True)

        c1, c2, c3, c4 = st.columns(4)
        with c1:
            st.markdown(f"""<div class='metric-grid-box'><div style='color:#707870; font-weight:600; font-size:0.85rem; text-transform:uppercase;'>Ledgered Plots</div><div style='font-size:1.8rem; font-weight:800; color:#111; margin:6px 0;'>{len(st.session_state.lands)} Fields</div><span class='badge-status badge-green'>Active</span></div>""", unsafe_allow_html=True)
        with c2:
            st.markdown("""<div class='metric-grid-box'><div style='color:#707870; font-weight:600; font-size:0.85rem; text-transform:uppercase;'>Ecosystem Reach</div><div style='font-size:1.8rem; font-weight:800; color:#111; margin:6px 0;'>12,500+</div><span class='badge-status badge-green'>↑ 4.2% MoM</span></div>""", unsafe_allow_html=True)
        with c3:
            st.markdown("""<div class='metric-grid-box'><div style='color:#707870; font-weight:600; font-size:0.85rem; text-transform:uppercase;'>AI Engine Accuracy</div><div style='font-size:1.8rem; font-weight:800; color:#111; margin:6px 0;'>96.4%</div><span class='badge-status badge-green'>Optimal</span></div>""", unsafe_allow_html=True)
        with c4:
            st.markdown("""<div class='metric-grid-box'><div style='color:#707870; font-weight:600; font-size:0.85rem; text-transform:uppercase;'>Active Schemes</div><div style='font-size:1.8rem; font-weight:800; color:#111; margin:6px 0;'>4 Live</div><span class='badge-status badge-blue'>Linked</span></div>""", unsafe_allow_html=True)

        st.write("")
        st.markdown("<h2 style='color:#1B5E20; font-weight:700; font-size:1.6rem; letter-spacing:-0.5px;'>🌱 Instant Computer Vision Soil Diagnostic</h2>", unsafe_allow_html=True)

        with st.container(border=True):
            split_left, split_right = st.columns([1.1, 1])
            with split_left:
                uploaded_soil_img = st.file_uploader("Upload topsoil snapshot", type=["jpg", "jpeg", "png"], label_visibility="collapsed")
                if uploaded_soil_img is not None:
                    st.image(uploaded_soil_img, caption="📍 Target Topsoil Bound Successfully", use_container_width=True)
                else:
                    st.markdown("<div style='border: 2px dashed #CCD5CC; border-radius:16px; padding: 40px 20px; text-align:center; background-color:#FAFBFA; margin-top:10px;'><span style='font-size:2.5rem;'>📸</span><h4 style='color:#3B453B; margin-top:10px; font-weight:600;'>No Topsoil File Selected</h4></div>", unsafe_allow_html=True)

            with split_right:
                st.markdown("<h3 style='margin-top:0; color:#2E7D32; font-weight:600; font-size:1.25rem;'>📊 AI Analytical Spectrum Output</h3>", unsafe_allow_html=True)
                if uploaded_soil_img is not None:
                    if st.button("✨ Run Soil Telemetry Scan Pipeline", type="primary", use_container_width=True):
                        with st.spinner("Decoding mineral density vectors..."):
                            time.sleep(1.2)
                        st.markdown("<div style='background-color:#F4FAF4; border: 1px solid #D8EED8; padding:18px; border-radius:14px;'><strong>Clayey Loam Matrix</strong><br>Organic Carbon: 0.68% (Optimal)</div>", unsafe_allow_html=True)
                else:
                    st.markdown("<div style='background-color:#F5F7F5; padding:20px; border-radius:14px; color:#5A655A; font-size:0.9rem;'>⏱️ Waiting on input profile stream...</div>", unsafe_allow_html=True)

    # ================= 🛰️ SATELLITE CROP MONITOR =================
    elif menu == "🛰️ Satellite Crop Monitor":
        st.markdown("<h1 style='color:#1B5E20; font-weight:700;'>🛰️ NDVI Satellite Remote Sensing Analytics</h1>", unsafe_allow_html=True)
        st.markdown("<p style='color:#636D63;'>Track vegetation density indices across mapped survey bounds seamlessly.</p>", unsafe_allow_html=True)
        st.line_chart(pd.DataFrame(np.random.uniform(0.42, 0.88, size=(24, 1)), columns=['NDVI Biomass Profile Index']))

    # ================= 🪲 AI PEST DIAGNOSTIC =================
    elif menu == "🪲 AI Pest Diagnostic":
        st.markdown("<h1 style='color:#1B5E20; font-weight:700;'>🪲 Phytosanitary Pathology Scan Vector</h1>", unsafe_allow_html=True)
        with st.container(border=True):
            st.checkbox("Leaf Yellowing / Necrotic spotting vectors spotted")
            if st.button("Run Diagnostic Match Matrix", type="primary"):
                st.error("💥 Trace alert match calculated: Potential early stage Fungal Rust signature present.")

    # ================= 💧 PRECISION IRRIGATION =================
    elif menu == "💧 Precision Irrigation":
        st.markdown("<h1 style='color:#1B5E20; font-weight:700;'>💧 Dryland Water Budgeting & Precision Irrigation</h1>", unsafe_allow_html=True)
        with st.container(border=True):
            days_since_rain = st.number_input("Days Since Last Rainfall Event", min_value=0, max_value=60, value=12)
            if st.button("📊 Analyze Moisture Deficit Profile", type="primary"):
                if days_since_rain > 10:
                    st.warning("⚠️ Critical Depletion: Available soil moisture dropped below 40%. Deploy 20mm protective pulse irrigation immediately.")
                else:
                    st.success("✅ Moisture metrics reside within standard dryland survival boundaries.")

    # ================= 🌾 SMART CROP ADVISORY =================
    elif menu == "🌾 Smart Crop Advisory":
        st.markdown("<h1 style='color:#1B5E20; font-weight:700;'>🌾 AI Dryland Crop & Variety Advisory</h1>", unsafe_allow_html=True)
        with st.container(border=True):
            delay = st.selectbox("Current Monsoon Delay Status", ["Normal Onset", "2 Weeks Delayed", "4 Weeks Delayed (Critical)"])
            if st.button("✨ Generate Contingency Plan", type="primary"):
                if "Critical" in delay:
                    st.error("💡 Strategic Advisory: Shift immediately to short-duration contingency assets: Horsegram (PHG-9) or Foxtail Millet (Navane).")
                else:
                    st.info("💡 Strategic Advisory: Plant standard Ragi intercropped with Toor in a 4:2 layout matrix.")

    # ================= 📊 ROI & BUDGET GENERATOR (NEW) =================
    elif menu == "📊 ROI & Budget Generator":
        st.markdown("<h1 style='color:#1B5E20; font-weight:700;'>📊 Dryland Cultivation ROI Calculator</h1>", unsafe_allow_html=True)
        st.markdown("<p style='color:#636D63;'>Estimate total cost of cultivation, expected market yield, and predictable net income parameters.</p>", unsafe_allow_html=True)
        
        with st.container(border=True):
            col_roi1, col_roi2 = st.columns(2)
            with col_roi1:
                crop_select = st.selectbox("Target Agri Crop Portfolio", ["Ragi (Finger Millet)", "Toor Dal", "Groundnut"])
                area_acres = st.number_input("Cultivation Area Size (Acres)", min_value=0.5, max_value=100.0, value=2.0, step=0.5)
            with col_roi2:
                seed_cost = st.number_input("Estimated Cost of Inputs / Labor per Acre (₹)", min_value=1000, max_value=50000, value=8500)
                expected_price = st.number_input("Targeted Market Selling Price (₹/Quintal)", min_value=1000, max_value=20000, value=3850)

            st.write("")
            if st.button("🧮 Compute Financial Projections", type="primary", use_container_width=True):
                # Calculate simple dryland agribusiness ROI metrics
                total_investment = seed_cost * area_acres
                avg_yield_per_acre = 10 if crop_select == "Ragi" else (6 if crop_select == "Toor Dal" else 8)
                total_yield = avg_yield_per_acre * area_acres
                gross_revenue = total_yield * expected_price
                net_profit = gross_revenue - total_investment
                roi_percentage = (net_profit / total_investment) * 100 if total_investment > 0 else 0
                
                st.markdown("### 📋 Financial Performance Ledger")
                c_r1, c_r2, c_r3, c_r4 = st.columns(4)
                with c_r1:
                    st.metric("Total Input Expense", f"₹{total_investment:,.2f}")
                with c_r2:
                    st.metric("Estimated Total Yield", f"{total_yield:.1f} Qtls")
                with c_r3:
                    st.metric("Projected Net Income", f"₹{net_profit:,.2f}")
                with c_r4:
                    st.metric("Calculated Return Ratio", f"{roi_percentage:.1f}%")

    # ================= 🧵 FAMILY SKILLS & HANDICRAFTS (NEW) =================
    elif menu == "🧵 Family Skills & Handicrafts":
        st.markdown("<h1 style='color:#1B5E20; font-weight:700;'>🧵 Rural Artisan Skills & Non-Farm Micro-Income</h1>", unsafe_allow_html=True)
        st.markdown("<p style='color:#636D63;'>Empower multi-generational farming households with off-season handicraft mapping, cottage industries, and market linkages.</p>", unsafe_allow_html=True)
        
        tab_skill1, tab_skill2 = st.tabs(["📚 Active Skill Training Profiles", "🏺 Local Handicrafts Marketplace Setup"])
        with tab_skill1:
            st.markdown("### Available Off-Season Cottage Training Programs")
            col_s1, col_s2 = st.columns(2)
            with col_s1:
                with st.container(border=True):
                    st.markdown("#### 🧶 Khadi & Eco-Textile Weaving")
                    st.caption("Duration: 4 Weeks | Sponsoring Body: KVIC Karnataka")
                    st.markdown("**Status:** `🟢 Enrolling Now`")
                    if st.button("Apply to Training Unit A", use_container_width=True):
                        st.success("Application dispatched safely to district rural skill coordinators.")
            with col_s2:
                with st.container(border=True):
                    st.markdown("#### 🍯 Organic Honey Processing & Basketry")
                    st.caption("Duration: 2 Weeks | Target: Self-Help Groups (SHGs)")
                    st.markdown("**Status:** `🟢 Commencing June 2026`")
                    if st.button("Apply to Training Unit B", use_container_width=True):
                        st.success("SHG group roster allocation confirmed successfully.")
                        
        with tab_skill2:
            st.markdown("### Inventory Allocation for Local Rural Products")
            with st.form("artisan_form"):
                artisan_name = st.text_input("Artisan Household Head Name")
                product_cat = st.selectbox("Product Portfolio Line", ["Hand-woven Cotton Mats", "Terracotta Pottery Artifacts", "Agro-Waste Organic Handicrafts"])
                stock_vol = st.slider("Available Batch Volume Units for Marketplace Listing", 1, 500, 25)
                submit_artisan = st.form_submit_submit_button = st.form_submit_button("🚀 Deploy Asset to Digital Marketplace")
                if submit_artisan:
                    st.success(f"Successfully processed registration profile for {artisan_name}. {stock_vol} units uploaded to local e-bazaar directories.")

    # ================= 🏛️ GOVERNMENT APPLICATIONS & SCHEMES (NEW) =================
    elif menu == "🏛️ Government Applications":
        st.markdown("<h1 style='color:#1B5E20; font-weight:700;'>🏛️ Integrated Government Schemes & Application Gateway</h1>", unsafe_allow_html=True)
        st.markdown("<p style='color:#636D63;'>Verify framework parameters, check automated structural eligibility alignments, and register profiles instantly.</p>", unsafe_allow_html=True)
        
        with st.container(border=True):
            st.markdown("### Automated Eligibility Engine Tracker")
            farmer_holding = st.number_input("Total Land Holding Threshold Size (Acres)", min_value=0.0, value=2.5)
            caste_category = st.selectbox("Social Category Matrix", ["General / OBC", "SC / ST", "Minority Profiles"])
            
            if st.button("🔍 Run Central Scheme Eligibility Verification", type="primary"):
                st.write("")
                st.markdown("#### Meta-Matched Direct Benefit Schemes")
                
                # Dynamic rules-based eligibility matching simulation
                if farmer_holding <= 5.0:
                    st.markdown("""
                        * ✅ **PM-KISAN Samman Nidhi:** Eligible (`₹6,000 / Year Direct Income Support`).
                        * ✅ **Kracshik Bandhu / State Arid Incentive Matrix:** Small/Marginal Farmer Category verified. Eligible for 100% micro-irrigation sub-surface subsidy packages.
                    """)
                else:
                    st.markdown("""
                        * ✅ **PM-KISAN Samman Nidhi:** Eligible (`Standard Acreage Cap Tier`).
                        * ⚠️ **Custom Farm Pond Subsidies:** Partial cost-sharing model triggered based on land parameters.
                    """)
                    
                if caste_category == "SC / ST":
                    st.markdown("* ✅ **Ganga Kalyana Scheme / State Borewell Support:** Special priority quota verified. 100% financial clearance available.")
                    
        st.write("")
        st.markdown("### 📑 Live Application Tracker Framework")
        schemes_tracker = {
            "Application Tracking Ref": ["APP-PMK-9021", "APP-GK-3841", "APP-FOND-1102"],
            "Target Scheme Structure": ["PM-KISAN Base Renewal", "Ganga Kalyana Allocation", "Krishi Honda (Farm Pond) Subsidy"],
            "Verification Stage Status": ["Approved & Disbursed", "Pending Field Survey Audit", "Document Verification Phase"],
            "Last Update Timestamp": ["12-May-2026", "24-June-2026", "26-June-2026"]
        }
        st.table(pd.DataFrame(schemes_tracker))

    # ================= 📈 LIVE MARKET PRICES =================
    elif menu == "📈 Live Market Prices":
        st.markdown("<h1 style='color:#1B5E20; font-weight:700;'>📈 Live Dryland Market Commodity Prices</h1>", unsafe_allow_html=True)
        cm1, cm2, cm3, cm4 = st.columns(4)
        with cm1:
            st.markdown("""<div class='metric-grid-box'><div style='color:#707870; font-weight:600; font-size:0.85rem;'>RAGI (FINGER MILLET)</div><div style='font-size:1.6rem; font-weight:800; color:#111; margin:6px 0;'>₹3,850 / Qtl</div><span class='badge-status badge-green'>▲ ₹50 (Bengaluru)</span></div>""", unsafe_allow_html=True)
        with cm2:
            st.markdown("""<div class='metric-grid-box'><div style='color:#707870; font-weight:600; font-size:0.85rem;'>TOOR DAL (PIGEON PEA)</div><div style='font-size:1.6rem; font-weight:800; color:#111; margin:6px 0;'>₹12,400 / Qtl</div><span class='badge-status badge-green'>▲ ₹120 (Kalaburagi)</span></div>""", unsafe_allow_html=True)
        with cm3:
            st.markdown("""<div class='metric-grid-box'><div style='color:#707870; font-weight:600; font-size:0.85rem;'>JOWAR (SORGHUM)</div><div style='font-size:1.6rem; font-weight:800; color:#111; margin:6px 0;'>₹5,200 / Qtl</div><span class='badge-status badge-orange'>▼ ₹30 (Hubballi)</span></div>""", unsafe_allow_html=True)
        with cm4:
            st.markdown("""<div class='metric-grid-box'><div style='color:#707870; font-weight:600; font-size:0.85rem;'>GROUNDNUT (OILSEED)</div><div style='font-size:1.6rem; font-weight:800; color:#111; margin:6px 0;'>₹7,150 / Qtl</div><span class='badge-status badge-green'>▲ ₹80 (Davangere)</span></div>""", unsafe_allow_html=True)
            
        with st.container(border=True):
            st.markdown("### 🏛️ APMC Regional Market Ledger Insights")
            market_data = {
                "Commodity": ["Ragi", "Toor Dal", "Jowar", "Groundnut"],
                "Minimum Price (₹/Qtl)": [3400, 11500, 4800, 6500],
                "Maximum Price (₹/Qtl)": [4100, 13200, 5600, 7600],
                "Model Price (₹/Qtl)": [3850, 12400, 5200, 7150]
            }
            st.dataframe(pd.DataFrame(market_data), use_container_width=True, hide_index=True)

    # ================= 📑 LAND LEDGER RECORDS =================
    elif menu == "📑 Land Ledger Records":
        st.markdown("<h1 style='color:#1B5E20; font-weight:700;'>📑 Certified Land Ledger Registry Records</h1>", unsafe_allow_html=True)
        with st.container(border=True):
            st.dataframe(pd.DataFrame(st.session_state.lands), use_container_width=True, hide_index=True)
            st.markdown("---")
            st.markdown("#### Append New Plot Horizon Profile")
            with st.columns(3):
                srv = st.text_input("Survey Index Number", placeholder="e.g. SRV-901")
                own = st.text_input("Registered Legal Owner", placeholder="Full Name")
                sz = st.number_input("Area Coverage (Acres)", min_value=0.1, value=1.0)
            if st.button("➕ Add Plot Record Profile to State Node Registry", type="primary"):
                if srv and own:
                    st.session_state.lands.append({"Survey No": srv, "Owner": own, "Area": sz, "Village": "Local Node Cluster"})
                    st.success("New land registration written to core session structures successfully!")
                    time.sleep(0.4)
                    st.rerun()

    # ================= ⚙️ CONFIGURATION CORE =================
    elif menu == "⚙️ Configuration Core":
        st.markdown("<h1 style='color:#1B5E20; font-weight:700;'>⚙️ System Configuration Core</h1>", unsafe_allow_html=True)
        tab1, tab2, tab3 = st.tabs(["👤 User Profile Matrix", "📡 IoT & Hardware Nodes", "🛡️ Database & Reset Core"])
        
        with tab1:
            st.text_input("Active Node Operator", value="Admin / Primary Farmer", disabled=True)
            st.selectbox("Primary Language Interface", ["English", "ಕನ್ನಡ (Kannada)", "Hindi"])
            if st.button("💾 Save Profile Changes", type="primary"):
                st.success("Profile written successfully.")
        with tab2:
            st.toggle("Enable Live Cloud Sync for Soil Probes", value=True)
            st.success("🟢 Node-01 (Soil Moisture Sensor) - Connected [Battery: 84%]")
        with tab3:
            st.caption("Clear function execution memory allocations built with @st.cache markers safely.")
            if st.button("♻️ Purge All Function Caches", use_container_width=True):
                st.cache_data.clear()
                st.cache_resource.clear()
                st.success("✅ Application function caches wiped cleanly from Streamlit memory core successfully!")

# ================= CORE ENGINE TRIGGER CONTROLLER =================

if st.session_state.logged_in:
    main_app()
else:
    auth_page()
