a = [int(j) for j in input().split()]
x = int(input())
if a.count(x) == 0:
    print('Отсутствует')
for i in range(len(a)):
    if a[i] == x:
        print(i, end=' ')