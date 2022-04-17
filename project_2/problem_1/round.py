def round(key, plaintext, sbox, perm):
    xored = key ^ plaintext
    print(xored)
    sboxed = sbox(xored)
    print(hex(sboxed))
    permutated = perm(sboxed)
    print(hex(permutated))
    return permutated
