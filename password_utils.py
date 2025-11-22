# password_utils.py

import hashlib
import os
import base64

def generate_salt():
    #generate a random 16-byte salt
    return os.urandom(16)

def hash_password(password: str, salt: bytes) -> str:
    #hash a password with salt using SHA-256
    if isinstance(password, str):
        password = password.encode()
    return hashlib.sha256(password + salt).hexdigest()

def verify_password(password: str, hashed_password: str, salt: bytes) -> bool:
    #password matches the hashed password?
    return hashed_password == hash_password(password, salt)

def encode_salt(salt: bytes) -> str:
    #encode salt to base64 for storing in db, like b'\x8f\xa3\xd2\x1f\x5b...' → 'j6PSs...'
    return base64.b64encode(salt).decode()

def decode_salt(salt_b64: str) -> bytes:
    #decode base64 salt from DB back to bytes
    return base64.b64decode(salt_b64)