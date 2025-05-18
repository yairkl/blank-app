import streamlit as st

st.title("File Uploader bug reproduce")
file = st.file_uploader("Upload file...")
if file:
    st.write(file.name)