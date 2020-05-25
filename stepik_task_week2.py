a = int(input())
if a == 0:
    print(a)
    exit()
b = a # проверка на сумму равную 0
c = []  # список, в котором запоминаем все введенные числа
c.append(a)
while 1 == 1: #просто пытаюсь запустить цикл
    i = int(input())
    b = b + i
    c.append(i)
    if b == 0:
        res1 = sum([j ** 2 for j in c])
        break
print(res1)
'''for k in range(len(res1)):
    res1[k] = int(res1[k])
    print(res1[k])'''





