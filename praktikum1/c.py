import math
import re


def W_statistik(text_file):
    # Schritt 1: Öffnen und lesen der Textdatei
    with open(text_file, 'r', encoding='utf-8') as file:
        text = file.read()

    # Schritt 2: Zählen der Häufigkeit der Wörter im Text
    total = 0
    counts = {}
    for word in re.split(r'\W+', text):
        if word == '':
            continue
        counts[word] = counts.get(word, 0) + 1
        total += 1

    # Schritt 3: Berechnen der Wahrscheinlichkeiten für jedes Wörter
    probabilities = {char: count / total for char, count in counts.items()}

    # Schritt 4: Berechnen des Informationsgehalts für jedes Wörter
    information = {char: -math.log2(prob) for char, prob in probabilities.items()}

    # Schritt 5: Berechnen der Entropie des Textes
    entropy = sum(prob * info for prob, info in zip(probabilities.values(), information.values()))

    # Schritt 6: Ausgabe der Ergebnisse
    longest_word = max(len(word) for word in counts.keys())
    print(f"{'Wörter':<{longest_word}} | Wahrscheinlichkeit | Informationsgehalt")
    for word, prob, info in zip(counts.keys(), probabilities.values(), information.values()):
        print(f"{word:<{longest_word}} | {prob:.6f}           | {info:.6f}")

    print(f"\nEntropie des Textes: {entropy:.6f}")


# Beispielaufruf der Funktion
W_statistik("Text.txt")
