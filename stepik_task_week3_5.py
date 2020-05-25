with open('/Users/evshutova/Downloads/dataset_3363_2-2.txt') as inf:
    line = inf.readline().strip()
letter = list(line)


'''letter = ['y', '1', '2', 'z', '1', '2', 'l', '1', '2']
a = ''
b = []
num = ''

for i in range(len(letter)):
    if str(letter[i]).isdigit() == False:
        if a != '':
            for j in range(len(b)):
                num = num + str(b[j])
            k = int(num)
            for j in range (k):
                print(a, end= '')
        a = letter[i]
        b = []
        num = ''
    else:
        b.append(letter[i])
for j in range(len(b)):
    num = num + str(b[j])
k = int(num)
for j in range(k):
    print(a, end='')'''

def count_num(b, a):
    num = ''
    for j in range(len(b)):
        num = num + str(b[j])
    k = int(num)
    for j in range(k):
        print(a, end='')

a = ''
b = []

for i in range(len(letter)):
    if str(letter[i]).isdigit() == False:
        if a != '':
            count_num(b, a)
        a = letter[i]
        b = []
        num = ''
    else:
        b.append(letter[i])
count_num(b, a)
#with open('/Users/evshutova/Downloads/dataset.txt', 'w') as ouf:


















#print(str(letter[0]).isdigit())
#print(letter[0].isdigit)


