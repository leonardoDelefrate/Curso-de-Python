from random import randint
print('---------------------')
print('JOGO DO PAR OU ÍMPAR')
print('---------------------')
cont = 0
p_i = ' '
while True:
    while(p_i not in 'PpIi'):
        p_i = str(input('Você quer PAR ou ÍMPAR [p/i]? ')).upper().strip()
    jogador = int(input('Qual número você deseja jogar? '))
    comp = randint(0,100)
    if((jogador + comp) % 2 == 0 and p_i == 'P'):
        print(f'O computador escolheu {comp}!')
        print(f'O total é {jogador + comp}')
        print('Você venceu!')
        print('Vamos jogar novamente...')
        cont = cont + 1
    elif((jogador + comp) % 2 > 0 and p_i == 'I'):
        print(f'O computador escolheu {comp}!')
        print(f'O total é {jogador + comp}')
        print('Você venceu!')
        print('Vamos jogar novamente...')
        cont = cont + 1
    if ((jogador + comp) % 2 == 0 and p_i == 'I'):
        print(f'O computador escolheu {comp}!')
        print(f'O total é {jogador + comp}')
        print('------------')
        print('Você perdeu!')
        print('------------')
        break
    elif ((jogador + comp) % 2 > 0 and p_i == 'P'):
        print(f'O computador escolheu {comp}!')
        print(f'O total é {jogador + comp}')
        print('------------')
        print('Você perdeu!')
        print('------------')
        break
if(cont == 1):
    print(f'Você venceu apenas {cont} vez!')
elif(cont > 1):
    print(f'Você venceu {cont} vezes seguidas!')
elif(cont == 0):
    print('Você não venceu nenhuma vez!')