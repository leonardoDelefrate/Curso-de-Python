resposta = ''
soma = 0
cont = 0
while(resposta != 'N'):
    cont = cont + 1
    número = int(input('Digite um número'))
    soma = soma + número
    resposta = str(input('Deseja continuar?[S/N]:')).strip().upper()
    if(cont == 1):
        menor = número
        maior = número
    if(número > maior):
        maior = número
    elif(número < menor):
        menor = número
média = soma/cont
print(f'Você digitou {cont} valores')  #É possível usar esta forma ao invés de .format#
print('A média dos valores é: {}'.format(média))
print('O menor valor é {}'.format(menor))
print('O maior valor é {}'.format(maior))
