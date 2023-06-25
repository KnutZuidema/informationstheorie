import random

import numpy as np

from praktikum2.a import hamming_encoder

parity_check_matrix = np.array([
    [1, 1, 1, 0, 1, 0, 0],
    [1, 1, 0, 1, 0, 1, 0],
    [1, 0, 1, 1, 0, 0, 1]
])


def hamming_decoder(encoded_data):
    # Dekodierte Sequenz initialisieren
    decoded_data = ''

    # Decodierung der codierten Sequenz
    for i in range(0, len(encoded_data), 7):
        # Extrahieren der 7-Bit-Blöcke
        block = encoded_data[i:i + 7]

        # Umwandeln des 7-Bit-Blocks in einen Vektor
        block = np.array([int(bit) for bit in block])

        # Multiplikation des 7-Bit-Blocks mit der Parity-Check-Matrix
        parity_check = np.dot(parity_check_matrix, block.T) % 2

        # Prüfen, ob ein Fehler aufgetreten ist
        if np.sum(parity_check) != 0:
            # Überprüfe, welcher Spalte aus der Parity-Check-Matrix entspricht und korrigiere den Fehler
            for j in range(len(parity_check_matrix.T)):
                if np.array_equal(parity_check, parity_check_matrix.T[j]):
                    block[j] = (block[j] + 1) % 2
                    break

        # Umwandeln des decodierten Blocks in eine Zeichenkette
        decoded_block = ''.join([str(bit) for bit in block[:4]])

        # Anhängen des decodierten Blocks an die decodierte Sequenz
        decoded_data += decoded_block

    return decoded_data


if __name__ == '__main__':
    # Erzeugen einer zufälligen Informationsfolge
    data = ''.join([random.choice(['0', '1']) for _ in range(16)])
    print(f"Information: {data}")

    # Codieren der Informationsfolge
    encoded_data = hamming_encoder(data)
    print(f"Encoded:     {encoded_data}")

    # Dekodieren der codierten Sequenz
    decoded_data = hamming_decoder(encoded_data)
    print(f"Decoded:     {decoded_data}")
