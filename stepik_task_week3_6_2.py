'''import requests
n = 0
with open('/Users/evshutova/Downloads/dataset_3378_2-2.txt') as t, open('/Users/evshutova/Downloads/kate.txt', 'w') as w:
    text_url = t.readline().strip()
    print(text_url)
    r = requests.get(text_url)
    print(r.text)
    w.write(r.text)
    a = r.text
    print(a)
with open('/Users/evshutova/Downloads/kate.txt') as w:
    for line in w:
        n +=1
print(n)'''
import requests
with open('/Users/evshutova/Downloads/dataset_3378_2-3.txt') as t:
    text_url = t.readline().strip()
    r = requests.get(text_url).text.count('\n')
    print(r)
