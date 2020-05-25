def dictionary_add(dictionary_name, team):
    if team in dictionary_name:
        dictionary_name[team] += 1
    else:
        dictionary_name[team] = 1
    return dictionary_name

'''team1 = 'Локо'
dictionary_test = {}
dictionary_add(dictionary_test, team1)
dictionary_add(dictionary_test, team1)
print(dictionary_test)'''

n = int(input())
dict_victory, dict_losing, dict_draw = {}, {}, {}
games = [input().split(';') for i in range(n)]
teams_set = set()

for game in games:
    team1, score_team_1, team2, score_team2 = game #ВАЖНО СМОТРИ КАТЯ !!!!!!!!!!!!!!!!!!
    if int(score_team_1) > int(score_team2): #если в строке победа у первой команды
        dictionary_add(dict_victory, team1)
        dictionary_add(dict_losing, team2) #описываем проигрыш второй команды
    elif int(score_team_1) == int(score_team2): #если в строке ничья
        dictionary_add(dict_draw, team1)
        dictionary_add(dict_draw, team2)
    else:
        dictionary_add(dict_victory, team2) #описываем победу второй команды
        dictionary_add(dict_losing, team1) #описываем проигрыш первой команды
    teams_set.add(team1)
    teams_set.add(team2)
for element in teams_set:
    if element in dict_victory:
        count_victory = dict_victory[element]
    else:
        count_victory = 0
    if element in dict_losing:
        count_losing = dict_losing[element]
    else:
        count_losing = 0
    if element in dict_draw:
        count_draw = dict_draw[element]
    else:
        count_draw = 0
    print(element, ':', sep='', end='')
    print(count_victory + count_losing + count_draw, count_victory, count_draw, count_losing, count_victory * 3 + count_draw, sep=' ')

print(dict_victory)
print(dict_losing)
print(dict_draw)







