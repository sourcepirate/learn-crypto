# one time pad decrypt

from __future__ import print_function


import os
import sys


def main(ency_file_path):
    path = os.path.join(os.getcwd(), ency_file_path)
    copy_file = os.path.join(os.getcwd(), ency_file_path.replace(".enc", ".copy"))

    fd = open(path, 'rb')
    wd = open(copy_file, 'wb')
    key = open("keyfile.key", 'rb').read()

    while True:
        data = fd.read(32)
        if not data:
            break
        decrypted = [chr(ord(i) ^ ord(j)) for i, j in zip(data, key)]
        wd.write("".join(decrypted))
    
    wd.close()
    fd.close()


main(sys.argv[1])