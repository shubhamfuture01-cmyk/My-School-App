import streamlit as st

# --- APP CONFIGURATION ---
st.set_page_config(page_title="My School - AI Guru", page_icon="🏫", layout="centered")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    body { -webkit-user-select: none; -moz-user-select: none; -ms-user-select: none; user-select: none; }
    .stApp { background-color: #f0f2f6; }
    </style>
    """, unsafe_allow_html=True)

# --- MASTER DATABASE ---
MASTER_DATA = {
    "Class 1": {"Maths": "Counting 1-20, Shapes (Roti-Circle), Big/Small.", "VVIP": "5 ke baad kya aata hai?"},
    "Class 10": {"Science": "Chemical Reactions, Light, Electricity.", "Maths": "Real Numbers, Trigonometry.", "VVIP": "Prove √2 is irrational?"},
    "Class 12 Science": {"Physics": "Gauss Law, Kirchhoff’s Laws, Optics.", "VVIP": "PN Junction working."}
}

# --- APP LOGIC ---
st.title("🏫 My School: Aapka Digital Guru")
st.subheader("Easy. Best. Affordable.")

if 'logged_in' not in st.session_state:
    mobile = st.text_input("Mobile Number", placeholder="98XXXXXXXX")
    if st.button("Get OTP"):
        st.session_state.logged_in = True
        st.rerun()
else:
    st.sidebar.image("https://icons8.com")
    selected_class = st.selectbox("Apni Class Chuniye:", list(MASTER_DATA.keys()))

    if 'premium' not in st.session_state:
        st.warning("🔒 Subscription Fees: ₹199 (One-time)")
        if st.button("Pay ₹199 Now"):
            st.session_state.premium = True
            st.balloons()
            st.rerun()
    else:
        subjects = list(MASTER_DATA[selected_class].keys())
        sub = st.radio("Subject Chuniye:", [s for s in subjects if s != "VVIP"])
        st.info(MASTER_DATA[selected_class][sub])
        st.error(f"🔥 VVIP: {MASTER_DATA[selected_class]['VVIP']}")
        
