import random

import numpy as np

generator_matrix = np.array([
    [1, 0, 0, 0, 1, 1, 1],
    [0, 1, 0, 0, 1, 1, 0],
    [0, 0, 1, 0, 1, 0, 1],
    [0, 0, 0, 1, 0, 1, 1]
])


def hamming_encoder(data):
    # Überprüfen der Länge der Informationsfolge
    if len(data) % 4 != 0:
        # Auffüllen der Informationsfolge mit Nullen, wenn die Länge nicht durch 4 teilbar ist
        data += '0' * (4 - len(data) % 4)

    # Codierte Sequenz initialisieren
    encoded_data = ''

    # Codierung der Informationsfolge
    for i in range(0, len(data), 4):
        # Extrahieren der 4-Bit-Blöcke
        block = data[i:i + 4]

        # Umwandeln des 4-Bit-Blocks in einen Vektor
        block = np.array([int(bit) for bit in block])

        # Multiplikation des 4-Bit-Blocks mit der Generatormatrix
        encoded_block = np.dot(block, generator_matrix) % 2

        # Umwandeln des codierten Blocks in eine Zeichenkette
        encoded_block = ''.join([str(bit) for bit in encoded_block])

        # Anhängen des codierten Blocks an die codierte Sequenz
        encoded_data += encoded_block

    return encoded_data


if __name__ == '__main__':
    # Erzeugen einer zufälligen Informationsfolge
    data = ''.join([random.choice(['0', '1']) for _ in range(16)])

    # Codieren der Informationsfolge
    encoded_data = hamming_encoder(data)

    # Ausgabe der Ergebnisse
    print(f"Information: {data}")
    print(f"Encoded:     {encoded_data}")
