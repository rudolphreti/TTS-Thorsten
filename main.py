from TTS.api import TTS
from text_cleaner import clean_text_for_tts

# Lade das Thorsten-Modell direkt
tts = TTS(model_name="tts_models/de/thorsten/tacotron2-DDC", gpu=False)

# Text aus Datei lesen
with open("input.txt", "r", encoding="utf-8") as file:
    german_text = file.read()

# Text für TTS bereinigen
german_text = clean_text_for_tts(german_text)

# Erstelle eine Audioausgabe
output_path = "output.wav"
tts.tts_to_file(text=german_text, file_path=output_path)

print(f"Audio gespeichert unter: {output_path}")
print(f"Bereinigter Text (Anfang): {german_text[:100]}...")