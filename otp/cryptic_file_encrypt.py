# one time pad encrypt
from __future__ import print_function


import os
import sys
from itertools import cycle

def main(file_path):
    path = os.path.join(os.getcwd(), file_path)
    new_path = os.path.join(os.getcwd(), "{}.enc".format(file_path))
    fd = open(path, 'rb')
    wd = open(new_path, 'wb')
    keyf = open("keyfile.key", 'wb')
    key = os.urandom(32)
    print("Encrypticing with key {}".format(key))
    keyf.write(key)
    keyf.close()
    while True:
        data = fd.read(32)
        if not data:
            break
        encyrpted_data = [chr(ord(i) ^ ord(j)) for i, j in zip(key, data)]
        wd.write("".join(encyrpted_data))
    fd.close()
    wd.close()

print(sys.argv)
main(sys.argv[1])