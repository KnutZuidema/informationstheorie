import random

import matplotlib.pyplot as plt
import numpy as np

from praktikum2.a import hamming_encoder
from praktikum2.b import hamming_decoder
from praktikum2.c import channel_bsc

if __name__ == '__main__':

    L_data = 100
    N_iterations = 100
    p_bsc = list(np.arange(0.8, 0.2, -0.1)) + list(np.arange(0.2, 0, -0.02))

    bit_error_rates = []
    channel_error_rates = []

    for p in p_bsc:
        total_bit_errors = 0
        total_channel_errors = 0

        for _ in range(N_iterations):
            # Generiere zufällige Informationsbits
            data = ''.join(random.choices(['0', '1'], k=L_data))

            # Codierung der Informationsbits
            encoded_data = hamming_encoder(data)

            # Kanalübertragung mit BSC
            channel_error_word = channel_bsc(p, len(encoded_data))
            received_data = ''.join(
                ['1' if encoded_data[i] != channel_error_word[i] else '0' for i in range(len(encoded_data))])

            # Decodierung der empfangenen Daten
            decoded_data = hamming_decoder(received_data)

            # Zähle die Anzahl der Bitfehler
            bit_errors = sum([1 for i in range(len(data)) if data[i] != decoded_data[i]])

            # Zähle die Anzahl der Kanalfehler
            channel_errors = sum([1 for i in range(len(encoded_data)) if encoded_data[i] != received_data[i]])

            total_bit_errors += bit_errors
            total_channel_errors += channel_errors

        # Berechne Bitfehlerrate und Kanalfehlerrate
        bit_error_rate = total_bit_errors / (N_iterations * L_data)
        channel_error_rate = total_channel_errors / (N_iterations * len(encoded_data))

        bit_error_rates.append(bit_error_rate)
        channel_error_rates.append(channel_error_rate)

    # Plotten der Ergebnisse
    plt.semilogy(p_bsc, bit_error_rates, label='Bitfehlerrate')
    plt.semilogy(p_bsc, channel_error_rates, label='Kanalfehlerrate')
    plt.xlabel('Übergangsfehlerwahrscheinlichkeit p')
    plt.ylabel('Fehlerrate')
    plt.title('Leistung der Hamming (7,4,3) Codierung im BSC-Kanal')
    plt.legend()
    plt.grid(True)
    plt.show()
