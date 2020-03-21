#лінійний пошук
import random
import numpy as np
while True:
    while True:
        try:
            n=int(input('Enter length of array'))
            a=np.zeros(n,dtype=int)
            x = int(input('Enter which number you want to find: '))
            count = 0  # заведення лічильника
            break
        except ValueError:
            print('Only nums')
    for i in range(n):#Заповнення масиву числами
         a[i]=random.randint(0,5)
    print(f'Your array \n{a}')

    for i in range (n):#перебір чисел масиву
        count+=2
        if a[i]==x:#перевірка чи є число на даній ітерації шуканим числом
            print(f'Your number {x} is on {i} position')
            break
        else:
            count+=1
            print('No num like you want')

    print(f'You have {count+1} times')
    result = input('Do you want to retry.If yes enter 1 if no something else')
    if result == '1':
        continue
    else:
        break
