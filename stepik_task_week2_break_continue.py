'''a = []
while True:
    num = int(input())
    if num < 10:
        continue
    if 10 <= num <= 100:
        a.append(num)
    else:
        break
print(*a, sep= '\n')'''


while True:
    num = int(input())
    if num > 100:
        break
    if num < 10:
        continue
    print(num)
