def sbox_1(key):
    # key = 0xabcd
    str_key = str(hex(key)[2:].zfill(4))
    # key_list = list(map(str, str(hex(key)[2:].zfill(4))))
    letter_list = "0123456789abcdef"
    key_next = ""
    # print(str_key)

    for i in range(4):
        if str_key[i] == "0":
            key_temp = letter_list[1]
        elif str_key[i] == "1":
            key_temp = letter_list[9]
        elif str_key[i] == "2":
            key_temp = letter_list[6]
        elif str_key[i] == "3":
            key_temp = letter_list[13]
        elif str_key[i] == "4":
            key_temp = letter_list[7]
        elif str_key[i] == "5":
            key_temp = letter_list[3]
        elif str_key[i] == "6":
            key_temp = letter_list[5]
        elif str_key[i] == "7":
            key_temp = letter_list[15]
        elif str_key[i] == "8":
            key_temp = letter_list[2]
        elif str_key[i] == "9":
            key_temp = letter_list[12]
        elif str_key[i] == "a":
            key_temp = letter_list[14]
        elif str_key[i] == "b":
            key_temp = letter_list[10]
        elif str_key[i] == "c":
            key_temp = letter_list[4]
        elif str_key[i] == "d":
            key_temp = letter_list[11]
        elif str_key[i] == "e":
            key_temp = letter_list[8]
        elif str_key[i] == "f":
            key_temp = letter_list[0]

        key_next = key_next + key_temp
    key_next_hex = int(key_next, 16)
    # print(hex(key_next_hex))
    return key_next_hex


def sbox_2_3(key):
    # key = 0xabcd
    str_key = str(hex(key)[2:].zfill(4))
    # key_list = list(map(str, str(hex(key)[2:].zfill(4))))
    letter_list = "0123456789abcdef"
    key_next = ""
    # print(str_key)

    for i in range(4):
        if str_key[i] == "0":
            key_temp = letter_list[0]
        elif str_key[i] == "1":
            key_temp = letter_list[1]
        elif str_key[i] == "2":
            key_temp = letter_list[9]
        elif str_key[i] == "3":
            key_temp = letter_list[6]
        elif str_key[i] == "4":
            key_temp = letter_list[13]
        elif str_key[i] == "5":
            key_temp = letter_list[7]
        elif str_key[i] == "6":
            key_temp = letter_list[3]
        elif str_key[i] == "7":
            key_temp = letter_list[5]
        elif str_key[i] == "8":
            key_temp = letter_list[15]
        elif str_key[i] == "9":
            key_temp = letter_list[2]
        elif str_key[i] == "a":
            key_temp = letter_list[12]
        elif str_key[i] == "b":
            key_temp = letter_list[14]
        elif str_key[i] == "c":
            key_temp = letter_list[10]
        elif str_key[i] == "d":
            key_temp = letter_list[4]
        elif str_key[i] == "e":
            key_temp = letter_list[11]
        elif str_key[i] == "f":
            key_temp = letter_list[8]

        key_next = key_next + key_temp
    key_next_hex = int(key_next, 16)
    # print(hex(key_next_hex))
    return key_next_hex
