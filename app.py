import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets["AIzaSyDPPXRc2mK3OBtrKixpoMNXqJhrpJI2wWQ"])

model = genai.GenerativeModel("gemini-1.5-flash")

prompt = st.text_input("traveling app")

if st.button("Run"):
    response = model.generate_content(prompt)
    st.write(response.text)

