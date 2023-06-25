import random

from praktikum2.a import hamming_encoder
from praktikum2.b import hamming_decoder


def channel_bsc(p, length):
    error_word = ''
    num_errors = int(p * length)

    # Füge Fehler (Einsen) zum Fehlerwort hinzu
    error_indices = random.sample(range(length), num_errors)
    for i in range(length):
        if i in error_indices:
            error_word += '1'
        else:
            error_word += '0'

    return error_word


if __name__ == '__main__':
    # Erzeugen einer zufälligen Informationsfolge
    data = ''.join(random.choices(['0', '1'], k=16))
    print(f"Information: {data}")

    # Codieren der Informationsfolge
    encoded_data = hamming_encoder(data)
    print(f"Encoded:     {encoded_data}")

    # Simulieren eines Kanals mit Bitfehlern
    error = channel_bsc(0.1, len(encoded_data))
    received_data = ''
    for i in range(len(encoded_data)):
        received_data += str(int(encoded_data[i]) ^ int(error[i]))
    print(f"Received:    {received_data}")

    # Dekodieren der codierten Sequenz
    decoded_data = hamming_decoder(received_data)
    print(f"Decoded:     {decoded_data}")

    print(f"Correct:     {decoded_data == data}")
