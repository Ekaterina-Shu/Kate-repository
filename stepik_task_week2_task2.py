n = int(input())
a = [] #пустой список, куда буду заносить выводимые цифры
i = 1 #цифры в списке, начинается с 1
while len(a) < n:
    if a.count(i) >= i:
        i += 1
    a.append(i)
print(*a)