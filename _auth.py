import hashlib
import random


def random_string(size: int) -> str:
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return "".join(random.choices(alphabet, k=size))

def md5_hash(text: str) -> str:
    m = hashlib.md5()
    m.update(text.encode('utf-8'))
    return m.hexdigest() 
