nome= input('Diga um nome')
print(' Olá senhor{}.É um prazer te-lo aqui conosco, por favor, confira suas notas abaixo'.format(nome))
P1= int(input('Digite o valor da P1'))
P2= int(input('Digite o valor da P2'))
m= (P1+P2)/2
print('{}, percebemos que suas notas no primeiro bimestre foram {} na P1 e {} na P2,portanto,sua média é de {}'.format(nome,P1,P2,m))