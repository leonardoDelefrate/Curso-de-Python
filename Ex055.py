print('-------------')
print('Gerador de PA')
print('-------------')
primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão: '))
cont = 1
termo = primeiro
print('{} ➝ '.format(primeiro), end='')
while(cont <= 9):
    termo += razao
    cont += 1
    print('{} ➝ ' .format(termo), end='')
print('FIM')