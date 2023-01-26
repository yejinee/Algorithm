def solution(matrix, b):
    if b==1:
        for x in range(len(matrix)):
            for y in range(len(matrix)):
                matrix[x][y] %= 1000
        return matrix

    half_matrix = solution(matrix, b//2)
    if b%2:
        return mutiple(mutiple(half_matrix, half_matrix), matrix)
    else:
        return mutiple(half_matrix, half_matrix)


def mutiple(matrix1, matrix2):
    matrix_size = len(matrix1)
    result = [[0]*matrix_size for _ in range(matrix_size)]

    for row in range(matrix_size):
        for col in range(matrix_size):
            value = 0
            for k in range(matrix_size):
                value += matrix1[row][k] * matrix2[k][col]
            result[row][col] = value % 1000
    return result


N, B = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
result = solution(A, B)
for res in result:
    print(*res)