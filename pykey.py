import hashlib
import string
import random
import os

chars = string.ascii_uppercase + string.digits + string.ascii_lowercase

def randString(length):
    string = ""
    for i in range(length):
        string += random.choice(chars)
    return string

def createRandKey(length, name):
    raw = randString(length)
    encoded = raw.encode()
    hash = hashlib.sha512(encoded)
    hex = hash.hexdigest()
    key = open(name+'.pyencrypt', 'w')
    key.write(hex)
    key.close()

def createKey(privateKey, name):
    encoded = privateKey.encode()
    hash = hashlib.sha512(encoded)
    hex = hash.hexdigest()
    key = open(name+'.pyencrypt', 'w')
    key.write(hex)
    key.close()

def readKey(name):
    key = open(name+'.pyencrypt', 'r')
    key_contents = key.read()
    key.close()
    return key_contents

def checkKey(privateKey, name):
    key = readKey(name)
    encoded = privateKey.encode()
    hash = hashlib.sha512(encoded)
    hex = hash.hexdigest()
    if key == hex:
        return True
    else:
        return False

def removeKey(name):
    os.remove(name+'.pyencrypt')
