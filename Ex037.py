from datetime import date
ano = int(input('Em que ano você nasceu? '))
idade = (date.today().year) - ano
if idade <=9:
    print('Você está na categoria MIRIM!')
elif idade <= 14:
    print('Você está na categoria INFANTIL!')
elif idade <=19:
    print('Você está na categoria JÚNIOR!')
elif idade <= 25:
    print('Você está na categoria SÊNIOR!')
elif idade > 25:
    print('Você está na categoria MASTER!')

