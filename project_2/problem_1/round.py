def round(key, plaintext, sbox, perm):
    xored = key ^ plaintext
    print("xored", hex(xored))
    sboxed = sbox(xored)
    print("sboxed", hex(sboxed))
    permutated = perm(sboxed)
    print("permutated", hex(permutated))
    permutated_str = str(hex(permutated)[2:].zfill(4))
    return permutated_str
