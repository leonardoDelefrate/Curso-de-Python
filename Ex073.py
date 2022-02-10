lista = []
for c in range(0,5):
    lista.append(int(input('Digite um valor')))
    if(c == 0):
        maior = lista[0]
        menor = lista [0]
    elif(c > 0):
        if(maior < lista[c]):
            maior = lista[c]
        if(menor > lista[c]):
            menor = lista[c]
print(f'''O maior valor da lista é {maior} e está na posição{}
       e o menor valor é {menor} e está na posição {}''')