import time
import secrets


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.6f} seconds")
        return result

    return wrapper


# Task 3a
@timer
def random_generated() -> None:
    with open("/dev/random", "rb") as file:
        keys = [file.read(128).hex() for _ in range(20)]
        for i, key in enumerate(keys, start=1):
            print(f"Key {i}: {key}")


# Task 3b
@timer
def urandom_generated() -> None:
    with open("/dev/random", "rb") as file:
        keys = [file.read(128).hex() for _ in range(20)]
        for i, key in enumerate(keys, start=1):
            print(f"Key {i}: {key}")


# Task 3c
@timer
def secrets_generated() -> None:
    keys = [secrets.token_bytes(128).hex() for _ in range(20)]
    for i, key in enumerate(keys, start=1):
        print(f"Key {i}: {key}")
