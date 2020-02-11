from Crypto.Random import get_random_bytes
import timeit

def GenerateKey():
    # Start Time for monitoring run time
    startTime = timeit.default_timer()

    #get_random_bytes will create a hexadecimal value of the selected bytes. As we need a 256 bit key here we take 32 bytes.
    key = get_random_bytes(32).hex()
    fKey = open("../data/key.txt", "w")
    fKey.write(key)
    fKey.close()
    print("The key that has been generated is: ", key)

    # Check Execution time using the startTime variable
    stopTime = timeit.default_timer()
    print("\nThe run Time for Generating a new Key is: ", stopTime - startTime)

# GenerateKey()