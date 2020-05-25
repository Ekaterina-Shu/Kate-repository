n = int(input())
x, y = 0, 0 #первая координата, вторая координата
commands = [input().split() for line in range(n)]
for word, distance in commands:
    if word == 'север':
        y += int(distance)
    if word == 'юг':
        y -= int(distance)
    if word == 'восток':
        x += int(distance)
    if word == 'запад':
        x -= int(distance)
print(x, y)

#print(commands)