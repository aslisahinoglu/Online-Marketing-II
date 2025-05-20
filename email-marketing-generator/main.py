import streamlit as st
from app.generator import generate_email
from app.data import products
from app.utils import tonalitaets_feedback

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

    if st.button("Als Text speichern"):
        with open("generated_email.txt", "w") as f:
            f.write(st.session_state.result)
        st.success("E-Mail als Text gespeichert!")

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
