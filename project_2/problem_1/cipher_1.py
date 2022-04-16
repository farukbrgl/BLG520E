def key_schedules(key_hex):
    print(key_hex)
    key_list = map(bin, str(key_hex))
    print(key_list)
    key_15 = key_list[0] ^ key_list[2] ^ key_list[4] ^ key_list[5]
    key_shifted = [key_15] + key_list[:-1]
    print(key_shifted)

    return key_shifted


key_schedules()
