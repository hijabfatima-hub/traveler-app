import streamlit as st

# ---- APP CONFIG ----
st.set_page_config(page_title="Simple Travel Chatbot", page_icon="🌍", layout="wide")
st.title("🌍 Offline Travel Planner (No API Key Needed)")
st.write("This chatbot gives simple travel suggestions without using any AI model or API.")

# ---- INPUTS ----
destination = st.text_input("Destination (City/Country)")
days = st.slider("Number of Days", 1, 14, 5)
budget = st.selectbox("Budget Level", ["Low", "Medium", "High"])

# ---- SIMPLE DATA (RULE BASED) ----
places = {
    "dubai": ["Burj Khalifa", "Dubai Mall", "Desert Safari", "Palm Jumeirah", "Global Village"],
    "turkey": ["Hagia Sophia", "Blue Mosque", "Cappadocia", "Antalya Beach", "Pamukkale"],
    "saudi": ["Kaaba (Makkah)", "Madina Masjid-e-Nabwi", "Riyadh Kingdom Tower", "Jeddah Corniche"],
    "malaysia": ["Petronas Towers", "Langkawi", "Batu Caves", "Genting Highlands", "Kuala Lumpur Tower"],
}

budget_estimate = {
    "Low": "Around $300 – $500",
    "Medium": "Around $600 – $1200",
    "High": "Above $1500",
}

best_season = {
    "dubai": "November to March",
    "turkey": "April to June & September to November",
    "saudi": "October to March",
    "malaysia": "March to October",
}

# ---- GENERATE TRAVEL PLAN ----
if st.button("Generate Travel Plan"):
    if not destination:
        st.error("Please enter a destination.")
    else:
        dest = destination.lower()

        st.success(f"Here is your travel plan for **{destination}**")

        # Budget
        st.subheader("💰 Estimated Budget")
        st.write(budget_estimate[budget])

        # Best Season
        st.subheader("🌤 Best Time to Visit")
        st.write(best_season.get(dest, "Best time varies by location."))

        # Places
        st.subheader("📍 Top Places to Visit")
        if dest in places:
            for p in places[dest]:
                st.write(f"- {p}")
        else:
            st.write("Top places list not available for this destination.")

        # Simple Itinerary
        st.subheader("🗓 Day-wise Itinerary")
        for i in range(1, days + 1):
            st.write(f"**Day {i}:** Explore local attractions, food, and markets.")

        st.subheader("🛏 Hotel Suggestions")
        st.write("""
        - Budget Hotel
        - Mid-range Hotel
        - Luxury Hotel
        """)

st.markdown("---")
st.caption("Simple rule-based Travel Chatbot — No API, No Cost!")

