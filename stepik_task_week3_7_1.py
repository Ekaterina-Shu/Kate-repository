def dictionary_add(dictionary_name, team1, team2):
    if team1 in dictionary_name.keys():
        dictionary_name[team1] += [team2]
    else:
        dictionary_name[team1] = [team2]
    return dictionary_name
n = int(input())
dict_victory, dict_losing, dict_draw = {}, {}, {}
games = [input().split(';') for i in range(n)]
teams_set = set()
for i in range(n):
    if int(games[i][1]) > int(games[i][3]): #если в строке победа у первой команды
        dictionary_add(dict_victory, games[i][0], games[i][2])
        dictionary_add(dict_losing, games[i][2], games[i][0]) #описываем проигрыш второй команды
    elif int(games[i][1]) == int(games[i][3]): #если в строке ничья
        dictionary_add(dict_draw, games[i][0], games[i][2])
        dictionary_add(dict_draw, games[i][2], games[i][0])
    else:
        dictionary_add(dict_victory, games[i][2], games[i][0]) #описываем победу второй команды
        dictionary_add(dict_losing, games[i][0], games[i][2]) #описываем проигрыш первой команды
    teams_set.add(games[i][0])
    teams_set.add(games[i][2])
count_victory, count_losing, count_draw = 0, 0, 0
for element in teams_set:
    #print(element, ':', sep='')
    #победы:
    if element in dict_victory.keys():
        count_victory = len(dict_victory[element])
    else:
        count_victory = 0
    #поражения:
    if element in dict_losing.keys():
        count_losing = len(dict_losing[element])
    else:
        count_losing = 0
    #ничья:
    if element in dict_draw.keys():
        count_draw = len(dict_draw[element])
    else:
        count_draw = 0
    #всего игр:
    games_number = count_victory + count_losing + count_draw
    #всего очков:
    games_points = count_victory * 3 + count_draw
    print(element, ':', sep='', end='')
    print(games_number, count_victory, count_draw, count_losing, games_points, sep=' ')


    '''print('count_victory', count_victory)
    print('count_losing', count_losing)
    print('count_draw', count_draw)'''

#print(teams_set)
'''print(games)
print(dict_victory)
print(dict_losing)
print(dict_draw)'''








