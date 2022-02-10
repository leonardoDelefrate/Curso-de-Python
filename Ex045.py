s = 0
count = 0
for c in range(1,7,1):
    n = int(input('Digite o {}° número! '.format(c)))
    if n % 2 == 0:
       s = s + n
print('A soma de todos os números pares citados acima é de {}'.format(s))