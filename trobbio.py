    print("Введите количество строк")
    n=int(input())
    print("Введите количество столбцов")
    m=int(input())
    print("Введите значения матрицы по строкам")
    matrix=[list(map(float, input().split())) for _ in range(n)]
    print("Столбцы:")
    for j in range(m):
        print([matrix[i][j] for i in range(n)])