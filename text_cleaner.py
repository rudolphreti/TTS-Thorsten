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

    # Gedankenstriche in Kommas umwandeln
    text = text.replace('–', ',')
    text = text.replace('—', ',')
    text = text.replace('-', ',')
    
    # Andere potenziell problematische Sonderzeichen bereinigen
    problematic_chars = ['\\', '/', '*', '|']
    for char in problematic_chars:
        text = text.replace(char, "")

    # Vor "sowie" ein Komma einfügen, wenn davor kein Komma steht
    text = re.sub(r'([^,])\s+sowie', r'\1, sowie', text)
    
    # Zeilen verarbeiten (statt Absätze)
    lines = text.split('\n')
    processed_lines = []
    
    for line in lines:
        line = line.strip()
        if line:  # Nur nicht-leere Zeilen verarbeiten
            # Prüfen, ob die Zeile bereits mit einem Punkt endet
            if not line.endswith('.') and not line.endswith('!') and not line.endswith('?'):
                line += '.'
            processed_lines.append(line)
    
    # Jede Zeile wird ein separater Satz
    processed_text = ' '.join(processed_lines)
    
    # Mehrfache Leerzeichen durch ein einzelnes ersetzen
    processed_text = re.sub(r'\s+', ' ', processed_text)
    
    return processed_text.strip()