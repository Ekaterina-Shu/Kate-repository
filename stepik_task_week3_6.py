def get_key(d, value): # функция, возвращающая ключ по значению value
    for k, v in d.items():
        if v == value:
            return k
text = ''
with open('/Users/evshutova/Downloads/dataset_3363_3-17.txt') as inf:
    for line in inf:
        line = line.strip()
        text += line #сделали весь текст в одной строке
word = ''
word1 = ''
dictionary = {} # ВОПРОС: почему не работало с dictionary = () ?
value = 0 # счетчик кол-ва вхождений
text = text + ' ' #добавила пробел, чтобы цикл i считался с последним словом
for i in range(len(text)):
    if text[i] != ' ':
        word += text[i] #вычленили слово

    else:
        text1 = text.lower()
        for j in range(len(text1)):
            if text1[j] != ' ':
                word1 += text1[j]
            else:
                if word1 == word.lower():
                    value += 1
                word1 = ''

        dictionary[word] = value  # занесли в словарь соотношение "слово - сколько раз встречается"
        value = 0
        word = ''
print(get_key(dictionary, max(dictionary.values())), max(dictionary.values()))

print(dictionary)

print('abc' < 'bcd')


