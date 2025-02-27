import re

def clean_text_for_tts(text):
    """
    Bereinigt einen Text für die Verwendung mit TTS-Systemen.
    Entfernt oder ersetzt problematische Zeichen.
    """
    # Alle Arten von Anführungszeichen entfernen
    quotes = ['"', "'", "„", "‟", "'", "‘", "“"]
    for quote in quotes:
        text = text.replace(quote, "")

    # Doppelpunkte in Punkte umwandeln
    text = text.replace(':', '.')
    
    # Andere potenziell problematische Sonderzeichen bereinigen
    problematic_chars = ['\\', '/', '*', '|']
    for char in problematic_chars:
        text = text.replace(char, "")
    
    # Mehrfache Leerzeichen durch ein einzelnes ersetzen
    text = re.sub(r'\s+', ' ', text)
    
    return text.strip()