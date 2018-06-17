a = raw_input('Give word for encrypting:')

while a != 'end':
    x = ''
    z = ''
    d = ''

    dict = {'q': 'AAAAA', 'w': 'BAAAA', 'e': 'BBAAA', 'r': 'BBBAA', 't': 'BBBBA', 'y': 'BBBBB',
            'u': 'ABBBB', 'i': 'AABBB', 'o': 'AAABB', 'p': 'AAAAB', 'a': 'ABBAB', 's': 'BAABA',
            'd': 'ABAAB', 'f': 'BABBA', 'g': 'ABBBA', 'h': 'BAAAB', 'j': 'BABAB', 'k': 'ABABA',
            'l': 'BBABB', 'z': 'AABAA', 'x': 'BABBB', 'c': 'ABAAA', 'v': 'AAABA', 'b': 'BBBAB',
            'n': 'ABABB', 'm': 'BABAA', ' ': 'BAABB'}

    for i in list(a):
        n = ord(i) + 3
        if n > 122:
            n = n - 26
        if n == 35:
            n = n - 3
        w = chr(n)
        z = z + w

        for j in range(len(x)):
            n = z[j]
            n = ord(n) + 1
            if n > 122:
                n = n - 24
            if n == 33:
                n = n - 1
            w = chr(n)
        z = z + w

        for k in range(len(z)):
            n = z[k]
            n = ord(n) + 2
            if n > 122:
                n = n - 25
            if n == 34:
                n = n - 2
            w = chr(n)
        z = z + w

    for i in list(z):
        if i in dict:
            x = x + dict[i]

    print x

    a = raw_input('Give word for encrypting:')