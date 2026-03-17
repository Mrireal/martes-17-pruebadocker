
import sys
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64

def decrypt(encrypted_text, key, iv):
    key_hash = hashlib.sha256(key.encode('utf-8')).digest()
    iv = base64.b64decode(iv)
    ct = base64.b64decode(encrypted_text)
    cipher = AES.new(key_hash, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size)
    return pt.decode('utf-8')

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python decrypt.py <encrypted_text> <key> <iv>")
        sys.exit(1)

    encrypted_text = sys.argv[1]
    key = sys.argv[2]
    iv = sys.argv[3]

    decrypted_text = decrypt(encrypted_text, key, iv)

    print(f"Decrypted Text: {decrypted_text}")
