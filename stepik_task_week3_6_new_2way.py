text = ''
with open('/Users/evshutova/Downloads/dataset_3363_3-20.txt') as inf:
    for line in inf:
        line = line.strip()
        text += line #сделали весь текст в одной строке
text = text.lower().split()
dictionary = {}
count = 1
result = []
for i in range(len(text)):
    if text[i] in dictionary.keys():
        dictionary[text[i]] += 1
    else:
        dictionary[text[i]] = 1
dictionary_max = max(dictionary.values())
for word, count in dictionary.items():
    if count == dictionary_max:
        result.append(word)
print(min(result), dictionary_max)



#    print(word, count, end=';')
#print()
#print(dictionary.items())
#print(dictionary)

#    if count == max(dictionary.values()):
#        print(dictionary[word] = count)


#a = max(dictionary.values())
#print(dictionary)
#print(a)


