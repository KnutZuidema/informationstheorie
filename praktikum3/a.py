from praktikum1.a import Z_statistik


def Q_Fanoencoder(text: str, probabilities: dict[str, float]):
    # Schritt 1: Sortiere die Symbol nach absteigender Wahrscheinlichkeit
    probabilities = dict_to_sorted_list(probabilities)

    # Schritt 2: Erstellen der Lookup-Tabelle
    lookup_table = create_lookup_table(probabilities)

    # Schritt 3: Codiere den Text mit der Lookup-Tabelle
    encoded_string = ''.join(lookup_table[symbol] for symbol in text)

    # Schritt 4: Konvertiere die binäre Folge in einen String
    result = binary_string_to_string(encoded_string)

    return result


def dict_to_sorted_list(dictionary: dict[str, float]) -> list[tuple[str, float]]:
    # Erstelle eine Liste von Tupeln (Symbol, Wahrscheinlichkeit)
    probabilities = list(dictionary.items())
    # Sortiere die Symbole nach absteigender Wahrscheinlichkeit
    probabilities.sort(key=lambda x: x[1], reverse=True)
    return probabilities


def split_by_probability(probabilities: list[tuple[str, float]]) -> tuple[list, list]:
    # Finde den Punkt, an dem das Gewicht der Wahrscheinlichkeiten ungefähr halbiert wird
    total_probability = sum(prob for _, prob in probabilities)
    half_probability = total_probability / 2
    cumulative_probability = 0
    split_index = 0

    for i, (_, prob) in enumerate(probabilities):
        cumulative_probability += prob
        if cumulative_probability >= half_probability:
            split_index = i
            break

    # Teile die Symbole in zwei Gruppen auf
    group1 = probabilities[:split_index + 1]
    group2 = probabilities[split_index + 1:]

    return group1, group2


def create_lookup_table(probabilities: list[tuple[str, float]]) -> dict[str, str]:
    if len(probabilities) == 1:
        # Wenn nur noch ein Symbol übrig ist, dann ist die Codierung abgeschlossen
        return {probabilities[0][0]: ''}

    group1, group2 = split_by_probability(probabilities)

    # Rekursiv kodiere die beiden Gruppen
    group1 = create_lookup_table(group1)
    group2 = create_lookup_table(group2)

    # Füge die beiden Gruppen zusammen
    lookup_table = {}
    lookup_table.update({symbol: '0' + code for symbol, code in group1.items()})
    lookup_table.update({symbol: '1' + code for symbol, code in group2.items()})

    return lookup_table


def binary_string_to_string(binary: str) -> str:
    # Füge Nullen an das Ende an, damit die Länge durch 8 teilbar ist
    binary += '0' * (8 - len(binary) % 8)

    string = ''
    for i in range(0, len(binary), 8):
        # Extrahiere den 8-Bit Block
        block = binary[i:i + 8]
        number = int(block, 2)
        character = chr(number)
        string += character

    return string


if __name__ == '__main__':
    text = "Dies ist ein Testtext."
    probabilities = Z_statistik(text)
    compressed_text = Q_Fanoencoder(text, probabilities)
    print(f"Originaler Text:    {text}")
    print(f"Komprimierter Text: {compressed_text}")
    print(f"Kompressionsrate:   {len(compressed_text) / len(text)}")
