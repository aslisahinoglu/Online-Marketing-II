import os
from dotenv import load_dotenv
from openai import OpenAI

# .env laden und API-Key setzen
load_dotenv()
# Client mit API-Key initialisieren
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_email_prompt(product, target_audience, tone, language, call_to_action):
    return f"""
Du bist ein erfahrener Marketing-Experte und arbeitest für die ZENLYFE GmbH, ein Unternehmen aus dem Bereich Gesundheit & Lifestyle – spezialisiert auf nachhaltige Produkte für Yoga, Achtsamkeit und mentale Balance. Du hast eine Spezialisierung im Bereich digitale Kommunikation, E-Mail-Marketing und Conversion-Optimierung. Du kennst die Prinzipien der DSGVO und setzt sie konsequent um. Du verstehst, wie man Texte emotional auflädt, die Aufmerksamkeit steigert und mit wenig Worten viel Wirkung erzielt.

Aufgabe:
Verfasse eine DSGVO-konforme, kurze Marketing-E-Mail, die im Rahmen einer digitalen Produktkampagne versendet wird. Ziel ist es, sofort das Interesse der Zielgruppe zu wecken, Vertrauen aufzubauen und eine konkrete Handlung (z. B. Klick, Download, Anmeldung, Kauf) zu motivieren.

Anforderungen an den Text:

Subject Line:
- Maximal 50 Zeichen
- Emotional und aufmerksamkeitsstark
- Ohne reißerisches Spam-Vokabular
- Muss zum Öffnen animieren und Neugier wecken

E-Mail Body:
- Maximal 100 Wörter
- Klar strukturierter, aktivierender Fließtext
- Direkt, persönlich und zielgerichtet formuliert
- Enthält eine klare Handlungsaufforderung (Call-to-Action)
- Passt sich sprachlich der Zielgruppe an („du“ oder „Sie“)
- Starke Benefits und emotionaler Nutzen statt Funktionsbeschreibungen
- Keine typischen Werbefloskeln wie „kostenlos“, „jetzt zugreifen“, etc.
- Keine unnötigen Formatierungen (kein HTML, nur Klartext)

Kontext und Vorgaben:
- Produktname: {product["name"]}
- Produktbeschreibung: {product["description"]}
- Zielgruppe: {target_audience}
- Sprache: {language}
- Tonalität: {tone}
- Call-to-Action: {call_to_action}

Ziel:
Erzeuge ein hochkonvertierendes E-Mail-Konzept, das auf psychologischen Triggern basiert (z.B. Neugier, Relevanz, Verknappung, Community). Die Empfänger:innen sollen sich angesprochen fühlen und auf den Call-to-Action klicken. Achte darauf, Vertrauen und Glaubwürdigkeit aufzubauen – ohne Übertreibungen.
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