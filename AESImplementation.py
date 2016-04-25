import re

from Crypto.Cipher import AES


from Operations import *
import random


class AESstuff:
    def __init__(self, key=None, mode=1, iv=None):
        if iv is None:
            self.cipher = AES.new(key, mode)
        else:
            self.cipher = AES.new(key, mode,iv) # if I want to make an auto CBC decryptor, but I'm making it from scratch
        self.key = key
        self.iv = iv
        self.keylength = len(self.key)
    def encrypt(self, data):
        return self.cipher.encrypt(data)
    def decrypt(self, data):
        return self.cipher.decrypt(data)
    def CBCEncrypt(self, IV=None, data=None):
        if data is None:
            print("No Data Detected, Cannae Do it")
            raise Exception("No Input Data-CBCEncrypt")
        if IV is None:
            IV = self.iv
        if IV is None:
            print("No IV Detected, Cannae Do it")
            raise Exception("No IV initiailized")
        length = len(self.key)
        decrypted = [data[i:i+length] for i in range(0, len(data), length)]
        for i, block in enumerate(decrypted):
            tempIV = decrypted[i]
            block = self.cipher.decrypt(block)
            block = xor(block,IV)
            decrypted[i] = block
            IV=tempIV
        return ''.join(x for x in decrypted)
    def detectifECB(self):
        teststring = 'A'*64
        teststring = self.appendBeforeandAfter(teststring)
        teststring = randompad(teststring,16)
        return detectECB(self.cipher.encrypt(teststring),10)
    def appendBeforeandAfter(self,data=None):
        if data is None:
            print("No Data Detected, Cannae Do it")
            raise Exception("No Input Data-CBCEncrypt")
        minappend = 5
        maxappend = 10
        before = randombytes(random.randint(minappend,maxappend))
        after = randombytes(random.randint(minappend,maxappend))
        data = before+data+after
        return data
    def randKeyAndProtocol(self):
        if bool(random.getrandbits(1)):
            self.cipher = AES.new(randombytes(self.keylength),2,randombytes(self.keylength))
            print "CBC"
        else:
            self.cipher = AES.new(randombytes(self.keylength),1)
            print "ECB"

