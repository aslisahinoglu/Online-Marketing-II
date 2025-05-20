import streamlit as st
from app.generator import generate_email
from app.data import products
from app.utils import tonalitaets_feedback
from datetime import datetime
import re

st.title("📧 Personalized Email Generator")

product_name = st.selectbox("Produkt auswählen", list(products.keys()))
product = products[product_name]

target = st.selectbox("Zielgruppe", ["Neukunden", "Bestandskunden", "Inaktive Nutzer"])
tone = st.selectbox("Tonalität", ["locker", "neutral", "förmlich"])
language = st.selectbox("Sprache", ["Deutsch", "Englisch"])
cta = st.text_input("Call-to-Action", "Jetzt ausprobieren")

if "result" not in st.session_state:
    st.session_state.result = ""

if st.button("E-Mail generieren"):
    st.session_state.result = generate_email(product, target, tone, language, cta)

if st.session_state.result:
    st.markdown("### ✉️ Ergebnis:")
    st.code(st.session_state.result, language="markdown")

    feedback = tonalitaets_feedback(st.session_state.result)
    st.write("Ton-Feedback:", feedback)

    st.text_area("E-Mail Text zum Kopieren", value=st.session_state.result, height=300)

    # Subject line extrahieren
    match = re.search(r"Subject Line:\s*(.+)", st.session_state.result)
    subject_line = match.group(1).strip() if match else "email"

    # Dateiname mit Datum und Subject
    date_str = datetime.now().strftime("%Y-%m-%d")
    filename = f"{date_str}_{subject_line}.txt"
    # Dateiname safe machen (keine Sonderzeichen)
    filename = re.sub(r'[\\/*?:"<>|]', "", filename)

    st.download_button(
        label="Als Text herunterladen",
        data=st.session_state.result,
        file_name=filename,
        mime="text/plain"
    )

if st.button("A/B Test generieren"):
    email_a = generate_email(product, target, "locker", language, cta)
    email_b = generate_email(product, target, "förmlich", language, cta)
    st.markdown("### Variante A (locker)")
    st.code(email_a)
    st.markdown("### Variante B (förmlich)")
    st.code(email_b)

from app.generator import generate_image_prompt

if st.button("Bild-Prompt generieren"):
    image_prompt = generate_image_prompt(product, target)
    st.markdown("### 🖼️ Bild-Prompt")
    st.code(image_prompt)
