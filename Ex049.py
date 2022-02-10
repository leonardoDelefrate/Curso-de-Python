import datetime
h = datetime.date.today().year
tma = 0
tme = 0
for p in range(1,8):
    ano = int(input('Em que ano a {}° pessoa nasceu? '.format(p)))
    idade = h - ano
    if idade >= 18:
        tma += 1
    else:
        tme += 1
print('{} pessoas atingiram a maioridade.'.format(tma))
print('{} pessoas ainda não atingiram a maioridade.'.format(tme))


