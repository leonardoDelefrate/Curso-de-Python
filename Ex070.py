valores = (int(input('Digite o primeiro valor')),
           int(input('Digite o segundo valor')),
           int(input('Digite o terceiro valor')),
           int(input('Digite o quarto valor')))

print(f'vezes que o 9 apareceu: {valores.count(9)}')
if(3 in valores):
    print(f'A posição do primeiro valor 3 é: {valores.index(3)}')
else:
    print('O valor 3 não foi digitado!')
print(f'Os números pares foram: ', end='')
for r in valores:
    if(r % 2 == 0):
        print(f'{r}',end=' ')
