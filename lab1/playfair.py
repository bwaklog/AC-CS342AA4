from typing import Dict, Tuple


def encrypt(keyword: str, plaintext: str) -> str:
    join = keyword.upper().replace("J", "I") + "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    flatmat = "".join(dict.fromkeys(join))

    matr = [list(flatmat[i : i + 5]) for i in range(0, 25, 5)]

    pos_map: Dict[str, Tuple[int, int]] = {}
    rev_map: Dict[Tuple[int, int], str] = {}

    pos_map: Dict[str, Tuple[int, int]] = {}
    rev_map: Dict[Tuple[int, int], str] = {}
    for i, row in enumerate(matr):
        for j, c in enumerate(row):
            pos_map[c] = (i, j)
            rev_map[(i, j)] = c

    pt = list(plaintext.upper().replace("J", "I"))

    i = 0
    while i < len(pt) - 1:
        if pt[i] == pt[i + 1]:
            pt.insert(i + 1, "X")
        i += 2

    if len(pt) % 2 != 0:
        pt.append("X")
    pairs = [pt[i : i + 2] for i in range(0, len(pt), 2)]

    for i, pair in enumerate(pairs):
        a = pos_map[pair[0]]
        b = pos_map[pair[1]]
        if a[0] == b[0]:
            pairs[i] = [
                rev_map[(a[0], (a[1] + 1) % 5)],
                rev_map[(b[0], (b[1] + 1) % 5)],
            ]
        elif a[1] == b[1]:
            pairs[i] = [
                rev_map[((a[0] + 1) % 5, a[1])],
                rev_map[((b[0] + 1) % 5, b[1])],
            ]
        else:
            pairs[i] = [
                rev_map[(a[0], b[1])],
                rev_map[(b[0], a[1])],
            ]

    enc = "".join("".join(pair) for pair in pairs)
    return enc


print(encrypt("WORK", "CRYPTOGRAPHY"))
