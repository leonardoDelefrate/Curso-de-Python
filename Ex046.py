p = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite o valor da razão: '))
en = p + (10-1) * r
print('='* 20,'10 TERMOS DA PA!','='*20)
for c in range(p,en,r):
    print('{}'.format(c), end=',' )