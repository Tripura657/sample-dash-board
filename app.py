import streamlit as st

# Set page config (must be first)
st.set_page_config(page_title="Mental Health App", layout="wide")

# Initialize session state for navigation
if "page" not in st.session_state:
    st.session_state.page = "home"

# Custom CSS for styling
st.markdown("""
    <style>
    .tile {
        background-color: #262730;
        padding: 30px;
        border-radius: 15px;
        text-align: center;
        color: white;
        cursor: pointer;
        transition: 0.3s;
    }
    .tile:hover {
        background-color: #1f77b4;
        transform: scale(1.05);
    }
    .tile img {
        width: 100px;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# --- HOMEPAGE ---
if st.session_state.page == "home":
    st.markdown("<h1 style='text-align: center;'>🌈 Welcome to Your Mental Wellness Dashboard</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)

    with col1:
        
        st.markdown('<div class="tile"><img src="https://cdn-icons-png.flaticon.com/512/4712/4712036.png"><p>Chatbot</p></div>', unsafe_allow_html=True)

    with col2:
        
        st.markdown('<div class="tile"><img src="https://cdn-icons-png.flaticon.com/512/1687/1687363.png"><p>Virtual Hug</p></div>', unsafe_allow_html=True)

    with col3:
        
        st.markdown('<div class="tile"><img src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png"><p>Story</p></div>', unsafe_allow_html=True)

    col4, col5 = st.columns(2)

    with col4:
        
        st.markdown('<div class="tile"><img src="https://cdn-icons-png.flaticon.com/512/1995/1995533.png"><p>Character Talk</p></div>', unsafe_allow_html=True)

    with col5:
        
        st.markdown('<div class="tile"><img src="https://cdn-icons-png.flaticon.com/512/3565/3565418.png"><p>Bubble Game</p></div>', unsafe_allow_html=True)

# --- MODULE PAGES ---
elif st.session_state.page == "chatbot":
    st.title("💬 Chatbot")
    st.write("This is the chatbot module.")
    if st.button("🔙 Back to Home"):
        st.session_state.page = "home"

elif st.session_state.page == "hug":
    st.title("🤗 Virtual Hug")
    st.write("Here's a cozy hug for you!")
    st.image("https://media.giphy.com/media/l2QDM9Jnim1YVILXa/giphy.gif")
    if st.button("🔙 Back to Home"):
        st.session_state.page = "home"

elif st.session_state.page == "story":
    st.title("📖 Motivational Story")
    st.write("Once upon a time...")
    if st.button("🔙 Back to Home"):
        st.session_state.page = "home"

elif st.session_state.page == "character":
    st.title("🎭 Character Talk")
    character = st.selectbox("Choose a character:", ["Harry Potter", "Iron Man", "Sherlock Holmes"])
    msg = st.text_input(f"What do you want to tell {character}?")
    if msg:
        st.write(f"🧙 {character} says: 'Thank you for sharing that!'")
    if st.button("🔙 Back to Home"):
        st.session_state.page = "home"

elif st.session_state.page == "bubble":
    st.title("🫧 Bubble Game")
    st.write("Pop your negative thoughts away!")
    if st.button("🔙 Back to Home"):
        st.session_state.page = "home"
