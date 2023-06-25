from praktikum1.a import Z_statistik
from praktikum3.a import Q_Fanoencoder, create_lookup_table, dict_to_sorted_list


def Q_Fanodecoder(encoded_text: str, probabilities: dict[str, float]):
    # Schritt 1: Sortiere die Symbol nach absteigender Wahrscheinlichkeit
    probabilities = dict_to_sorted_list(probabilities)

    # Schritt 2: Erstelle eine Umkehrung der Lookup-Tabelle
    lookup_table = create_lookup_table(probabilities)
    lookup_table = {code: symbol for symbol, code in lookup_table.items()}

    # Schritt 3: Konvertiere den Text in eine binäre Folge
    binary_string = string_to_binary_string(encoded_text)

    decoded_text = ""
    current_code = ""

    # Schritt 4: Dekodiere die binäre Folge
    for bit in binary_string:
        # Füge das Bit der aktuellen Binärzahl hinzu
        current_code += bit
        # Wenn die aktuelle Binärzahl in der Lookup-Tabelle existiert, dann füge das Symbol dem Ergebnis hinzu
        if current_code in lookup_table:
            decoded_text += lookup_table[current_code]
            current_code = ""

    return decoded_text


def string_to_binary_string(encoded_text):
    binary_string = ""
    for char in encoded_text:
        # Konvertiere jedes Zeichen in eine 8-Bit Binärzahl
        binary_string += format(ord(char), '08b')
    return binary_string


if __name__ == '__main__':
    text = "Dies ist ein Testtext."
    probabilities = Z_statistik(text)
    compressed_text = Q_Fanoencoder(text, probabilities)
    decoded_text = Q_Fanodecoder(compressed_text, probabilities)
    print(f"Originaler Text:    {text}")
    print(f"Komprimierter Text: {compressed_text}")
    print(f"Kompressionsrate:   {len(compressed_text) / len(text)}")
    print(f"Dekodierter Text:   {decoded_text}")
