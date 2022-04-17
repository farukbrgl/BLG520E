def permutation_1_2(key):
    str_key = str(bin(key)[2:].zfill(16))
    # print(str_key)
    # key_list = [int(i) for i in f'{key:0{16}b}']
    # print(key_list)
    kl = str_key
    kln = kl[0] + kl[4] + kl[8] + kl[12] + kl[1] + kl[5] + kl[9] + kl[13] + \
        kl[2] + kl[6] + kl[10] + kl[14] + kl[3] + kl[7] + kl[11] + kl[15]
    # print(kln)
    # key_next = "".join(map(str, kln)).zfill(16)
    # print(key_next)
    # print(type("".join(map(str, key_next))))
    key_next = int(kln, 2)
    # print(hex(key_next_bin))
    return key_next


def permutation_3(plaintext):
    plaintext_next = plaintext
    return plaintext_next
