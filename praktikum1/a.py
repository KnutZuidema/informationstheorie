import math


def Z_statistik(text):
    # Schritt 2: Zählen der Häufigkeit der Zeichen im Text
    total = len(text)
    counts = {}
    for char in text:
        counts[char] = counts.get(char, 0) + 1

    # Schritt 3: Berechnen der Wahrscheinlichkeiten für jedes Zeichen
    return {char: count / total for char, count in counts.items()}


if __name__ == '__main__':

    probabilities = Z_statistik("Dies ist ein Testtext.")

    # Schritt 4: Berechnen des Informationsgehalts für jedes Zeichen
    information = {char: -math.log2(prob) for char, prob in probabilities.items()}

    # Schritt 5: Berechnen der Entropie des Textes
    entropy = sum(probabilities[char] * information[char] for char in probabilities.keys())
    # Schritt 6: Ausgabe der Ergebnisse
    print("Buchstabe | Wahrscheinlichkeit | Informationsgehalt")
    for char in probabilities.keys():
        print(f"{char!r:<9} | {probabilities[char]:.6f}           | {information[char]:.6f}")

    print(f"\nEntropie des Textes: {entropy:.6f}")
