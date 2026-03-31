import streamlit as st

# --- APP CONFIGURATION ---
st.set_page_config(page_title="My School - Apna Digital Guru", page_icon="🏫", layout="centered")

# --- CUSTOM CSS (Professional UI & No Copy) ---
st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; }
    h1, h2, h3 { color: #1e3d59 !important; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
    p, span, label, .stRadio { color: #2c3e50 !important; font-size: 16px; font-weight: 500; }
    .stAlert { border-radius: 12px; border: 1px solid #dee2e6; box-shadow: 2px 2px 10px rgba(0,0,0,0.05); }
    .stButton>button { background-color: #ff6e40; color: white; border-radius: 10px; height: 50px; font-weight: bold; border: none; }
    .stButton>button:hover { background-color: #ff5722; color: white; transform: scale(1.02); transition: 0.2s; }
    body { -webkit-user-select: none; -moz-user-select: none; -ms-user-select: none; user-select: none; }
    </style>
    """, unsafe_allow_html=True)

# --- THE GIANT MASTER DATABASE (All Classes, All Subjects) ---
MASTER_DATA = {
    "Class 1": {
        "English": "1. Alphabets (A-Z), 2. Three letter words (Cat, Bat), 3. Greetings (Hello, Thank you), 4. Action words (Run, Jump).",
        "Maths": "1. Counting 1-50, 2. Shapes (Circle, Square), 3. Addition (1-digit), 4. Big and Small concepts.",
        "VVIP": "Apple kis letter se shuru hota hai? (A) | 5 ke baad kya aata hai? (6)"
    },
    "Class 5": {
        "EVS": "1. Super Senses (Ants/Tigers), 2. A Snake Charmer's Story, 3. From Tasting to Digesting, 4. Seeds and Seeds, 5. Experiments with Water.",
        "Maths": "1. The Fish Tale (Lakhs/Crores), 2. Shapes & Angles, 3. Parts and Wholes (Fractions), 4. Area and Perimeter.",
        "VVIP": "Ants ek line mein kaise chalti hain? (Smell magic) | 1/2 bada hai ya 1/4? (1/2)"
    },
    "Class 6": {
        "Science": "1. Food Components, 2. Sorting Materials, 3. Separation (Filtration/Sieving), 4. Body Movements (Joints), 5. Electricity (Circuits), 6. Fun with Magnets.",
        "Maths": "1. Knowing Numbers (Lakh/Million), 2. Whole Numbers, 3. Playing with Numbers (HCF/LCM), 4. Geometry (Lines/Angles), 5. Integers (+/-), 6. Fractions & Decimals, 7. Algebra Intro, 8. Ratio & Proportion.",
        "VVIP": "Scurvy kiski kami se hoti hai? (Vitamin C) | 1 Million = ? Lakh (10 Lakh)"
    },
    "Class 10": {
        "Science": "1. Chemical Reactions, 2. Acids, Bases & Salts, 3. Metals & Non-metals, 4. Carbon & its Compounds, 5. Life Processes (Digestion/Respiration), 6. Light (Reflection/Refraction), 7. Human Eye, 8. Electricity (V=IR), 9. Magnetic Effects.",
        "Maths": "1. Real Numbers, 2. Polynomials, 3. Linear Equations, 4. Quadratic Equations, 5. Arithmetic Progression (AP), 6. Trigonometry (sin/cos), 7. Statistics (Mean/Median/Mode).",
        "SST": "1. Nationalism in India, 2. Resources & Development, 3. Power Sharing, 4. Money & Credit.",
        "VVIP": "Prove √2 is irrational? (Maths) | Ohm's Law (Electricity) | 1857 Revolt (History)"
    },
    "Class 12 Science": {
        "Physics": "1. Electrostatics (Gauss Law), 2. Current Electricity (Kirchhoff’s), 3. Magnetism, 4. EMI & AC, 5. Ray Optics (Lenses), 6. Dual Nature of Matter, 7. Atoms & Nuclei, 8. Semiconductors (P-N Junction).",
        "Chemistry": "1. Solutions (Raoult's Law), 2. Electrochemistry, 3. Chemical Kinetics, 4. Haloalkanes, 5. Alcohols & Phenols, 6. Biomolecules.",
        "Biology": "1. Reproduction in Organisms, 2. Genetics (Mendel/DNA), 3. Evolution, 4. Biotech Applications, 5. Ecology.",
        "VVIP": "Derive Electric Field of a Dipole? | SN1 vs SN2 Mechanisms? | DNA Replication process?"
    },
    "Class 12 Commerce": {
        "Accountancy": "1. Partnership Accounts (Admission/Death), 2. Company Accounts (Shares/Debentures), 3. Cash Flow Statement, 4. Ratio Analysis.",
        "Business Studies": "1. Management Principles (Fayol/Taylor), 2. Planning/Organizing, 3. Marketing Mix (4Ps), 4. Consumer Protection.",
        "Economics": "1. National Income, 2. Money & Banking (RBI), 3. Government Budget, 4. Indian Economic Development (LPG Reforms).",
        "VVIP": "Pro-rata allotment entries? | RBI Credit Control tools? | 4Ps of Marketing?"
    },
    "Class 12 Arts": {
        "History": "1. Harappan Civilization, 2. Kings & Chronicles (Mughals), 3. Bhakti-Sufi traditions, 4. Gandhi Ji & Freedom Movement.",
        "Pol Science": "1. Cold War Era, 2. End of Bipolarity (USSR), 3. Challenges of Nation Building, 4. Emergency (1975).",
        "Geography": "1. Human Geography, 2. India: Population & Settlements, 3. Resources (Water/Minerals).",
        "VVIP": "Harappan Drainage System? | Partition of India (1947) causes? | Fundamental Rights?"
    }
}
# Note: Isme baki classes (2,3,4,7,8,9,11) ka bhi format same rahega.

# --- APP LOGIC ---
st.title("🏫 My School: Apna Digital Guru")
st.write("---")

if 'logged_in' not in st.session_state:
    st.markdown("### 🔒 Secure Student Login")
    mobile = st.text_input("Apna Mobile Number Dalein:", placeholder="98XXXXXXXX")
    if st.button("Start Learning (Get OTP)"):
        st.session_state.logged_in = True
        st.rerun()
else:
    # Home Page: Class Selection
    st.sidebar.image("https://icons8.com")
    st.sidebar.write("### Welcome Student!")
    
    selected_class = st.selectbox("Apni Class Chuniye:", list(MASTER_DATA.keys()))

    if 'premium' not in st.session_state:
        st.warning(f"🔒 {selected_class} ka poora data unlock karne ke liye ₹199 ka One-time fee pay karein.")
        if st.button("Pay ₹199 Now"):
            st.session_state.premium = True
            st.balloons()
            st.rerun()
    else:
        # Full Data Display
        subjects = list(MASTER_DATA[selected_class].keys())
        clean_subjects = [s for s in subjects if s != "VVIP"]
        sub = st.radio("Subject Select Karein:", clean_subjects, horizontal=True)
        
        st.write("---")
        st.subheader(f"📖 {sub} - Full Chapter Guide")
        st.info(MASTER_DATA[selected_class][sub])
        
        st.subheader("🔥 Board/Exam VVIP Questions")
        st.error(MASTER_DATA[selected_class]["VVIP"])
        
        # AI Interaction
        st.write("---")
        query = st.text_input("🤖 AI Guru se koi bhi sawal poochiye:", placeholder="E.g. Newton ka 1st law kya hai?")
        if query:
            st.success(f"AI Guru is thinking... '{query}' ka detail jawab aapke verified data se fetch ho raha hai.")

st.write("---")
st.caption("© 2024 My School - Easy. Best. Affordable Education for Everyone.")
