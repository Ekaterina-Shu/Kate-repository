text = ''
with open('/Users/evshutova/Downloads/dataset_3363_3-23.txt') as inf:
    for line in inf:
        line = line.strip()
        text += line #сделали весь текст в одной строке
text = text.lower().split()
text.sort()
dictionary = {}
count = 0
word1 = ''
for word in text:
    if word in dictionary.keys():
        dictionary[word] += 1
    else:
        dictionary[word] = 1
for word in dictionary:
    if dictionary[word] > count:
        count = dictionary[word]
        word1 = word
print(word1, count)


'''dictionary = {}
count = 1

result = []
for i in range(len(text)):
    if text[i] in dictionary.keys():
        dictionary[text[i]] += 1
    else:
        dictionary[text[i]] = 1
    if i == 0:
        word1 = text[i]
    else:
        if text[i] < word1:
            word1 = text[i]


#print(dictionary)
print(word1)'''
'''dictionary_max = max(dictionary.values())
for word, count in dictionary.items():
    if count == dictionary_max:
        result.append(word)
print(min(result), dictionary_max)'''



