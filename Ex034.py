num1 = float(input('Digite um número qualquer '))
num2 = float(input('Digite outro número qualquer '))
if num1>num2:
    print('O número {} é maior que o número {} .'.format(num1,num2))
elif num2>num1:
    print('O número {} é maior que o número {} .'.format(num2,num1))
elif num1==num2:
    print('O número {} é igual ao número {} .'.format(num1,num2))

