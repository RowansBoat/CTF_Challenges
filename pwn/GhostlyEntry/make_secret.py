# make_secret.py
import hashlib
import base64

def xor_bytes(data: bytes, key: bytes) -> bytes:
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])

def create_secret_file(flag: str, password: str, out_file: str = "secret.dat"):
    key = hashlib.sha256(password.encode()).digest()   # 32-byte key
    enc = xor_bytes(flag.encode('utf-8'), key)
    with open(out_file, "wb") as f:
        f.write(base64.b64encode(enc))

if __name__ == "__main__":
    flag = "CTF{/shellofahouse/}"
    password = "shell"   # the secret phrase players must find / guess
    create_secret_file(flag, password)
