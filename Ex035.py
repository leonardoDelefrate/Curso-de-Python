from datetime import date
ano = int(input('Em que ano você nasceu? '))
idade = int(input('Quantos anos você tem? '))
atual = date.today().year
if idade < 18:
    print('Você precisa ter, no mínimo, 18 anos para realizar o alistamento')
    print('Ainda faltam {} anos para você se alistar'.format(18 - idade))
if idade == 18:
    print('Você deve se alistar imediatamente!')
if idade > 18:
    print('Você deveria ter se alistado há {} anos'.format(idade - 18))


