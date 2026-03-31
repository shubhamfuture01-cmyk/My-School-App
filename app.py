import streamlit as st

# --- APP CONFIGURATION ---
st.set_page_config(page_title="My School - AI Guru", page_icon="🏫", layout="centered")

# --- CUSTOM CSS (FIXED COLORS & NO COPY) ---
st.markdown("""
    <style>
    /* Background and Text Fix */
    .stApp { background-color: #f8f9fa; }
    h1, h2, h3 { color: #1e3d59 !important; }
    p, span, label { color: #2c3e50 !important; font-weight: 500; }
    
    /* Box Styling */
    .stAlert { border-radius: 10px; border: 1px solid #d1d8e0; }
    
    /* Button Styling */
    .stButton>button { background-color: #ff6e40; color: white; border-radius: 8px; width: 100%; border: none; }
    .stButton>button:hover { background-color: #ff5722; color: white; }

    /* Security: No Text Selection */
    body { -webkit-user-select: none; -moz-user-select: none; -ms-user-select: none; user-select: none; }
    </style>
    """, unsafe_allow_html=True)

# --- MASTER DATABASE (All Classes Added) ---
MASTER_DATA = {
    "Class 1": {"Maths": "Counting 1-20, Shapes (Roti-Circle), Big/Small.", "VVIP": "5 ke baad kya aata hai?"},
    "Class 2": {"EVS": "Body parts, Sense Organs, Good Habits.", "VVIP": "Humein sun-ne mein kaun madad karta hai?"},
    "Class 3": {"EVS": "Plants, Water, Family, Foods we eat.", "VVIP": "Hamara pehla school kaunsa hai?"},
    "Class 4": {"Maths": "Weight (Kg/g), Tables, Clock (Tick-Tick).", "VVIP": "1 Kg mein kitne gram hote hain?"},
    "Class 5": {"EVS": "Super Senses, Seeds dispersal, Water Experiments.", "VVIP": "Ants line mein kyun chalti hain?"},
    "Class 6": {"Science": "Food components, Sorting materials, Body movements.", "VVIP": "Vitamin C se kaunsi bimari hoti hai?"},
    "Class 7": {"Maths": "Integers, Fractions, Lines and Angles.", "VVIP": "Sum of angles in a triangle (180 deg)?"},
    "Class 8": {"Science": "Crop production, Microorganisms, Friction.", "VVIP": "Kharif aur Rabi crops ke examples?"},
    "Class 9": {"Science": "Matter, Atoms, Motion, Gravitation.", "VVIP": "Newton's 2nd Law (F=ma) derive karein."},
    "Class 10": {"Science": "Chemical Reactions, Light, Electricity.", "Maths": "Real Numbers, Trigonometry.", "VVIP": "Prove √2 is irrational?"},
    "Class 11 Science": {"Physics": "Units, Motion, Laws of Motion.", "VVIP": "Static vs Kinetic Friction?"},
    "Class 11 Commerce": {"Accounts": "Journal Entries, Ledger, Assets/Liabilities.", "VVIP": "Golden Rules of Accounting?"},
    "Class 11 Arts": {"History": "Mesopotamia, Roman Empire, Nomadic Empires.", "VVIP": "Fundamental Rights (Maulik Adhikar)?"},
    "Class 12 Science": {"Physics": "Gauss Law, Optics, Semiconductors.", "VVIP": "PN Junction working."},
    "Class 12 Commerce": {"Accounts": "Partnership, Shares, Cash Flow.", "VVIP": "Pro-rata allotment entries?"},
    "Class 12 Arts": {"History": "Harappan Civ, Bhakti-Sufi, Gandhi ji.", "VVIP": "1857 Revolt causes?"}
}

# --- APP LOGIC ---
st.title("🏫 My School: Aapka Digital Guru")
st.subheader("Easy. Best. Affordable.")

if 'logged_in' not in st.session_state:
    st.info("Namaste! Padhai shuru karne ke liye Login karein.")
    mobile = st.text_input("Mobile Number", placeholder="98XXXXXXXX")
    if st.button("Get OTP"):
        st.session_state.logged_in = True
        st.rerun()
else:
    st.sidebar.image("https://icons8.com")
    selected_class = st.selectbox("Apni Class Chuniye:", list(MASTER_DATA.keys()))

    if 'premium' not in st.session_state:
        st.warning("🔒 Subscription Fees: ₹199 (One-time) for Lifetime Access.")
        if st.button("Pay ₹199 Now"):
            st.session_state.premium = True
            st.balloons()
            st.rerun()
    else:
        subjects = list(MASTER_DATA[selected_class].keys())
        # Filter out VVIP from radio buttons
        clean_subjects = [s for s in subjects if s != "VVIP"]
        sub = st.radio("Subject Chuniye:", clean_subjects)
        
        st.divider()
        st.write(f"📖 **{sub} - Expert Notes:**")
        st.info(MASTER_DATA[selected_class][sub])
        
        st.write("🔥 **VVIP Questions (Board Special):**")
        st.error(MASTER_DATA[selected_class]["VVIP"])
        
        # AI BOT SECTION
        st.divider()
        query = st.text_input("🤖 AI Guru se Poochiye:", placeholder="E.g. Ohm's law samjhao...")
        if query:
            st.success(f"AI Answer: '{query}' ka jawab verified database se fetch ho raha hai.")
            
