import streamlit as st
import pandas as pd

# Set the title of the app
st.title("My Streamlit Web App")

# Display some simple text
st.write("Hello! Welcome to my Streamlit web app!")

# Create a text input box for user input
name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name}!")

# Display a simple DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'London', 'Tokyo']}
df = pd.DataFrame(data)

st.write("Here is some sample data:")
st.dataframe(df)
