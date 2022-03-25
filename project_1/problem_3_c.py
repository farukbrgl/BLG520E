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

f_ciphertext = open("p3_encrypted.txt", "r", newline='\n')
# f_ciphertext_one_line = open("ciphertext_one_line.txt", "w")
f_ciphertext_to_numbers = open("p3_encrypted_ciphernumbers.txt", "w")
for line in f_ciphertext.readlines():
    for c in line:
        if c == "\n":
            pass
        else:
            # print(l_n[c], c)
            f_ciphertext_to_numbers.write(str(l_n[c]) + "\n")
            # f_ciphertext_to_numbers.write(str(c) + ": " + str(l_n[c]) + "\n")
            # f_ciphertext_one_line.write(str(c))

f_ciphertext.close()
f_ciphertext_to_numbers.close()
# f_ciphertext_one_line.close()


f_ciphertext_one_line_read = open("p3_encrypted.txt", "r")
text_line = f_ciphertext_one_line_read.readlines()[0]

f_occurs_all = open("p3_occurs_all.txt", "w")
f_occurs_multi = open("p3_occurs_multi.txt", "w")
f_factors = open("p3_factors.txt", "w")

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

f_pattern_list = open("p3_pattern_list.txt", "w")
f_pattern_list.write(str(pattern_list))

f_pattern_list.close()

# print(pattern_list)
# print(len(pattern_list))
factors_list = []
f_occurs_multi.write("Pattern" + " | " + "occurs" + " | " + "spacing" + " | "
                     + "factors")

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
        f_occurs_multi.write(pattern + " " + str(indices) + " " + str(spacing) + " "
                             + str(divisors(spacing)) + " "
                             + "\n")
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
count_dict = {}
# print(search_list)
ab = 0
for k in range(1, len(search_list)):
    counter = 0
    search_number = search_list[k]
    for lm in range(len(factors_list)):
        if search_number in factors_list[lm]:
            counter = counter + 1
    count_dict.update({search_number: counter})
    # count_list.append(counter)

count_dict_sorted = dict(
    sorted(count_dict.items(), key=lambda x: x[1], reverse=True))
print(count_dict_sorted)


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


def frequency_show(ct):
    freq_count_dict = {}
    # print(search_list)
    for k in range(len(letters_list)):
        counter = 0
        search_letter = letters_list[k]
        counter = ct.count(search_letter)
        freq_count_dict.update({search_letter: counter})

    freq_count_dict_sorted = dict(
        sorted(freq_count_dict.items(), key=lambda x: x[1], reverse=True))

    print(freq_count_dict_sorted)
    return freq_count_dict_sorted


ct_k1 = []
ct_k2 = []
ct_k3 = []
ct_k4 = []
ct_k5 = []
f_ciphertext_one_line = open("p3_encrypted.txt", "r")
line = f_ciphertext_one_line.readline()
i = 0
for i in range(int(len(line) / 5)):
    ct_k1.append(line[5 * i + 0])
    ct_k2.append(line[5 * i + 1])
    ct_k3.append(line[5 * i + 2])
    ct_k4.append(line[5 * i + 3])
    ct_k5.append(line[5 * i + 4])
# print(ct_k1)
# print(ct_k2)
# print(ct_k3)
# print(ct_k4)
# print(ct_k5)

f_ciphertext_one_line.close()

freq_dict_k1 = frequency_show(ct_k1)
freq_dict_k2 = frequency_show(ct_k2)
freq_dict_k3 = frequency_show(ct_k3)
freq_dict_k4 = frequency_show(ct_k4)
freq_dict_k5 = frequency_show(ct_k5)

# ct =
# def frequency_analysis(freq_count_dict):
