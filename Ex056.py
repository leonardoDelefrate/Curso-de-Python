print('-------------')
print('Gerador de PA')
print('-------------')
primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão: '))
cont = 1
termo = primeiro
total = 0
resposta = 10
print('{} ➝ '.format(primeiro), end='')
while(resposta != 0):
    total = total + resposta
    while(cont <= total):
        termo += razao
        cont += 1
        print('{} ➝ ' .format(termo), end='')
    print('PAUSA')
    resposta = int(input('Quantos termos você deseja mostrar a mais?'))
print('FIM !')