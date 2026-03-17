import sys
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64


def encrypt(text, key):
    # Derive a 32-byte key using SHA-256 from the provided key string
    key_hash = hashlib.sha256(key.encode("utf-8")).digest()

    cipher = AES.new(key_hash, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(text.encode("utf-8"), AES.block_size))
    iv = base64.b64encode(cipher.iv).decode("utf-8")
    ct = base64.b64encode(ct_bytes).decode("utf-8")
    return iv, ct


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python encrypt.py <text_to_encrypt> <key>")
        sys.exit(1)

    text_to_encrypt = sys.argv[1]
    key = sys.argv[2]

    iv, encrypted_text = encrypt(text_to_encrypt, key)

    print(f"IV: {iv}")
    print(f"Encrypted Text: {encrypted_text}")
