l1 = float(input('Insira o primeiro lado do triângulo '))
l2 = float(input('Insira o segundo lado do triângulo '))
l3 = float(input('Insira o terceiro lado do triângulo '))
if l1 == l2 == l3:
    print('O triângulo é equilátero!')
elif l1 == l2 or l1 == l3 or l2 == l3:
    print('O triângulo é isósceles!')
elif l1 != l2 and l2 != l3 and l1 != l3:
    print('O triângulo é escaleno!')