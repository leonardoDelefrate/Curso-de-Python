cont = 0
cont_m = 0
cont_f20 = 0
cont_maioridade = 0
while True:
    sexo = ' '
    while(sexo not in 'MF'):
        sexo = str(input('Masculino ou Feminino[M/F]? ')).upper().strip()
    idade = int(input(f'Qual a idade da {cont + 1}° pessoa: '))
    if(sexo == 'M'):
        cont_m = cont_m + 1
    elif(sexo == 'F' and idade < 20):
        cont_f20 = cont_f20 + 1
    if(idade >= 18):
        cont_maioridade = cont_maioridade + 1
    resposta = ' '
    while(resposta not in 'SN'):
        resposta = str(input('Deseja continuar o cadastro[S/N]? ')).upper().strip()
    if(resposta == 'N'):
        break
print(f'O total de pessoas com mais de 18 anos foram de {cont_maioridade}')
print(f'O total de homens cadastrados é de {cont_m}')
print(f'O total de mulheres com menos de 20 anos é de {cont_f20}')
print('----------------')
print('FIM DO PROGRAMA')
print('----------------')