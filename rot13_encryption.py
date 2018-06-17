lexi = raw_input("Give word for ROT13:")
encrypted_word = ''

for i in list(lexi):
    m = ord(i)
    y = ord(i) + 13
    if y > 122:
        for s in range(13):
            m = m + 1
            if m > 122:
                diff = 13 - s
                fin = 96 + diff
                encrypted_word = encrypted_word + chr(fin)
                break
    else:
        encrypted_word = encrypted_word + chr(y)

print encrypted_word