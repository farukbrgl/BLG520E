import re
letters_to_numbers = {
    "A": "0", "B": "1", "C": "2", "D": "3", "E": "4", "F": "5",
    "G": "6", "H": "7", "I": "8", "J": "9", "K": "10", "L": "11",
    "M": "12", "N": "13", "O": "14", "P": "15", "Q": "16", "R": "17",
    "S": "18", "T": "19", "U": "20", "V": "21", "W": "22", "X": "23",
    "Y": "24", "Z": "25"
}

l_n = letters_to_numbers

f_ciphertext = open("ciphertext.txt", "r", newline='\n')
f_ciphertext_one_line = open("ciphertext_one_line.txt", "w")
f_ciphertext_to_numbers = open("ciphenumbers.txt", "w")
for line in f_ciphertext.readlines():
    for c in line:
        if c == "\n":
            pass
        else:
            print(l_n[c], c)
            f_ciphertext_to_numbers.write(str(l_n[c]) + "\n")
            # f_ciphertext_to_numbers.write(str(c) + ": " + str(l_n[c]) + "\n")
            f_ciphertext_one_line.write(str(c))

f_ciphertext.close()
f_ciphertext_to_numbers.close()
f_ciphertext_one_line.close()
lst = []
f_ciphertext_one_line_read = open("ciphertext_one_line.txt", "r")
indices_object = (re.finditer(
    "GVJ", (f_ciphertext_one_line_read.readlines()[0])))
indices = [index.start() for index in indices_object]
print(indices, "GJV")
