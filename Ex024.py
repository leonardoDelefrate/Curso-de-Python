import random
computador = random.randint(0,5)
print('-=-' * 20)
print('                 O JOGO IRÁ COMEÇAR           '.title())
print('-=-' * 20)
numero = int(input('Digite um número inteiro entre 0 e 5'))
if numero == computador:
    print('Parabéns, você ganhou')
else:
    print('Seu cretino, você perdeu miseravelmente')
