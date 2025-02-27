# TTS-Thorsten

Ein Python-Tool zur Text-zu-Sprache-Umwandlung mit dem deutschen Thorsten-TTS-Modell.

## Übersicht

Dieses Projekt bietet eine einfache Möglichkeit, deutsche Texte in natürlich klingende Sprache umzuwandeln. Es verwendet das Thorsten-TTS-Modell, das speziell für die deutsche Sprache trainiert wurde.

## Funktionen

- Einlesen von Texten aus Dateien
- Automatische Bereinigung problematischer Zeichen für bessere TTS-Ergebnisse
- Umwandlung von Text in Audiodateien
- Speicherung der Ausgabe in einem dedizierten Ordner

## Installation

1. Klone dieses Repository:
   ```
   git clone https://github.com/rudolphreti/TTS-Thorsten.git
   cd TTS-Thorsten
   ```

2. Installiere die benötigten Abhängigkeiten:
   ```
   pip install TTS
   ```

## Verwendung

### Grundlegende Verwendung

```
python main.py
```

Dieses Kommando liest den Text aus `input.txt`, bereinigt ihn und erstellt eine Audiodatei `output/output.wav`.

### Konfiguration

- `input.txt`: Enthält den zu sprechenden Text
- `output/output.wav`: Die erzeugte Audiodatei im Output-Ordner

## Projektstruktur

- `main.py`: Hauptskript zur Textumwandlung
- `text_cleaner.py`: Modul zur Bereinigung problematischer Zeichen
- `input.txt`: Eingabetext
- `output/`: Ordner für alle erzeugten Audiodateien (wird in .gitignore ausgeschlossen)
- `.gitignore`: Definiert Dateien und Ordner, die nicht ins Git-Repository aufgenommen werden
- `README.md`: Diese Dokumentation

## Textbereinigung

Das Tool entfernt automatisch potentiell problematische Zeichen für TTS-Systeme, einschließlich:

- Verschiedene Arten von Anführungszeichen (deutsch, englisch, typografisch)
- Nicht-standardisierte Gedankenstriche und Ellipsen
- Andere Sonderzeichen, die zu Problemen führen können

Diese Bereinigung verbessert die Qualität und Zuverlässigkeit der Sprachausgabe erheblich.

## Beispiel

1. Füge deinen Text in die Datei `input.txt` ein:
   ```
   Übermäßig spät äußerte Jörg seinen größten Ärger über die völlig überraschende Maßnahme.
   ```

2. Führe das Skript aus:
   ```
   python main.py
   ```

3. Die Audiodatei `output/output.wav` wird erstellt und enthält die gesprochene Version des Textes.

## Erweiterte Anpassung

Du kannst die Bereinigungsfunktionen in `text_cleaner.py` anpassen, um zusätzliche Zeichen zu entfernen oder zu ersetzen, je nach deinen spezifischen Anforderungen.

## Lizenz

MIT

## Danksagung

Dieses Projekt nutzt:
- [Thorsten TTS](https://github.com/thorstenMueller/Thorsten-Voice) - Das deutsche TTS-Modell von Thorsten Müller
- [Coqui TTS](https://github.com/coqui-ai/TTS) - Das TTS-Framework