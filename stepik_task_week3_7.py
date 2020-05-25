mean_maths = 0
mean_phys = 0
mean_rus = 0
n = 0 #счетчик строк
result = open('/Users/evshutova/Downloads/reply_3363_4.txt', 'w')
with open('/Users/evshutova/Downloads/dataset_3363_4-3.txt') as t:
    for line in t:
        line = line.strip().split(';')
        line.append(' ')
        mean = (int(line[1]) + int(line[2]) + int(line[3]))/3
        print(mean)
        result.write(str(mean) + '\n')
        mean_maths = mean_maths + int(line[1])
        mean_phys = mean_phys + int(line[2])
        mean_rus = mean_rus + int(line[3])
        n += 1
print(mean_maths/n, mean_phys/n, mean_rus/n, sep= ' ')
result.write(str(mean_maths/n) + ' ' + str(mean_phys/n) + ' ' + str(mean_rus/n))




