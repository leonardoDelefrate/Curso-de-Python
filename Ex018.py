import random
n1 = str(input('nome do primeiro aluno'))
n2 = str(input('nome do segundo aluno'))
n3 = str(input('nome do terceiro aluno'))
n4 = str(input('nome do quarto aluno'))
n5 = str(input('nome do quinto aluno'))
n6 = str(input('nome do sexto aluno'))
n7 = str(input('nome do sétimo aluno'))
n8 = str(input('nome do oitavo aluno'))
n9 = str(input('nome do nono aluno'))
lista = [n1,n2,n3,n4,n5,n6,n7,n8,n9]
random.shuffle(lista)
print(' A ordem de apresentação é:')
print(lista)
