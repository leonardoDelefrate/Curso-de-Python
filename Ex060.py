somavalor = 0
valor = 0
cont = 0
while(valor != 999):
    valor = int(input('Digite um valor [999 para parar!]: '))
    if(valor == 999):
        break
    somavalor = somavalor + valor
    cont += 1
print(f'Você digitou {cont} números e a soma dos valores é de: {somavalor}')
