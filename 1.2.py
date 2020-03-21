#виведіть на екран транспоновану матрицю 3*3 (початкова матриця задана
#користувачем).
import numpy as np
while True:
    while True:
        try:
            n, m = 3, 3 # Створення матриць
            a = np.zeros((n, m), dtype=int)
            b = np.zeros((m, n), dtype=int)
            break
        except ValueError:
            print('Only nums')

    for i in range(n): #задання першій матриці значення
        for j in range(m):
            a[i, j] = int(input(f'A[{i},{j}]='))
    print(f'Your matrix: \n {a}')
    for i in range(n): # транспонування матриці
        for j in range(m):
            new = a[j, i]
            b[i, j] = new
    print(f'Your new matrix: \n {b}')
    result = input('Do you want to retry.If yes enter 1 if no something else')
    if result == '1':
        continue
    else:
        break

