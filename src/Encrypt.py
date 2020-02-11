from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import timeit

def Enc():
    # Start Time for monitoring run time
    startTime = timeit.default_timer()

    # generate the Initialization Vector (IV)
    iv = get_random_bytes(16)

    #Get the Key
    fKey = open("../data/key.txt", "r")
    key = fKey.read()
    fKey.close()
    print("Secret Key: ", key)
    key = bytes.fromhex(key)

    #Get the Plaintext Message
    fPlainText = open("../data/plaintext.txt","r")
    plainTextString = fPlainText.read().encode("latin-1")
    fPlainText.close()
    print("PlaintText String: ", plainTextString)
    plainTextString = plainTextString + ((16 - len(plainTextString) % 16) * '~').encode("latin-1")

    #Encrypt using AES with CBC Mode
    cipher = AES.new(key, 2, iv) #Mode ECB=1, CBC=2

    #Save the Initialization Vector (IV)
    iv = iv.hex()
    print("IV: ",iv)
    fIV = open("../data/iv.txt", "w")
    fIV.write(iv)
    fIV.close()

    #Save the ciphertext
    cipherText = (cipher.encrypt(plainTextString)).hex()
    print("ciphertext: ", cipherText)
    fCipherText = open("../data/ciphertext.txt", "w")
    fCipherText.write(cipherText)
    fCipherText.close()

    # Check Execution time using the startTime variable
    stopTime = timeit.default_timer()
    print("\nThe run Time of the Encryption Function for CBC Mode is: ", stopTime - startTime)

    # Save Stats
    fstats = open("../data/runstats", "a+")
    fstats.write("Mode: CBC")
    fstats.write(" Task: Encryption")
    fstats.write(" Runtime: ")
    fstats.write(str(stopTime - startTime))
    fstats.write(" Ciphertext Generated: ")
    fstats.write(cipherText)
    fstats.write("\n")
    fstats.close()

# Enc()