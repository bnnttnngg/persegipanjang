import streamlit as st

with st.form("myform"):
    st.title("persegi panjang")
    panjang = st.text_input("panjang")
    lebar = st.text_input("lebar")
    button = st.form_submit_button()

    if button:
        st.text(f"Panjang Persegi panjang adalah {int(panjang)*int(lebar)}")