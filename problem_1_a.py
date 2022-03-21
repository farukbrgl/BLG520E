import re
import math
from sympy import divisors

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


f_ciphertext_one_line_read = open("ciphertext_one_line.txt", "r")
text_line = f_ciphertext_one_line_read.readlines()[0]

f_occurs_all = open("occurs_all.txt", "w")
f_occurs_multi = open("occurs_multi.txt", "w")
f_factors = open("factors.txt", "w")

# indices_object = (re.finditer(
#     "GVJ", (f_ciphertext_one_line_read.readlines()[0])))
# indices = [index.start() for index in indices_object]
# print(indices, "GJV")

pattern_list = []
for j in range(3, 12):
    for i in range(3000 - j):
        if j == 3:
            pattern_ = text_line[i] + text_line[i + 1] + text_line[i + 2]
        elif j == 4:
            pattern_ = text_line[i] + text_line[i + 1] + \
                text_line[i + 2] + text_line[i + 3]
        elif j == 5:
            pattern_ = text_line[i] + text_line[i + 1] + \
                text_line[i + 2] + text_line[i + 3] + text_line[i + 4]
        elif j == 6:
            pattern_ = text_line[i] + text_line[i + 1] + \
                text_line[i + 2] + text_line[i + 3] + \
                text_line[i + 4] + text_line[i + 5]
        elif j == 7:
            pattern_ = text_line[i] + text_line[i + 1] + \
                text_line[i + 2] + text_line[i + 3] + \
                text_line[i + 4] + text_line[i + 5] + text_line[i + 6]
        elif j == 8:
            pattern_ = text_line[i] + text_line[i + 1] + \
                text_line[i + 2] + text_line[i + 3] + \
                text_line[i + 4] + text_line[i + 5] + \
                text_line[i + 6] + text_line[i + 7]
        elif j == 9:
            pattern_ = text_line[i] + text_line[i + 1] + \
                text_line[i + 2] + text_line[i + 3] + \
                text_line[i + 4] + text_line[i + 5] + \
                text_line[i + 6] + text_line[i + 7] + text_line[i + 8]
        elif j == 10:
            pattern_ = text_line[i] + text_line[i + 1] + \
                text_line[i + 2] + text_line[i + 3] + \
                text_line[i + 4] + text_line[i + 5] + text_line[i + 6] + \
                text_line[i + 7] + text_line[i + 8] + text_line[i + 9]
        elif j == 11:
            pattern_ = text_line[i] + text_line[i + 1] + \
                text_line[i + 2] + text_line[i + 3] + \
                text_line[i + 4] + text_line[i + 5] + text_line[i + 6] + \
                text_line[i + 7] + text_line[i + 8] + \
                text_line[i + 9] + text_line[i + 10]

        if pattern_ in pattern_list:
            pass
        else:
            pattern_list.append(pattern_)


print(pattern_list)
print(len(pattern_list))
factors_list = []
for pattern in pattern_list:
    # print(pattern)
    #     # pattern = text_line[i] + text_line[i + 1] + text_line[i + 2]
    indices_object = (re.finditer(pattern, (text_line)))
    indices = [index.start() for index in indices_object]
#     pattern_list.append(pattern)
#     # print(pattern, indices)
#
#     # all indices can be seen by uncomment below line
#     # and comment if block after that
#     # f_occurs_all.write(pattern + str(indices) + "\n")
#
    if len(indices) > 1:
        spacing = indices[1] - indices[0]
        f_factors.write(str(divisors(spacing)) + "\n")
        # f_occurs_multi.write(pattern + " " + str(spacing) + " "
        #                      + str(divisors(spacing)) + " "
        #                      + str(indices) + "\n")
        factors_list.append(divisors(spacing))
    else:
        pass

# print(factors_list)
f_factors.close()
f_occurs_all.close()
f_occurs_multi.close()
f_ciphertext_one_line_read.close()

search_list = []
p = 0
for string in factors_list:
    o = 0
    for factors in factors_list[p]:
        number = factors_list[p][o]
        if number in search_list:
            pass
        else:
            search_list.append(number)

        o = o + 1
    p = p + 1
search_list.sort()
print(search_list)
