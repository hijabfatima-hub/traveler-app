# AI Travel Chatbot using Google Gemini Free API (Streamlit Cloud Compatible)
# IMPORTANT: Use secrets properly
# In Streamlit Cloud → Settings → Secrets add this:
# GOOGLE_API_KEY = "your_key_here"

import streamlit as st
import google.generativeai as genai

# --- CONFIG ---
# Correct way to load the API key from Streamlit secrets
genai.configure(api_key=st.secrets["AIzaSyCRW0d9PP08j9OepQm8oRqtT_26PRq3CKY"])

# Recommended free model from Google
model = genai.GenerativeModel("gemini-1.5-flash-002")

# --- APP UI ---
st.set_page_config(page_title="AI Travel Chatbot", page_icon="🌍", layout="wide")
st.title("🌍 AI Travel Planner (Free Gemini API)")

st.write("Enter your travel details and get a full itinerary ✈️🏨🗺️")

destination = st.text_input("Destination (City/Country)")
days = st.slider("Number of Days", 1, 14, 5)
budget = st.selectbox("Budget Level", ["Low", "Medium", "High"])

if st.button("Generate Travel Plan"):
    if not destination:
        st.error("Please enter a destination.")
    else:
        with st.spinner("Creating your travel plan..."):
            prompt = f"""
            Create a complete travel plan.
            Destination: {destination}
            Days: {days}
            Budget: {budget}

            Include:
            - Total budget estimate
            - Best seasons to visit
            - 6–10 places to visit with short descriptions
            - A full day-wise itinerary for {days} days
            - 3 hotel suggestions (budget, mid-range, luxury)
            - Safety tips & travel tips
            Format clean and readable.
            """

            response = model.generate_content(prompt)
            st.success("Your Trip Plan is Ready!")
            st.write(response.text)

st.markdown("---")
st.caption("Made with Google Gemini Free API + Streamlit")


