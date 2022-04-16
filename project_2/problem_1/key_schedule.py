def key_schedule(key):
    key_shifted = key >> 1
    key_str = str(bin(key))
    key_0 = int(key_str[-1])
    key_2 = int(key_str[-3])
    key_4 = int(key_str[-5])
    key_5 = int(key_str[-6])
    key_15 = key_0 ^ key_2 ^ key_4 ^ key_5
    key_next = key_shifted + key_15 * 2**15
    # print(bin(key))
    # print(bin(key_shifted))
    # print(bin(key_15))
    # print(bin(key_next))
    # print((key))
    # print((key_shifted))
    # print((key_15))
    # print((key_next))
    print(hex(key_next))
    print(hex(key))
    # key_bin = bin(key_hex)
    # print(key_bin)
    # key_list = list(map(int, str(key_bin)))
    # print(key_list)
    # key_15 = key_list[0] ^ key_list[2] ^ key_list[4] ^ key_list[5]
    # key_shifted = [key_15] + key_list[:-1]
    # print(key_shifted)
    return key_next
