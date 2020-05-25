war_line = str(input()).lower().split()
war_line.sort()


#s = input()

res1 = '' # результат - пустая строка

while len(war_line) > 0:
    a = 1 #счетчик while
    while len(war_line) > 1 and war_line[0] == war_line[1]:
        a += 1
        war_line = war_line[1:]
    res1 = war_line[0]
    print(res1, a, sep=' ')
    war_line = war_line[1:]

#print(res1, a, sep=' ')
'''for x in range(len(war_line) - 1, -1, -1):
     #счетчик одинаковых слов
    if x > 0 and war_line[x] == war_line[x - 1]:
        a += 1
    #elif x > 0 and war_line[x] != war_line[x + 1]:
        word = war_line[x]
    if x > 0 and war_line[x] != war_line[x - 1] and war_line[x] == war_line[x + 1]:
        print(word, a, sep=' ')
    else:
        print(war_line[x], a, sep=' ')'''



