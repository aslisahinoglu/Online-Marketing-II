import os
from dotenv import load_dotenv
from openai import OpenAI

# .env laden und API-Key setzen
load_dotenv()
# Client mit API-Key initialisieren
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_email_prompt(product, target_audience, tone, language, call_to_action):
    return f"""
    Du bist ein Marketing-Experte. Schreibe eine kurze, effektive Marketing-E-Mail für folgendes Produkt:

    Produkt: {product["name"]}
    Beschreibung: {product["description"]}

    Zielgruppe: {target_audience}
    Sprache: {language}
    Tonalität: {tone}
    Call-to-Action: {call_to_action}

    Die E-Mail soll eine hohe Öffnungsrate erzielen. Gib:
    - Subject Line
    - Email Body

    Schreibe DSGVO-konform und vermeide Spam-Wörter.
    """

def generate_email(product, target_audience, tone, language, call_to_action):
    prompt = generate_email_prompt(product, target_audience, tone, language, call_to_action)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=700
    )

    return response.choices[0].message.content

def generate_image_prompt(product, target_audience):
    return f"Erstelle einen Bild-Prompt für ein Produktfoto von {product['name']} für die Zielgruppe {target_audience}."