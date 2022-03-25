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

lndkl = list(letters_to_numbers.keys())
lndvl = list(letters_to_numbers.values())

letters_list = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
]

pt = 0


def beaufort_reverse(key, ct):
    pt = 0
    if key > ct:
        pt = key - ct
    elif ct > key:
        pt = key - ct + 26
    return pt


# to_dictionary = {"Bulgaria": 450, "Australia": 610, "Canada": 916}
#
# new_ke_lis = list(to_dictionary.keys())
# new_val = list(to_dictionary.values())
#
# new_pos = new_val.index(610)  # value from dictionary
# print("Get a key by value:", new_ke_lis[new_pos])


l_n = letters_to_numbers
f_plaintext = open("p2_plaintext_decry.txt", "w")
f_ciphernumbers = open("p2_encrypted_ciphernumbers.txt", "r")
line_number = 0
for line in f_ciphernumbers.readlines():
    if line_number % 5 == 0:
        p_t = beaufort_reverse(6, int(line))
        letter_p_t = lndkl[lndvl.index(str(p_t))]
        f_plaintext.write(letter_p_t)
    elif line_number % 5 == 1:
        p_t = beaufort_reverse(8, int(line))
        letter_p_t = lndkl[lndvl.index(str(p_t))]
        f_plaintext.write(letter_p_t)
    elif line_number % 5 == 2:
        p_t = beaufort_reverse(13, int(line))
        letter_p_t = lndkl[lndvl.index(str(p_t))]
        f_plaintext.write(letter_p_t)
    elif line_number % 5 == 3:
        p_t = beaufort_reverse(25, int(line))
        letter_p_t = lndkl[lndvl.index(str(p_t))]
        f_plaintext.write(letter_p_t)
    elif line_number % 5 == 4:
        p_t = beaufort_reverse(10, int(line))
        letter_p_t = lndkl[lndvl.index(str(p_t))]
        f_plaintext.write(letter_p_t)

    line_number = line_number + 1


def beaufort(key, pt):
    if key > pt:
        ct = key - pt
    elif pt > key:
        ct = key - pt + 26
    return ct
