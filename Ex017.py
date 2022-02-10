import math
an = float(input("Digite um ângulo qualquer"))
rad = (an * 6.28) /360
print('O seno do ângulo {} vale {}'.format(an,math.sin(rad)))
print('O cosseno do ângulo {} vale {}'.format(an,math.cos(rad)))
print('A tangente do ângulo {} vale {}'.format(an,math.tan(rad)))

