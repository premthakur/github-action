import streamlit as st

st.title("Simple Streamlit App")
st.write("Welcome to my simple Streamlit app!")

if st.button("Say hello"):
    st.write("Hello, Streamlit!")
else:
    st.write("Goodbye, Streamlit!")
