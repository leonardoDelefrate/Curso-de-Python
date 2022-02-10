from random import randint
from time import sleep
item = 'PEDRA','PAPEL','TESOURA'
comp = randint(0,2)
print('\033[4;36;40mBEM VINDO AO JOGO DO JOKENPO\033[m')
print('''Suas opções são
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
esc = int(input('''Escolha sua jogada !!!
'''))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print('Você escolheu {}'.format(item[esc]))
print('O computador escolheu {} !'.format(item[comp]))
if comp == 0 and esc == 0:
    print('O jogo empatou!')
elif comp == 0 and esc == 1:
    print('O jogador venceu!')
elif comp == 0 and esc == 2:
    print('O computador venceu!')
elif comp == 1 and esc == 0:
    print('O computador venceu!')
elif comp == 1 and esc == 1:
    print('O jogo empatou!')
elif comp == 1 and esc == 2:
    print('O jogador venceu!')
elif comp == 2 and esc == 0:
    print('O computador venceu!')
elif comp == 2 and esc == 1:
    print('O jogador venceu!')
elif comp == 2 and esc == 2:
    print('O jogo empatou!')


