maior = 0
menor = 0
for g in range(1,6):
    peso = float(input('Digite o peso da {}° pessoa: '.format(g)))
    if g == 1:
        maior = peso
        menor = peso
    elif peso > maior:
         maior = peso
    elif peso < menor:
         menor = peso
print("O maior peso foi de {} kg".format(maior))
print('O menor peso foi de {} kg'.format(menor))


