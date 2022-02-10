somavalor = 0
valor = 0
cont = 0
while(valor != 999):
    valor = int(input('Digite um valor [999 para parar!]: '))
    somavalor = somavalor + valor
    cont += 1
print('Você digitou {} números e a soma dos valores é de: {}'.format(cont - 1,somavalor - 999))