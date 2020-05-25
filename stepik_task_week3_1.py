def modify_list(l):
#l = [int(l[i]) for i in range(len(l))]
    for i in range(len(l)-1, -1, -1):
        if l[i] % 2 != 0:
            #if i != len(l) - 1 and l[i + 1] in l:
            del l[i]
            #else:
                #l = l[:i]
            #i -= 1
        else:
            l[i] = l[i]//2
            #i -= 1

lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)


'''lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)'''






