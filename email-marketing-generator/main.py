import streamlit as st
from app.generator import generate_email

product = {
    "name": "ZENLYFE Eco Yoga Mat",
    "description": "Nachhaltige Yogamatte aus Naturkautschuk. Rutschfest, biologisch abbaubar, für Allergiker geeignet."
}

st.title("📧 Personalized Email Generator")

target = st.selectbox("Zielgruppe", ["Neukunden", "Bestandskunden", "Inaktive Nutzer"])
tone = st.selectbox("Tonalität", ["locker", "neutral", "förmlich"])
language = st.selectbox("Sprache", ["Deutsch", "Englisch"])
cta = st.text_input("Call-to-Action", "Jetzt ausprobieren")

if st.button("E-Mail generieren"):
    result = generate_email(product, target, tone, language, cta)
    st.markdown("### ✉️ Ergebnis:")
    st.code(result, language="markdown")
    
