#у матриці 4*4, що задана користувачем замініть всі від’ємні елементи на 0.
import numpy as np
while True:
    while True:
        try:
            n, m = 4, 4 # створення матриць
            a = np.zeros((n, m), dtype=int)
            b=np.zeros((n, m), dtype=int)
            break
        except ValueError:
            print('Only nums')
    for i in range(n): #задання значень для першої матриці
        for j in range(m):
            a[i, j] = int(input(f'A[{i},{j}]='))
            b[i,j]=a[i,j] #копіювання значень першої матриці
            if b[i,j]<0:
                b[i,j]=0 # перетворення негативних значень у нуль
    print(f'Your matrix:\n{a}')
    print(f'Your new matrix without negative digits\n {b}')
    result = input('Do you want to retry.If yes enter 1 if no something else')
    if result == '1':
        continue
    else:
        break