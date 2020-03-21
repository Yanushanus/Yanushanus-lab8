#виведіть на екран елементи лінійного масиву (заданий користувачем) у
#зворотному порядку;
import numpy as np
while True:
    while True:
        try:
            n = int(input('Enter amount of digits')) #Задання розміру масиву
            a = np.zeros((n), dtype=int)
            b= np.zeros((n), dtype=int)
            break
        except ValueError:
            print('Only nums')

    for i in range(n): #введення чисел у масив
        a[i] = int(input('Enter your digits: '))
    print(a)

    for i in range(n): #заповнення пустого масиву значеннями с першого,але навпаки
        b[i]=a[n - 1 - i]
    print(f'New array:{b}')
    result = input('Do you want to retry.If yes enter 1 if no something else')
    if result == '1':
        continue
    else:
        break

