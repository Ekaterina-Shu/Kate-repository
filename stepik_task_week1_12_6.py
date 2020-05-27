n = int(input())
result = n % 100
if result <= 9:
    if result == 1:
        print(n, 'программист')
    elif 2 <= result <= 4:
        print(n, 'программиста')
    else:
        print(n, 'программистов')
elif 10 <= result <= 20:
    print(n, 'программистов')
else:
    result = result % 10
    if result <= 9:
        if result == 1:
            print(n, 'программист')
        elif 2 <= result <= 4:
            print(n, 'программиста')
        else:
            print(n, 'программистов')
    elif 10 <= result <= 20:
        print(n, 'программистов')




#print(2 % 100)