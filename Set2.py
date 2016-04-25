import Operations
import AESImplementation
import FileConvert
def main():
    #challenge 9
    print 'Challenge 9 Results: '
    print Operations.padString('YELLOW SUBMARINE',20,'\x04')

    #challenge 10
    data = FileConvert.FileConvert("10.txt")
    data.b64ToBinary()
    data.integrate()
    iv = Operations.padString('',16,'\x00')
    AESCipher = AESImplementation.AESstuff('YELLOW SUBMARINE')
    print AESCipher.CBCEncrypt(iv,data.getContent())

    #challenge 11
    data11 = FileConvert.FileConvert("12.txt")
    data11.integrate()
    RandCipher = AESImplementation.AESstuff(Operations.randombytes(16))
    RandCipher.randKeyAndProtocol()
    if RandCipher.detectifECB()==1:
        print "ECB Detected"
    else:
        print "CBC, Or something"

    #challenge 12
    data12 = FileConvert.FileConvert("12.txt")
    data12.b64ToBinary()



if __name__ == '__main__':
    main()