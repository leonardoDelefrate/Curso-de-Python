f = str(input('Digite uma frase: ')).upper().strip()
p = f.split()
j = ''.join(p)
i = ''
for letra in range(len(j)-1,-1,-1):
    i += j[letra]
print('O inverso de {} é {}'.format(j,i))
if i == j:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo')