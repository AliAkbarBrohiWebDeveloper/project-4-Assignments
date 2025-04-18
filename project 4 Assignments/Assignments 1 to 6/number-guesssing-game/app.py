import streamlit as st
import random

# Initialize session state variables if they don't exist
if "random_number" not in st.session_state:
    st.session_state.random_number = random.randint(1, 10)

if "attempts" not in st.session_state:
    st.session_state.attempts = 0

# Page setup
st.set_page_config(page_title="Guess the Number", page_icon="🎲", layout="centered")

# Custom CSS styling
st.markdown(
    """
    <style>
    body {
        background-color: blue;
        font-family: Arial;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and Instructions
st.markdown("<h1 style='text-align:center;color:black;'>Guess The Number Game 🎲</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center;color:#4388ab;'>Guess a Number between 1-10</h4>", unsafe_allow_html=True)

# User input for guess
user_guess = st.number_input("Enter your Guess:", min_value=1, max_value=10, step=1)

# Check Guess button
if st.button("Check Guess"):
    st.session_state.attempts += 1
    if user_guess == st.session_state.random_number:
        st.success(f"Congratulations! You guessed the correct number in {st.session_state.attempts} attempts.")
        # Reset for a new round
        st.session_state.random_number = random.randint(1, 10)
        st.session_state.attempts = 0
    else:
        st.error("Incorrect guess: Please try again.")
