import streamlit as st
import requests

API_URL = "http://localhost:8000/plan"  # Adjust if FastAPI runs elsewhere

st.title("🗺️ Local Explorer Assistant")
st.markdown("Plan your personalized day trip with AI.")

with st.form("trip_form"):
    location = st.text_input("City you’ll be exploring:", "Barcelona")
    interests = st.text_input("Your interests (comma-separated):", "architecture, local food")
    duration = st.slider("Available time (in hours):", 1.0, 12.0, 6.0)
    avoid = st.text_input("Things to avoid (comma-separated, optional):", "crowds")
    submitted = st.form_submit_button("Plan My Trip")

if submitted:
    with st.spinner("Contacting your travel assistant..."):
        try:
            payload = {
                "location": location,
                "interests": [i.strip() for i in interests.split(",") if i.strip()],
                "duration_hours": duration,
                "avoid": [a.strip() for a in avoid.split(",") if a.strip()] if avoid else []
            }
            response = requests.post(API_URL, json=payload)
            if response.status_code == 200:
                itinerary = response.json().get("itinerary", "No response from agent.")
                st.success("Here's your local exploration plan:")
                st.markdown(itinerary, unsafe_allow_html=True)
            else:
                st.error(f"Error: {response.status_code} - {response.text}")
        except Exception as e:
            st.error(f"Request failed: {e}")