#/usr/bin/python
import math
def r_convert(no,base, digits  = "0123456789ABCDEF"):
    if no < base:
        return no
    else:
        rem = no % base
        return  str(r_convert( ((no - rem )/ base),base, digits  = "0123456789A\
BCDEF"))  + str(digits[rem])


def word_to_binary(input_sentence):
    final = ""
    for char in input_word:
        digit = ord(char)
        base_2 = r_convert(digit,2)
        final += str(base_2) 
    return final



        
        
        

