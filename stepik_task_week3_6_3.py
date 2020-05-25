import requests
with open('/Users/evshutova/Downloads/dataset_3378_3-5.txt') as t:
    text_url = t.readline().strip()
    basic_url = 'https://stepic.org/media/attachments/course67/3.6.3/'
#    print(basic_url)
    r = requests.get(text_url).text.split()
    print(r)
    print(text_url)
    while r[0] != 'We':
        new_url = basic_url + r[0]
        r = requests.get(new_url).text.split()

        print(new_url)
        print(r)
with open('/Users/evshutova/Downloads/kate.txt', 'w') as w:
    a = ' '.join(r)
    w.write(a)
#    print('text_url', a)
#   print(*r)


