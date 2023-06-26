"""
in deze file staan wiskundige functie die ik heb gebruikt voor het

bron: https://iq.opengenus.org/dot-product-in-python/
"""
import numpy as np

def inwendig_product(a, b):
    """
    Hier wordt het inwendig product/dot product van twee vectoren berekend.
    Dus stel je voor D1 = [1, 1, 0, 0] en D2 = [0, 1, 1, 0]
    D1 * D2 = 1*0 + 1*1 + 0*1 + 0*0 = 1

    :param a: Eerste vector
    :param b: Tweede vector
    :return: Het inwendig product van de twee vectoren
    """
    # Controleer of de arrays compatibel zijn
    if len(a) != len(b):
        raise ValueError("Arrays are not compatible for dot product")

    # Bereken het inwendig product
    dot_product = sum([a[i] * b[i] for i in range(len(a))])

    return dot_product


def calculate_magnitude(x):
    """
    Bereken de magnitude (L2-norm) van een vector x.

    :param x: De vector waarvan de magnitude moet worden berekend
    :return: De magnitude van de vector x
    """
    # Bereken de som van de kwadraten van de elementen in de vector
    sum_of_squares = sum([element ** 2 for element in x])

    # Bereken de vierkantswortel van de som van de kwadraten
    magnitude = np.sqrt(sum_of_squares)

    return magnitude





