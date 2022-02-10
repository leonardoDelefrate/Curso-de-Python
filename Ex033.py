num = int(input('\033[1;31mDigite o número inteiro que deseja converter\033[m '))
print('''Analise as opções abaixo. 
[1] binário
[2] octal
[3] hexadecimal''')
op = int(input('Escolha uma das opções para converter '))
print(' A opção escolhida foi : {} '.format(op))
if op == 1:
    print('O número {} em binário é: \033[1;31m{}\033[m '.format(num,bin(num)[2:]))
elif op == 2:
    print('O npumero {} em octal é: \033[1;31m{}\033[m '.format(num,oct(num)[2:]))
elif op == 3:
    print('O número {} em hexadecimal é: \033[1;31m{}\033[m '.format(num,hex(num)[2:]))
else:
    print('Operação inválida.')
