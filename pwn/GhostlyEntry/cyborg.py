# cyborg.py
import hashlib
import base64

def xor_bytes(data: bytes, key: bytes) -> bytes:
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])

def reveal_flag_from_file(password: str, secret_file: str = "secret.dat") -> str:
    try:
        with open(secret_file, "rb") as f:
            b64 = f.read().strip()
    except FileNotFoundError:
        return None

    try:
        enc = base64.b64decode(b64)
    except Exception:
        return None

    key = hashlib.sha256(password.encode()).digest()
    dec = xor_bytes(enc, key)
    try:
        return dec.decode('utf-8')
    except Exception:
        return None

def ghostlyentry_loop():
    print("All things change in a dynamic environment. If you want to survive you better cough up the password!")
    print("Type 'quit' to exit.\n")

    attempts = 0
    while True:
        attempt = input("> ").strip()
        attempts += 1

        if attempt.lower() == "quit":
            print("My mind is human. My body is manufactured. And you are not getting past.")
            break
        
        flag = reveal_flag_from_file(attempt)
        if flag:
            print("\nJust know it only gets worse from here.")
            print(flag)
            break
        else:
            print(f"You won't get past me with that  (attempt #{attempts})")
            if attempts >= 5:
                print("Hint: Ghost in the house more like Ghost in the interface users use to interact with an operating system.")

if __name__ == "__main__":
    ghostlyentry_loop()
