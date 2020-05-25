s = input().split()
s.sort()
res = []
i = 0
if s[i] == s[len(s) - 1] and len(s) > 1: #костыль для обработки ситуации когда одно и тоже число повторяется (1 1 1 1)
    res.append(s[i])
for i in range(len(s) - 1):
    if s[i] == s[i+1] and s[i-1] != s[i]:
        res.append(s[i])
for j in range(len(res)):
    res[j] = int(res[j])
    print(res[j], sep=' ', end=' ')


