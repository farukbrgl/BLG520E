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

plaintext = 0x0000
key = 0x0000


def cipher_1(plaintext, key):
    for i in range(3):
        key = key_schedule(key)
        plaintext_next = round(key, plaintext, sbox_1, permutation_1_2)
        print(round.sbox.str_key)
    ciphertext = plaintext_next
    print(ciphertext)

    return ciphertext


def cipher_2(plaintext, key):
    for i in range(3):
        key = key_schedule(key)
        plaintext = round(key, plaintext, sbox_2_3, permutation_1_2)

    ciphertext = plaintext
    print(ciphertext)
    return ciphertext


def cipher_3(plaintext, key):
    for i in range(3):
        key = key_schedule(key)
        plaintext = round(key, plaintext, sbox_2_3, permutation_3)

    ciphertext = plaintext
    print(ciphertext)
    return ciphertext


cipher_1(plaintext, key)
cipher_2(plaintext, key)
cipher_3(plaintext, key)
