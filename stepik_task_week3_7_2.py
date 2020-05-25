def dictionary_create(line1, line2):
    dictionary = {}
    for i in range(len(line1)):
        dictionary[line1[i]] = line2[i]
    return dictionary


def crypt(crypt_dictionary, line):
    for letter in line:
        letter = crypt_dictionary[letter]
        print(letter, end='')
    print()


alphabet_basic, alphabet_final, line_decrypt, line_encrypt = input(), input(), input(), input()
forward_dict = dictionary_create(alphabet_basic, alphabet_final)
backward_dict = dictionary_create(alphabet_final, alphabet_basic)
crypt(forward_dict, line_decrypt)
crypt(backward_dict, line_encrypt)

'''for letter in line_decrypt:
    letter = forward_dict[letter]
    print(letter, end='')
print()
for letter in line_encrypt:
    letter = backward_dict[letter]
    print(letter, end='')'''


#print(dictionary1)
#print(dictionary2)
