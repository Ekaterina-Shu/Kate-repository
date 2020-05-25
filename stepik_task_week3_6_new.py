text = ''
with open('/Users/evshutova/Downloads/dataset_3363_3-20.txt') as inf:
    for line in inf:
        line = line.strip()
        text += line #сделали весь текст в одной строке
text = (text + ' ').lower() #чтобы правильно считалось последнее слово в цикле for + привели текст к 1 регистру
word, word1 = '', ''
count = 0 #счетчик
dictionary = {}
for i in range(len(text)):
    if text[i] !=' ':
        word = word + text[i] #вычленила слово
    else:
        for j in range(len(text)):
            if text[j] != ' ':
                word1 = word1 + text[j]
            else:
                if word1 == word:
                    count += 1
                word1 = ''
        if count in dictionary.keys() and word not in dictionary[count]:
            dictionary[count] += [word]
        else:
            dictionary[count] = [word]
        word = ''
        count = 0
key_list = [int(key) for key in dictionary.keys()] #intовый список кол-ва слов

print(min(dictionary[max(key_list)]), max(key_list))
