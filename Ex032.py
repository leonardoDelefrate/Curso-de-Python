casa = float(input('insira o valor da casa '))
sal = float(input('Insira o seu salário '))
anos = int(input('Em quantos anos deseja pagar o imóvel? '))
prestação = casa/(anos * 12)
if prestação > 0.30 * sal:
    print('Não é possível realizar o empréstimo. ')
else:
    print('Para pagar uma casa de {} em {} anos precisa-se de {} R$'.format(casa,sal,prestação))