import collections


students_dict = collections.defaultdict(list)
with open('/Users/evshutova/Downloads/dataset_3380_5-3.txt') as text:
    for line in text:
        line = line.split()
        class_stu, surname, height = line
        students_dict[int(class_stu)].append(int(height))
for class_stu in range(1, 12):
    if class_stu in students_dict:
        result = sum(students_dict[class_stu]) / len(students_dict[class_stu])
        print(class_stu, result)
    else:
        print(class_stu, '-')



