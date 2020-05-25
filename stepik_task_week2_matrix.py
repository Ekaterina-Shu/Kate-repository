matrix = []
input_str = input()
while input_str != 'end':
    line = [int(i) for i in input_str.split()]
    matrix.append(line)
    input_str = input()
a_row = len(matrix)
b_col = len(matrix[0])
for i in range(a_row):
    for j in range(b_col):
        if  0 < i < a_row - 1 and 0 < j < b_col - 1:
            k = int(matrix[i - 1][j])
            l = int(matrix[i + 1][j])
            m = int(matrix[i][j - 1])
            n = int(matrix[i][j + 1])
            #print(k, l, m, n, sep=' ')
            matrix[i][j] = k + l+ m + n #int(matrix[i - 1][j]) + int(matrix[i + 1][j]) + int(matrix[i][j - 1]) + int(matrix[i][j + 1])
        else:
            matrix[i][j] = 0
        print(matrix[i][j], end= ' ')
    print()