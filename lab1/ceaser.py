def encrypt(plaintext: str, key: int) -> str:
    return "".join(
        list(
            map(
                lambda x: chr((((ord(x) - ord("A")) + key) % 26) + ord("A")),
                plaintext.upper(),
            )
        )
    )


print(encrypt("CRYPTOGRAPHY", 10))
assert encrypt("CRYPTOGRAPHY", 10) == "MBIZDYQBKZRI"
