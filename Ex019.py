nome = str(input("Escreva seu nome")).strip()
print(nome, 'escrito em maiúsculo fica {}'.format(nome.upper()))
print(nome, 'escrito em minúsculo fica {}'.format(nome.lower()))
print(nome, 'tem, ao todo, {} letras.'.format(len(nome) - nome.count(' ')))
print('O primeiro nome de {} possui {} letras.'.format(nome,nome.find(' ')))

