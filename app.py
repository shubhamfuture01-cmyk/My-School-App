import streamlit as st

# --- APP CONFIG ---
st.set_page_config(page_title="My School - Full Textbook", page_icon="📚", layout="wide")

# --- CUSTOM CSS (Book Reading Style) ---
st.markdown("""
    <style>
    .stApp { background-color: #ffffff; }
    .book-page { 
        background-color: #fffdf5; 
        padding: 40px; 
        border: 1px solid #e0d7c1; 
        border-radius: 5px; 
        box-shadow: 5px 5px 15px rgba(0,0,0,0.05);
        font-family: 'Georgia', serif;
        line-height: 1.8;
        color: #2d2d2d;
    }
    h1, h2 { color: #1e3d59 !important; text-align: center; }
    .highlight { background-color: #fff3cd; font-weight: bold; padding: 2px 5px; }
    </style>
    """, unsafe_allow_html=True)

# --- THE DEEP DATABASE (Class 6 & 9 Detailed Material) ---
FULL_TEXTBOOK_DATA = {
    "Class 6": {
        "Science": {
            "Chapter 1: Components of Food": """
            ## Chapter 1: Components of Food (Pura Lesson)
            
            **Prakritik Nutrient (Poshak Tatva):** 
            Hum jo khana khate hain, usme sharir ke liye zaroori kuch khaas cheezein hoti hain jinhe 'Nutrients' kehte hain. 
            
            **1. Carbohydrates:** 
            Ye hamare sharir ko <span class='highlight'>Energy (Urja)</span> dete hain. Ye mukhya roop se Starch aur Sugar ke roop mein milte hain. 
            *Parchan (Test):* Agar khane par Iodine solution dalne se wo 'Blue-Black' ho jaye, toh usme Starch hai.
            
            **2. Proteins:** 
            Inhe <span class='highlight'>Body Building Foods</span> kehte hain. Ye sharir ki rammmat (repair) aur growth ke liye zaroori hain. 
            *Sources:* Dal, Dudh, Anda, Machhli.
            
            **3. Fats:** 
            Ye carbohydrates se bhi zyada energy dete hain. Butter, Ghee, aur Tel iske mukhya source hain.
            
            **4. Vitamins & Minerals:** 
            Ye sharir ko bimariyon se bachate hain. Vitamin A aankhon ke liye, Vitamin C immunity ke liye aur Vitamin D haddiyon (bones) ke liye zaroori hai.
            
            **Balanced Diet (Santulit Aahar):** 
            Wo khana jisme saare nutrients, roughage aur pani sahi matra mein hon. Isse sharir swasth rehta hai.
            """,
            "Chapter 2: Electricity & Circuits": """
            ## Chapter 2: Electricity & Circuits
            
            **Electric Cell:** 
            Ye bijli ka ek source hai. Iske do terminal hote hain: **Positive (+)** aur **Negative (-)**. Cell ke andar chemicals hote hain jo bijli banate hain.
            
            **Electric Bulb:** 
            Bulb ke andar ek patla taar hota hai jise <span class='highlight'>Filament</span> kehte hain. Jab bijli isse guzarti hai, toh ye chamakne lagta hai.
            
            **Electric Circuit:** 
            Bijli ke behene ka poora rasta 'Circuit' kehlata hai. Bijli hamesha Positive se Negative terminal ki taraf behti hai.
            
            **Switch:** 
            Ye ek simple device hai jo circuit ko todne (Off) ya jodne (On) ke kaam aata hai.
            
            **Conductors vs Insulators:** 
            - **Conductors:** Wo cheezein jo bijli ko guzarne dein (Iron, Copper, Silver).
            - **Insulators:** Wo jo bijli ko rokein (Rubber, Plastic, Wood).
            """
        },
        "Maths": {
            "Chapter 1: Number Systems": "Detailed Math content with formulas..."
        }
    },
    "Class 9": {
        "Science": {
            "Chapter 1: Cell - The Unit of Life": """
            ## Chapter 1: The Fundamental Unit of Life
            
            **Discovery:** 
            Cell ki khoj <span class='highlight'>Robert Hooke</span> ne 1665 mein ki thi. Unhone cork ke ek patle tukde mein 'Madhumakkhi ke chatte' jaise chote kamre dekhe.
            
            **Cell Theory:** 
            Schleiden aur Schwann ne bataya ki saare plants aur animals cells se bane hain. Cells hi jeevan ki buniyadi ikai (basic unit) hain.
            
            **Cell ke Mukhya Hisse (Organelles):**
            1. **Plasma Membrane:** Ye cell ki outer boundary hai jo sirf zaroori cheezon ko andar-bahar jane deti hai.
            2. **Nucleus:** Isse 'Cell ka Brain' kehte hain. Isme DNA hota hai jo genetic information rakhta hai.
            3. **Cytoplasm:** Cell ke andar ka jelly-jaisa hissa.
            4. **Mitochondria:** Inhe <span class='highlight'>Powerhouse of the Cell</span> kehte hain kyunki ye ATP ke roop mein energy banate hain.
            5. **Lysosomes:** Inhe 'Suicide Bags' kehte hain kyunki ye cell ke kachre ko saaf karte hain.
            
            **Plant Cell vs Animal Cell:**
            Plant cells mein 'Cell Wall' aur 'Chloroplast' (khana banane ke liye) hota hai, jo animal cells mein nahi hota.
            """
        }
    }
}

# --- APP LOGIC ---
st.title("🏫 My School: Digital Textbook Edition")
st.write("---")

if 'logged_in' not in st.session_state:
    st.markdown("### 🔐 Student Login")
    if st.button("Open My School"):
        st.session_state.logged_in = True
        st.rerun()
else:
    # Sidebar selection
    st.sidebar.header("Library")
    sel_class = st.sidebar.selectbox("Class Chuniye:", ["Class 6", "Class 9"])
    subjects = list(FULL_TEXTBOOK_DATA[sel_class].keys())
    sel_sub = st.sidebar.radio("Subject:", subjects)
    
    chapters = list(FULL_TEXTBOOK_DATA[sel_class][sel_sub].keys())
    sel_ch = st.sidebar.selectbox("Chapter Chuniye:", chapters)

    # Main Reading Area
    st.markdown(f"<div class='book-page'>{FULL_TEXTBOOK_DATA[sel_class][sel_sub][sel_ch]}</div>", unsafe_allow_html=True)
    
    # AI Support
    st.write("---")
    q = st.text_input("🤖 AI Guru: Is chapter mein kuch samajh nahi aaya?")
    if q:
        st.info(f"AI Guru is explaining: '{q}'. (Ye feature agle update mein aur bada hoga!)")

st.caption("Success! Aapka 'Full Textbook' structure taiyaar hai.")
