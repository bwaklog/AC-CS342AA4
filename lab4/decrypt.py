import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

plaintext = bytes.fromhex("255044462d312e350a25d0d4c5d80a34")
ciphertext = bytes.fromhex("d06bf9d0dab8e8ef880660d2af65aa82")
iv = bytes.fromhex("09080706050403020100A2B2C2D2E2F2")

ct_key_map = list(filter(
    lambda y: y[0] == ciphertext,
    map( 
        lambda x: (x[0].encrypt(plaintext), x[1]),
        map(
            lambda key: (AES.new(key, AES.MODE_CBC, iv), key), # cipher 
            map(
                lambda line: bytes.fromhex(line.strip()), # Key
                open("keys.txt").readlines()
            )
        )
    )
))[0]

print(json.dumps({
    'plaintext': plaintext.hex(),
    'ciphertext': ct_key_map[0].hex(),
    'iv': iv.hex(),
    'key': ct_key_map[1].hex(),
}, indent=4))
