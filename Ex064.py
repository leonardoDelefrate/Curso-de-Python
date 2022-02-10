total = menor_preço = cont = 0
cont_preço1000 = 0
prod_barato = ' '
while True:
    nome = ' '
    nome = str(input('Nome do produto:')).upper().strip()
    preço = float(input('Preço do produto: R$ '))
    total = total + preço
    if(preço > 1000):
        cont_preço1000 = cont_preço1000 + 1
    cont = cont + 1
    if(cont == 1):
        menor_preço = preço
        prod_barato = nome
    elif(preço < menor_preço):
        menor_preço = preço
        prod_barato = nome
    resposta = ' '
    while(resposta not in 'SN'):
        resposta = str(input('Deseja continuar[S/N]? ')).upper().strip()[0]
    if(resposta == 'N'):
        break
print(f'O total da compra foi de {total:.2f}')
if(cont_preço1000 == 1):
    print(f'{cont_preço1000} produto custou mais do que R$ 1000 reais')
elif(cont_preço1000 > 1):
    print(f'{cont_preço1000} produtos custaram mais do que R$ 1000 reais')
print(f'O produto mais barato foi {prod_barato} e custou {menor_preço}')
print('{:-^40}'.format('FIM DO PROGRAMA'))