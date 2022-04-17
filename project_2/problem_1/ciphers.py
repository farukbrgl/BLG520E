from key_schedule import key_schedule
from sbox import sbox_1
from sbox import sbox_2_3
from permutation import permutation_1_2
from permutation import permutation_3
from round import round
# key_schedule(0xffff)
# sbox_1(0xabcd)
# sbox_2_3(0xabcd)
# permutation_1_2(0x1111)

plaintext = 0xabcd
key = 0xabcd


def cipher_1():
    plaintext_next = round(key, plaintext, sbox_1, permutation_1_2)
    for i in range(4):
        key_next = key_schedule(key)
        plaintext_next = round(key_next, plaintext_next,
                               sbox_1, permutation_1_2)

    ciphertext = plaintext_next
    print(hex(ciphertext))
    return ciphertext


def cipher_2():
    plaintext_next = round(key, plaintext, sbox_2_3, permutation_1_2)
    for i in range(4):
        key_next = key_schedule(key)
        plaintext_next = round(key_next, plaintext_next,
                               sbox_1, permutation_1_2)

    ciphertext = plaintext_next
    print(hex(ciphertext))
    return ciphertext


def cipher_3():
    plaintext_next = round(key, plaintext, sbox_2_3, permutation_3)
    for i in range(4):
        key_next = key_schedule(key)
        plaintext_next = round(key_next, plaintext_next,
                               sbox_1, permutation_1_2)

    ciphertext = plaintext_next
    print(hex(ciphertext))
    return ciphertext


cipher_1()
cipher_2()
cipher_3()
