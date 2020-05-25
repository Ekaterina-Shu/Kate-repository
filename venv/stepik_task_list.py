s = input().split()
result = 0
res1 = 0
res2 = 0
res3 = 0
for i in range(len(s)):
    s[i] = int(s[i])
if len(s) == 1:  # если в строке 1 символ
    result = s[0]
    print(result)
    exit()
for i in range(len(s)):
    #s[i] = int(s[i])
    if i == 0: #обработка 1ого символа
        res1 = s[1] + s[len(s) - 1]
        print(res1, sep=' ', end=' ')
        continue
    if i == len(s) - 1:#обработка последнего символа
        res3 = s[len(s)-2] + s[0]
        print(res3, sep=' ', end=' ')
        continue
    #len(s) - 2 >= i > 0:#обработка символов между 1ым и последним
    res2 = s[i - 1] + s[i + 1]
    print(res2, sep=' ', end=' ')






