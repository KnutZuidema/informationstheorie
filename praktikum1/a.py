import math


def Z_statistik(text_file):
    # Schritt 1: Öffnen und lesen der Textdatei
    with open(text_file, 'r', encoding='utf-8') as file:
        text = file.read()

    # Schritt 2: Zählen der Häufigkeit der Zeichen im Text
    total = len(text)
    counts = {}
    for char in text:
        counts[char] = counts.get(char, 0) + 1

    # Schritt 3: Berechnen der Wahrscheinlichkeiten für jedes Zeichen
    probabilities = {char: count / total for char, count in counts.items()}

    # Schritt 4: Berechnen des Informationsgehalts für jedes Zeichen
    information = {char: -math.log2(prob) for char, prob in probabilities.items()}

    # Schritt 5: Berechnen der Entropie des Textes
    entropy = sum(prob * info for prob, info in zip(probabilities.values(), information.values()))

    # Schritt 6: Ausgabe der Ergebnisse
    print("Buchstabe | Wahrscheinlichkeit | Informationsgehalt")
    for char, prob, info in zip(counts.keys(), probabilities.values(), information.values()):
        print(f"{char!r:<9} | {prob:.6f}           | {info:.6f}")

    print(f"\nEntropie des Textes: {entropy:.6f}")


# Beispielaufruf der Funktion
Z_statistik("Text.txt")
