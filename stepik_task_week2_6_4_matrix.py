matrix = []
matrix_result = []
finish_index = input()
while finish_index != 'end':
    line = [int(s) for s in finish_index.split()]
    matrix.append(line)
    finish_index = input()
len_x = len(matrix)
len_y = len(matrix[0])
print(len_x)
print(len_y)
matrix_result = [['*' for x in range(len_y)] for y in range(len_x)]

for i in range(len_x):
    for j in range(len_y):
        '''if len_x == 0:
            matrix_result[i][j] = matrix[]
            #or len_y == 0:
        else:'''
        if i != 0 and j != 0 and i != len_x - 1 and j != len_y - 1:
            matrix_result[i][j] = matrix[i - 1][j] + matrix[i + 1][j] + matrix[i][j + 1] + matrix[i][j - 1]
        elif i == 0 and j == 0:
            matrix_result[i][j] = matrix[i + 1][j] + matrix[i][j + 1] + matrix[i][len_y - 1] + matrix[len_x - 1][j]
        elif i == 0 and j == len_y - 1:
            matrix_result[i][j] = matrix[i][j - 1] + matrix[i + 1][j] + matrix[i][j - (len_y - 1)] + matrix[len_x - 1][j]
        elif i == len_x - 1 and j == 0:
            matrix_result[i][j] = matrix[i - 1][j] + matrix[i][j + 1] + matrix[i - (len_x - 1)][j] + matrix[i][j + len_y - 1]
        elif i == len_x - 1 and j == len_y - 1:
            matrix_result[i][j] = matrix[i][j - 1] + matrix[i - 1][j] + matrix[i][j - (len_y - 1)] + matrix[i - (len_x - 1)][j]
        elif i == 0 and 0 < j < len_y - 1:
            matrix_result[i][j] = matrix[i][j + 1] + matrix[i][j - 1] + matrix[i + 1][j] + matrix[i - 1][j]
        elif i == len_x - 1 and 0 < j < len_y - 1:
            matrix_result[i][j] = matrix[i][j + 1] + matrix[i][j - 1] + matrix[i - 1][j] + matrix[i - (len_x - 1)][j]
        elif 0 < i < len_x - 1 and j == 0:
            matrix_result[i][j] = matrix[i + 1][j] + matrix[i - 1][j] + matrix[i][j + 1] + matrix[i][j + (len_y - 1)]
        elif 0 < i < len_x - 1 and j == len_y - 1:
            matrix_result[i][j] = matrix[i][j - 1] + matrix[i - 1][j] + matrix[i + 1][j] + matrix[i][j - (len_y - 1)]

        #else:
            #matrix_result[i][j] = '!'
for line in matrix_result:
    print(*line)
#print(matrix_result)