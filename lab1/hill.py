import numpy as np


def encrypt(key: np.ndarray, plaintext: str):
    plaintext = plaintext.upper().replace(" ", "")
    plaintext = "".join(char for char in plaintext if char.isalpha())

    _, n = key.shape

    plaintext += "X" if len(plaintext) % n != 0 else ""

    pt = list(map(lambda x: ord(x) - ord("A"), plaintext))

    P = np.array([pt[i : i + n] for i in range(0, len(pt), n)]).T
    C = (key @ P) % 26

    ct = "".join(chr(int(c) + ord("A")) for c in C.T.flatten())
    return ct


print(encrypt(np.array([[1, 2], [2, 2]]), "WORK"))
