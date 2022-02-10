print('='*30)
print('{:^30}'.format('BANCO'))
print('='*30)
valor = int(input('Que valor você quer sacar? R$ '))
total = valor
céd = 100
totcéd = 0
while True:
    if(total >= céd):
        total -= céd
        totcéd += 1
    else:
        if(totcéd > 0 and totcéd == 1):
            print(f'Total de {totcéd} cédula de R${céd}')
        if (totcéd > 0 and totcéd > 1):
            print(f'Total de {totcéd} cédulas de R${céd}')
        if(céd == 100):
            céd = 50
        elif(céd == 50):
            céd = 20
        elif(céd == 20):
            céd = 10
        elif (céd == 10):
            céd = 1
        totcéd = 0
        if(total == 0):
            break
print('='*30)
print('FIM')