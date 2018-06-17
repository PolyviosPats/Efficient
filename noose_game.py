l = []
ln = []
x = ''
pro = 0
word = raw_input('Give word for gallows:')
G_list = list(word)
for i in range(len(G_list)):
    if i == 0: l.append(G_list[i])
    elif i == len(G_list) - 1: l.append(G_list[i])
    else:
        w = '_'
        l.append(w)
    x = x + l[i]
print x
gr = raw_input('Give letter for gallows:')
while len(gr) > 1:
    gr = raw_input('Give one letter for gallows:')
while l != G_list:
    print 20 * '-'
    print 20 * ' '
    w = ''
    if gr not in ln: ln.append(gr,)
    for i in range(1, len(G_list) - 1):
        if gr == G_list[i]:
            l[i] = gr
    for st in l: w = w + st
    print w
    print len(w) * '-'
    print len(w) * ' '
    if gr not in G_list:
        print 'This letter does not exist in the gallows'
        print '-----------------------------------------'
        print '                                         '
        pro = pro + 1
    print 'Letters you gave', ln
    print '----------------'
    print '                '
    if word == w and pro == 0:
        print 'Amazing you are very good you found the word with the first try'
        break
    elif pro == 10:
        print 'You do not found the word you have been useless'
        break
    elif word == w:
        print 'Congratulations you found the word with', pro, 'tries'
        break
    gr = raw_input('Give letter for gallows:')
    while len(gr) > 1:
        gr = raw_input('Give one letter for gallows:')
