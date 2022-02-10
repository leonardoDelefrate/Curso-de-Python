print('-----------------------------------')
print('Bem vindo a sequência de fibonacci!')
print('-----------------------------------')
quantidade = int(input('Digite a quantidade de termos que aparecerão na sequência: '))
cont = 3
termo1 = 0
termo2 = 1
print('{} ➙ {} ➙ '.format(termo1,termo2), end='')
while(cont <= quantidade):
    termo3 = termo1 + termo2
    termo1 = termo2
    termo2 = termo3
    print('{} ➙ '.format(termo3), end='')
    cont = cont + 1
print('FIM')

