import collections

n = int(input())
dict_victory = collections.defaultdict(int)
dict_losing = collections.defaultdict(int)
dict_draw = collections.defaultdict(int)
games = [input().split(';') for i in range(n)]
teams_set = set()

for game in games:
    team1, score_team_1, team2, score_team2 = game #ВАЖНО СМОТРИ КАТЯ !!!!!!!!!!!!!!!!!!
    if int(score_team_1) > int(score_team2): #если в строке победа у первой команды
        dict_victory[team1] += 1
        dict_losing[team2] += 1 #описываем проигрыш второй команды
    elif int(score_team_1) == int(score_team2): #если в строке ничья
        dict_draw[team1] += 1
        dict_draw[team2] += 1
    else:
        dict_victory[team2] += 1 #описываем победу второй команды
        dict_losing[team1] += 1 #описываем проигрыш первой команды
    teams_set.add(team1)
    teams_set.add(team2)
for element in teams_set:
    count_victory = dict_victory[element]
    count_losing = dict_losing[element]
    count_draw = dict_draw[element]
    print(element, ':', sep='', end='')
    print(count_victory + count_losing + count_draw, count_victory, count_draw, count_losing, count_victory * 3 + count_draw, sep=' ')

print(dict_victory)
print(dict_losing)
print(dict_draw)







