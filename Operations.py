import operator
from itertools import cycle, imap
import os


def xor(arg1, arg2):
    return ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(arg1, cycle(arg2)))
def xorTwoStrings(string1,string2):
    return ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(string1, string2))

def xorAgainst(arg1, xor):
    return ''.join(chr(ord(a) ^ xor) for a in arg1)


def xorAgaintKey(arg1, key):
    return ''.join(chr(ord(a) ^ key) for a in arg1)


def hammingDistance(arg1, arg2):
    assert len(arg1) == len(arg2)
    return sum(imap(operator.ne, arg1, arg2))


def binaryHamming(arg1, arg2):
    arg1 = ''.join([bin(ord(letter))[2:].zfill(8) for letter in arg1])
    arg2 = ''.join([bin(ord(letter))[2:].zfill(8) for letter in arg2])
    assert len(arg1) == len(arg2)
    return sum(imap(operator.ne, arg1, arg2))

def padString(string, padlength, padchar):
    if len(string)==0:
        string+=padchar*padlength
    else:
        string+=padchar*(padlength%len(string))
    return string
def randompad(string, padlength):
    length = len(string)
    if length==0:
        string+=os.urandom(padlength)
    else:
        string+=os.urandom(padlength-(length%padlength))
    return string
def randombytes(size):
    return os.urandom(size)
def detectECB(data,maxoffset,keysize=16):
    for x in range(0,maxoffset):
        data1 = data[x:]
        blockdata = [data1[i:i+keysize] for i in range(0, len(data1), keysize)]
        for blocknumber,block in enumerate(blockdata):
            for block2 in blockdata[blocknumber+1:len(blockdata)-1]:
                if block == block2:
                    return 1

    return 0
