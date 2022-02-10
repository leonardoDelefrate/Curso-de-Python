print('=' * 5,'CALCULADORA DE COMPRAS','='*5)
p = float(input('Digite o valor total da compra: '))
op = int(input('''Escolha qual a forma de pagamento deseja utilizar:
[1] à vista dinheiro/cheque
[2] à vista no cartão
[3] em até 2x no cartão
[4] 3x ou mais no cartão
 '''))
if op == 1:
    total = p - (p * 0.1)
elif op == 2:
    total = p - (p * 0.05)
elif op == 3:
    total = p
    parcela = p/2
    print('Sua compra será parcelada em 2x sem juros, cujo valor das parcelas serão de R${} reais'.format(parcela))
elif op == 4:
    total = (p * 1.2)
print('O valor total da compra é de R${} reais ! '.format(total))