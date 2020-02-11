import sys
from Encrypt import Enc
from Decrypt import Dec
from ECBModeEncryption import ecbEncrypt
from ECBModeDecryption import ecbDecrypt
from KeyGen import GenerateKey
from CiphertextComparison import cipherCheck


if (sys.argv[1] == 'CBCE'):
    Enc()
elif (sys.argv[1] == 'CBCD'):
    Dec()
elif (sys.argv[1] == 'ECBE'):
    ecbEncrypt()
elif (sys.argv[1] == 'ECBD'):
    ecbDecrypt()
elif(sys.argv[1] == 'KEYGEN'):
    GenerateKey()
elif(sys.argv[1] == 'COMPARE'):
    cipherCheck()
