numero = 0
print('------------------------------------------------')
print("PARA SAIR DO PROGRAMA, DIGITE UM VALOR NEGATIVO!")
print('------------------------------------------------')
while True:
    numero = int(input('Que número desejas fazer a tabuada? '))
    if(numero < 0):
        break
    else:
        for c in range(0,11,1):
            resultado = numero * c
            print(f'{numero} X {c} = {resultado}')
print('FIM DO PROGRAMA')