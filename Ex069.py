from random import randint
numeros_aleatorios = (randint(0,10),randint(0,10),randint(0,10),
                      randint(0,10),randint(0,10))
print(f'Eu sorteei os seguintes números:{numeros_aleatorios[0:]}')
print(f'O maior número foi : {max(numeros_aleatorios)}')
print(f'O menor número foi : {min(numeros_aleatorios)}')