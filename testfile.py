'''s = input()

res1 = '' # результат - пустая строка

while len(s) > 0:
    a = 1 #счетчик 2ого while
    while len(s) > 1 and s[0] == s[1]:
        a += 1
        s = s[1:]
    res1 = res1 + s[0] + str(a)
    s = s[1:]

print(res1)'''
#############################
import requests
with open('/Users/evshutova/Downloads/dataset_3378_3-5.txt') as t:
    text_url = t.readline().strip()
basic_url = 'https://stepic.org/media/attachments/course67/3.6.3/'
#    print(basic_url)
r = requests.get(text_url).text
print(r)
print(text_url)
while r[0] != 'W' and r[1] != 'e':
    new_url = basic_url + r
    r = requests.get(new_url).text

    print(new_url)
print(r)





