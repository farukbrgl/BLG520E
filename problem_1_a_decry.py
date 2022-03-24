import re
# import math
from sympy import divisors

letters_to_numbers = {
    "A": "0", "B": "1", "C": "2", "D": "3", "E": "4", "F": "5",
    "G": "6", "H": "7", "I": "8", "J": "9", "K": "10", "L": "11",
    "M": "12", "N": "13", "O": "14", "P": "15", "Q": "16", "R": "17",
    "S": "18", "T": "19", "U": "20", "V": "21", "W": "22", "X": "23",
    "Y": "24", "Z": "25"
}

letters_list = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
]

l_n = letters_to_numbers
f_plaintext = open("plaintext_decry.txt", "w")
f_ciphernumbers = open("ciphernumbers.txt", "r")
line_number = 0
for line in f_ciphernumbers.readlines():
    if line_number == (5 * line_number + 0):
        print(line)
    line_number = line_number + 1


def beaufort(key, pt):
    if key > pt:
        ct = key - pt
    elif pt > key:
        ct = key - pt + 26
    return ct


def beaufort_reverse(key, ct):
    if key > ct:
        pt = key - ct
    elif ct > key:
        pt = key - ct + 26
    return pt
