#бінарний пошук
import random
import numpy as np

while True:
    while True:
        try:
            n=int(input('Enter your length'))#заведення змінних та лічильника
            a=np.zeros(n,dtype=int)
            x=int(input('Enter num to find'))
            count = 0
            break
        except ValueError:
            print('Only nums')
    for i in range(n):#заповнення масиву значеннями
        a[i]=random.randint(0,15)
    a=sorted(a)
    print(f'Your array: {a}')
    l=0#ліва границя
    r=len(a)-1#права границя
    k=0
    for i in range (n):
        k=(l+r)//2#середина масиву
        count+=2
        if a[k]==x:#перевірка чи дорівнює серединне значення шуканому
            print(f'Your num {x} is on {k} position')
            break
        elif a[k]<x:#якщо серединне значення менше за шукане,ліва границя зміститься вправо
            count+=1
            l=k+1
        elif a[k]>x:#якщо серединне значення більше за шукане,права границя зміститься вліво
            count+=1
            r=k-1
        if i==n-1:#перевірка чи немає шуканого числа у масиві
            count+=1
            print('Your num wasn`t found')

    print(f'You have {count+1} times')
    result = input('Do you want to retry.If yes enter 1 if no something else')
    if result == '1':
        continue
    else:
        break
