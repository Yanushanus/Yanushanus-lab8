#Підрядок
while True:
    s=input('Enter your sentence:')
    s1=input('Enter what pattern you want to find:')
    i=-1
    j=0
    count=0
    while (j < len(s1)) and i < (len(s) - len(s1)):
        j = 0
        i += 1
        count += 2
        while j < len(s1) and s1[j] == s[i + j]:
            j += 1
            count += 2
    if j==len(s1):
        print(f'Your pattern is on {i} position')
    else:
        print('Your pattern wasn`t found')
    print(f'You have {count + 1} times')
    result = input('Do you want to retry.If yes enter 1 if no something else')
    if result == '1':
        continue
    else:
        break
