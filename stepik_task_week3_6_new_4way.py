text = ''
with open('/Users/evshutova/Downloads/dataset_3363_3-24.txt') as inf:
    for line in inf:
        line = line.strip()
        text += line #сделали весь текст в одной строке
text = text.lower().split()
dictionary = {}
max_count = 0
min_word = None
for word in text:
    if word in dictionary:
        dictionary[word] += 1
    else:
        dictionary[word] = 1
    if dictionary[word] == max_count:
        if word < min_word:
            min_word = word
    if dictionary[word] > max_count:
        min_word = word
        max_count = dictionary[word]

print(min_word, max_count)
print(dictionary)







