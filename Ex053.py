print('{:^80}'.format('-------- Selecione uma das opções abaixo --------'))
n1 = float(input('Insira o primeiro numero '))
n2 = float(input('Insira o segundo numero '))
op = 0
while(op != 5):
    op = int(input('''
    [1]somar
    [2]multiplicar
    [3]maior
    [4]novos números
    [5]sair do programa
    '''))
    if(op==1):
        print('A soma vale {}'.format(n1+n2))
    elif(op==2):
        print('A multiplicação vale {}'.format(n1*n2))
    elif(op==3):
        maior = n1
        if(maior < n2):
            maior = n2
        print('O maior é {}'.format(maior))
    elif(op==4):
        n1 = float(input('Insira o primeiro número '))
        n2 = float(input('Insira o segundo número '))
    elif(op==5):
        print('Finalizando...')
    else:
        print('Opção inválida')
print('O programa foi finalizado.')
