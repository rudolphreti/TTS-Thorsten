from TTS.api import TTS
from text_cleaner import clean_text_for_tts
import os

# Lade das Thorsten-Modell direkt
tts = TTS(model_name="tts_models/de/thorsten/tacotron2-DDC", gpu=False)

# Stelle sicher, dass der Output-Ordner existiert
output_dir = "output"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Text aus Datei lesen
with open("input.txt", "r", encoding="utf-8") as file:
    german_text = file.read()

# Text für TTS bereinigen
german_text = clean_text_for_tts(german_text)

# Erstelle eine Audioausgabe im output-Ordner
output_path = os.path.join(output_dir, "output.wav")
tts.tts_to_file(text=german_text, file_path=output_path)

print(f"Audio gespeichert unter: {output_path}")
print(f"Bereinigter Text (Anfang): {german_text[:100]}...")