import streamlit as st
import os

# 1. Setup 'Memory'
if 'size' not in st.session_state:
    st.session_state.size = 20
if 'count' not in st.session_state:
    st.session_state.count = 0
if 'yes_clicked' not in st.session_state:
    st.session_state.yes_clicked = False

# --- THE "WHITE GLOW" SCREEN ---
# --- THE "WHITE GLOW" SCREEN WITH KISS GIFS ---
# --- THE "WHITE GLOW" SCREEN WITH LOCAL GIF ---
import time

if st.session_state.yes_clicked:
    # 1. Show the animation
    placeholder = st.empty() # Create a blank space
    
    with placeholder.container():
        st.markdown("<h1 style='text-align: center;'>❤️</h1>", unsafe_allow_html=True)
        # Use your local path here
        st.image("kiss.gif", use_container_width=True)
    
    # 2. Wait for the duration of the animation (e.g., 3 seconds)
    time.sleep(3)
    
    # 3. Clear the GIF so it doesn't loop
    placeholder.empty()
    
    # 4. Show a final still message or image
    st.markdown("<h1 style='text-align: center;'>I love you!</h1>", unsafe_allow_html=True)
    st.stop()

# --- NORMAL SCREEN (BEFORE CLICKING YES) ---
st.title("Will you be my Valentine? 🌹")

# Load your main image
base_path = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(base_path, "main_image.gif")

if os.path.exists(image_path):
    st.image(image_path, use_container_width=True)

col1, col2 = st.columns([1, 1])

with col1:
    if st.button("Yes", key="yes_btn"):
        st.session_state.yes_clicked = True
        st.rerun()

with col2:
    phrases = ["No", "Are you sure?", "Really sure??", "Think again!", "Last chance!"]
    current_text = phrases[min(st.session_state.count, len(phrases)-1)]
    if st.button(current_text):
        st.session_state.count += 1
        st.session_state.size += 15
        st.rerun()

# Growing button CSS
# 4. Updated CSS for button sizes and colors
st.markdown(f"""
    <style>
    /* Target the 'Yes' button (First column) */
    div.stColumn:nth-of-type(1) button {{
        background-color: #FF0000 !important; /* Red */
        color: white !important;
        font-size: {st.session_state.size}px !important;
        padding: {st.session_state.size/2}px {st.session_state.size}px !important;
        border: none !important;
    }}

    /* Target the 'No' button (Second column) */
    div.stColumn:nth-of-type(2) button {{
        background-color: #000000 !important; /* Black */
        color: white !important;
        border: 1px solid white !important;
    }}
    
    /* Optional: Change hover effect so they don't turn grey */
    div.stColumn:nth-of-type(1) button:hover {{
        background-color: #CC0000 !important; /* Darker Red on hover */
        border: 1px solid white !important;
    }}
    </style>
    """, unsafe_allow_html=True)