d = int(input())
words_mistakes_used = set() #тут храню "выведенные" слова-ошибки
words = {input().lower() for i in range(d)} #тут храню "известные" слова
'''for i in range(d): #можно ли этот for засунуть в list comprehension?
    word = input().lower()
    words.add(word)'''
l = int(input())
lines = [input().lower().split() for j in range(l)]
for line in lines:
    for word in line:
        if word not in words and word not in words_mistakes_used:
            print(word)
            words_mistakes_used.add(word)