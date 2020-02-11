import os
import sys

##
# This file exposes certain helper functions that are repeatedly used through out the project.
##

## Helper function to read files
def readFile(path):
    if not path:
        raise ValueError('Path not defined')

    current_directory = os.path.dirname(os.path.realpath(__file__))
    #print(current_directory)
    parent_path = os.path.split(current_directory)[0]
    path = parent_path + '\\data\\' + path
    #print(path)
    f = open(path, "r")
    if f.mode == 'r':
        contents = f.read().split(" ")
        #print(contents)
    f.close()
    return contents

## Helper function to write to files
def writeFile(path, text, append = False):

    if not path:
        raise ValueError('Path not defined')

    current_directory =  os.path.dirname(os.path.realpath(__file__))
    parent_path = os.path.split(current_directory)[0]
    path = parent_path + '\\data\\' + path
    #print("path : {}".format(path))

    p2 = 'w+'
    if append:
        p2 = 'a+'
        text = ",\n" + str(text)

    f = open(path,p2)

    #for i in range(12):
    f.write("{}".format(text))
    f.close()

def convert_to_ascii(msg):
    return [[ord(m1)for m1 in m] for m in msg]

def convert_to_binary(lst):
    return [["{0:b}".format(int(l1)) for l1 in m] for m in lst]

def convert_to_char(lst):
    return [[chr(int(d)) for d in dt] for dt in lst]

def convert_binary_to_int(lst):
    return [[str(int(str(d), 2)) for d in dt] for dt in lst]

def xor(k, m):
    print( [(word_k, word_m) for word_k, word_m in zip(k,m)] )
    return [ [str(int(i) ^ int(j)) for i,j in zip(word_k,word_m)] for word_k, word_m in zip(k,m)]

def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)

def get_ascii_key(k):
    k = ''.join(k)
    key = [k[0+i:8+i] for i in range(0, len(k), 8)]
    key = [[ ord( chr(int(k1, 2)) ) for k1 in key]]
    return key

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s : s[:-ord(s[len(s)-1:])]