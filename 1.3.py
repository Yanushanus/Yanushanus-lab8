#виконайте добуток двох квадратних матриць 3*3, врахуйте розмірність.
#Результати множення елементів занесіть до нової матриці та виведіть її на екран;
import numpy as np
while True:
    while True:
        try:
            n, m = 3, 3 #Створення матриць
            a = np.zeros((n, m), dtype=int)
            b = np.zeros((n, m), dtype=int)
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
    new_el=0
    c=[]
    d=[]
    for i in range(0,m):
        for j in range(0,n):
            for k in range(0,n):
                new_el=new_el+a[i,k]*b[k,j]
            c.append(new_el)
            new_el=0
        d.append(c)
        c=[]
    print(f'Your new matrix \n{d}')
    result = input('Do you want to retry.If yes enter 1 if no something else')
    if result == '1':
        continue
    else:
        break