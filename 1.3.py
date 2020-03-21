#виконайте добуток двох квадратних матриць 3*3, врахуйте розмірність.
#Результати множення елементів занесіть до нової матриці та виведіть її на екран;
import numpy as np
while True:
    while True:
        try:
            n, m = 3, 3 #Створення матриць
            a = np.zeros((n, m), dtype=int)
            b = np.zeros((n, m), dtype=int)
            c=np.zeros((n, m), dtype=int)
            break
        except ValueError:
            print('Only nums')
    for i in range(n): #Задання значень першій матриці
        for j in range(m):
            a[i, j] = int(input(f'A[{i},{j}]='))
    print(f'Matrix A: \n{a}')
    for i in range(n): # задання значень другій матриці
        for j in range(m):
            b[i, j] = int(input(f'B[{i},{j}]='))
    print(f'Matrix B: \n{b}')
    for i in range(n):
        for j in range(m):
            c[0,0]=a[0,0]*b[0,0]+a[0,1]*b[1,0]+a[0,2]*b[2,0]
            c[0,1]=a[0,0]*b[0,1]+a[0,1]*b[1,1]+a[0,2]*b[2,1]
            c[0,2]=a[0,0]*b[0,2]+a[0,1]*b[1,2]+a[0,2]*b[2,2]
            c[1,0]=a[1,0]*b[0,0]+a[1,1]*b[1,0]+a[1,2]*b[2,0]
            c[1,1]=a[1,0]*b[0,1]+a[1,1]*b[1,1]+a[1,2]*b[2,1]
            c[1,2]=a[1,0]*b[0,2]+a[1,1]*b[1,2]+a[1,2]*b[2,2]
            c[2,0]=a[2,0]*b[0,0]+a[2,1]*b[1,0]+a[2,2]*b[2,0]
            c[2,1]=a[2,0]*b[0,1]+a[2,1]*b[1,1]+a[2,2]*b[2,1]
            c[2,2]=a[2,0]*b[0,2]+a[2,1]*b[1,2]+a[2,2]*b[2,2]
    print(f'Matrix of multiplication: \n {c}')
    result = input('Do you want to retry.If yes enter 1 if no something else')
    if result == '1':
        continue
    else:
        break