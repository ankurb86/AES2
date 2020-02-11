from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def cipherCheck():
    #First we run AES for ECB Mode
    # Get the key
    fKey = open("../data/key.txt", "r")
    key = fKey.read()
    fKey.close()
    key = bytes.fromhex(key)

    # Get the plaintext
    fPlainText = open("../data/plaintext.txt", "r")
    plainTextString = fPlainText.read().encode("latin-1")
    fPlainText.close()
    plainTextString = plainTextString + ((16 - len(plainTextString) % 16) * '~').encode("latin-1")

    #Select mode for encryption
    cipher = AES.new(key, 1)  # Mode ECB=1, CBC=2
    #Generate the ciphertext
    cipherText = (cipher.encrypt(plainTextString)).hex()
    print("The Ciphertext generated using ECB Mode: ",cipherText)

    #Now we run for CBC mode
    iv = get_random_bytes(16)
    cipher = AES.new(key, 2, iv)
    cipherText = (cipher.encrypt(plainTextString)).hex()
    print("The Ciphertext generated using CBC Mode: ", cipherText)
