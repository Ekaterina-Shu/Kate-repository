'''def f(m):
    return m * 2
n = int(input())
d = {}
for i in range(n):
    d[i] = int(input())
print(d)
for value in d.values():
    print(f(value))'''

'''def f(m):
    return m * 2
n = int(input())
d = {}
d1 = []
dfun = {} #пустой список для подсчета фунок
for i in range(n):
    d[i] = int(input())
    d1.append(d[i])
    d1.sort()
for i in range(len(d1)):
    if i != len(d1) - 1:
        if d[i] == d[i+1]:
            i += 1
        else:
            dfun[d1[i]] = f(d1[i])
            i += 1
    else:
        dfun[d1[i]] = f(d1[i])
for value in d.values():
    for key in dfun.keys():
        if value == key:
            print(dfun[key])'''

def f(m):
    return m * 2
n = int(input())
d = {}
for i in range(n):
    a = int(input())
    if a in d:
        print(d[a])
    else:
        d[a] = f(a)
        print(d[a])
#print(d)




