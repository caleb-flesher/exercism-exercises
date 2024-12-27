# Using aenygma's solution and notes from commentors
import string 

def rotate(text, key):
    a2z = string.ascii_lowercase
    newchars = a2z[key % 26:] + a2z[:key % 26]
    trans = str.maketrans(a2z + a2z.upper(), newchars + newchars.upper())
    return text.translate(trans)