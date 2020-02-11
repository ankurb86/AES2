# AES2
AES Encryption with ECB(Electronic Codebook) and CBC(Cipher Block Chaining)

README FILE

PROJECT ON AES ENCRYPTION for CS 6058 DATA SECURITY AND PRIVACY, SPRING 2018,
by ANKUR BHATTACHARYA, MID #M12467767
bhattaar@mail.uc.edu
March 8th, 2018

[ABOUT THE PROJECT]
    This project is for implementing the AES Encryption to securely transfer files from sender to receiver
    It will make use of ECB(Electronic Codebook) and CBC(Cipher Block Chaining) modes of Encryption and Decryption.
    The system will monitor the run times of the functions.
    Data will be saved in hexadecimal format for the Key, IV and Ciphertexts

---------------------------------------------------------------------------------------------------------------------------
CONTENTS
I.      SYSTEM AND SOFTWARE REQUIREMENTS
II.     RUNNING THE PROGRAM AND PROGRAM DESCRIPTIONS
III.    FILES AND STRUCTURE
IV.     KNOWN ISSUES AND WORKAROUNDS

---------------------------------------------------------------------------------------------------------------------------
I.  SYSTEM AND SOFTWARE REQUIREMENTS

1.  Operating System: Windows 7, Windows 8, Windows 10
2.  Software: Python 3.6.3
    Please note that the latest version of python i.e. Python 3.6.3 is required to run this if you're using Windows 10.
    Download the latest version at https://www.python.org/downloads/release/python-363/
    While Installing, check the button to include the Path to Python in Environment Variables

---------------------------------------------------------------------------------------------------------------------------
II. RUNNING THE PROGRAM AND PROGRAM DESCRIPTIONS

    1. Open up a command prompt window
    2. Check if Python is installed
        2.a.  To get to the command line, open the Windows menu and type “cmd” in the search bar. Select Command Prompt from the search results.
              In the Command Prompt window, type the following and press Enter.
                python
              If Python is installed and in your path, then this command will run python.exe and show you the version number.
                C:\Users\Nighthawk>python
                Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
                Type "help", "copyright", "credits" or "license" for more information.
              If python is installed, then type the following command and press Enter
                exit()
              If python is not installed, you will see
                'python' is not recognized as an internal or external command, operable program or batch file.
              In that case, please install python from the steps provided above
    3.  Go to the program location path by issuing the cd command with the path of the program's src folder
                cd <path>
                e.g. C:\Users\Nighthawk>cd /d D:\Development\Python\UC\opt_m12467767\src
    4.  Run the following command to install the crypto dome package
                pip install pycryptodome
                e.g. D:\Development\Python\UC\aes_m12467767\src>pip install pycryptodome
    5.  COMMANDS FOR RUNNING THE PROGRAM
        If you need to change the message at any time then open the data/plaintext.txt folder and edit the message.
        You can change the secret key from the data/key.txt as well for the ENCRYPTION PROGRAM

        Type the required commands and press enter
        5.a.    ENCRYPTION WITH ECB MODE PROGRAM
                This program takes the message from the plaintext.txt file in the data folder and generates a ciphertext based on the key in the
                key.txt file of the data folder. It generates a ciphertext using AES with ECB mode of encryption. It stores the ciphertext in the
                ciphertext.txt file in the data folder. If you wish to change the message, You will need to open the plaintext.txt file and
                enter a message.
                It will save data of its run in the runstats.txt file

                Command:
                    python aes.py ECBE

        5.b.    DECRYPTION WITH ECB MODE PROGRAM
                This program takes the ciphertext from the ciphertext.txt file, takes the secret key from the key.txt file and then generates the
                original message back using AES with ECB mode of decryption and saves this message in the result.txt file.
                Before running this you must ensure that you have encrypted the message using ECB Encryption mode. If you try to run this program
                after using CBC encryption mode, it will throw an error.
                It will save data of its run in the runstats.txt file

                Command:
                    python aes.py ECBD

        5.c     ENCRYPTION WITH CBC MODE PROGRAM
                This program first creates a random IV of 128 bits. It then takes the message from the plaintext.txt file in the data folder and
                XORs it with the IV. It then generates a ciphertext based on the key in the key.txt file of the data folder running it as a
                function of the IV XOR Plaintext value. It generates a ciphertext using AES with CBC mode of encryption. It stores the ciphertext
                in the ciphertext.txt file in the data folder. If you wish to change the message, You will need to open the plaintext.txt file and
                enter a message.
                It will save data of its run in the runstats.txt file

                Command:
                    python aes.py CBCE

        5.d.    DECRYPTION WITH CBC MODE PROGRAM
                This program takes the ciphertext from the ciphertext.txt file, takes the secret key from the key.txt file, takes the IV from the
                iv.txt file and then uses these files to generate the original message back using AES with CBC mode of decryption and saves this
                message in the result.txt file. Before running this you must ensure that you have encrypted the message using CBC Encryption mode.
                If you try to run this program after using CBC encryption mode, it will throw an error.
                It will save data of its run in the runstats.txt file

                Command:
                    python aes.py CBCD

        5.e.    NEW KEY GENERATION PROGRAM
                This program creates a random 256bit key and saves the key in the key.txt file.
                Command:
                    python aes.py KEYGEN

        5.f.    CHECK KEY FREQUENCY PROGRAM
                This program will first run the AES encryption with ECB Mode using the key and plain text stored in the key.txt file and
                plaintext.txt file. It will generate a ciphertext based on this encryption and output the ciphertext on the screen.
                Then the program will run the AES encryption with CBC Mode by generating an IV of 128 bits and use the IV to generate a ciphertext
                and output the ciphertext on the screen.

                Command:
                    python aes.py COMPARE

---------------------------------------------------------------------------------------------------------------------------
III. FILES AND STRUCTURE

    The Files included in this project are:
    build
    data
    --ciphertext.txt
    --iv.txt
    --key.txt
    --plaintext.txt
    --result.txt
    --runstats.txt
    src
    --aes.py
    --CiphertextComparison.py
    --Decrypt.py
    --ECBModeDecryption.py
    --ECBModeEncryption.py
    --Encryption.py
    --KeyGen.py
    --main.py
    Readme.txt

---------------------------------------------------------------------------------------------------------------------------
IV. KNOWN ISSUES AND WORKAROUNDS

    If you receive the below error at any point of time, then follow the steps provided below as a fix.

    [ISSUE 1]
    OSError: raw write() returned invalid length
    This error mostly pops up while running the CHECK KEY FREQUENCY PROGRAM.

    [WORKAROUND]
    This occurs if you're running Windows 10 and a version of Python lower than 3.6.
    Update your python version to 3.6+ to fix the issue.

    [ISSUE 2]
    ImportError: No module named Crypto.Cipher
    This error mostly pops up while running the Encryption/Decryption programs for ECB/CBC Mode

    [WORKAROUND]
    This occurs if the crypto package did not come installed with python.
    Install cryptodome package with pip to fix the issue (Step II.4).

