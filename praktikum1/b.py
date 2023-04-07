import math


def Z2_statistik(text_file):
    # Schritt 1: Öffnen und lesen der Textdatei
    with open(text_file, 'r', encoding='utf-8') as file:
        text = file.read()

    # Schritt 2: Zählen der Häufigkeit der 2er Tupel im Text
    total = len(text) - 1
    counts = {}
    for tuple in zip(text, text[1:]):
        counts[tuple] = counts.get(tuple, 0) + 1

    # Schritt 3: Berechnen der Wahrscheinlichkeiten für jedes 2er Tupel
    probabilities = {char: count / total for char, count in counts.items()}

    # Schritt 4: Berechnen des Informationsgehalts für jedes 2er Tupel
    information = {char: -math.log2(prob) for char, prob in probabilities.items()}

    # Schritt 5: Berechnen der Entropie des Textes
    entropy = sum(prob * info for prob, info in zip(probabilities.values(), information.values()))

    # Schritt 6: Ausgabe der Ergebnisse
    print("2er Tupel   | Wahrscheinlichkeit | Informationsgehalt")
    for tuple, prob, info in zip(counts.keys(), probabilities.values(), information.values()):
        print(f"{tuple!r:<11} | {prob:.6f}           | {info:.6f}")

    print(f"\nEntropie des Textes: {entropy:.6f}")


# Beispielaufruf der Funktion
Z2_statistik("Text.txt")
