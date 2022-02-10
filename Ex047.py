n = int(input('Qual número você deseja verificar? '))
t = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[31m',end=' ')
        t += 1
    else:
        print('\033[34m',end=' ')
    print('{}'.format(c),end=' ')
if t == 2:
    print('O número {} é um número primo.'.format(n))
else:
    print('O número {} não é um número primo.'.format(n))