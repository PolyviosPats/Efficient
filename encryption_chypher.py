lexi = raw_input("Give word for Encryption:")
step = int(input("Give step:"))
encrypted_word = ''
while step > -5 and step > 5:
    step = int(input("Give step between -5 <> 5:"))
for i in list(lexi):            
    m = ord(i)
    y = ord(i) + step
    if y > 122:
        for s in range(step):
            m = m + 1
            if m > 122:
                diff = step - s
                fin = 96 + diff
                encrypted_word = encrypted_word + chr(fin)
                break
    else:
        encrypted_word = encrypted_word + chr(y)
        
print encrypted_word

