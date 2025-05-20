from dotenv import load_dotenv
import os
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

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

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=700
    )

    return response["choices"][0]["message"]["content"]
