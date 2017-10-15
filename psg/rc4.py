# Key sheduling and rc4 with Pseduo random number generation

import os

def to_keys(s):
    """to integer array"""
    return [ord(i) for i in s]

def KSA(key):
    keylength = len(key)
    S = range(256)
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % keylength]) % 256
        S[i], S[j] = S[j], S[i] 
    return S

def PRGA(S):
    """stream cipher key"""
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]  # swap
        K = S[(S[i] + S[j]) % 256]
        yield K

def RC4(key):
    S = KSA(key)
    return PRGA(S)

def encrypt(key, text):
    """encrypt"""
    gen = RC4(key)
    _bytes = []
    for i in text:
        _bytes.append(chr(ord(i) ^ next(gen)))
    return "".join(_bytes)

print(encrypt(to_keys(os.urandom(128)), "hello"))
    