mediaidade = 0
somaidade = 0
mv = 0   # maioridade homem #
nv = ''  # nome mais velho #
totmulher20 = 0
for c in range(1,6):
    print("----- {}° pessoa -----".format(c))
    n = str(input("Nome: ".format(c)))
    i = int(input("Idade: ".format(c)))
    s = str(input("Sexo[M/F]: ".format(c)))

    somaidade += i

    if(c == 1 and (s == "m" or s == "M")):
        mv = i
        nv = n
    if(s in 'Mm' and i > mv):
        mv = i
        nv = n
    if(s in 'Ff' and i < 20):
        totmulher20 += 1

mediaidade = somaidade/4
print("A média das idades é de {}".format(mediaidade))
print("O homem mais velho tem {} anos e se chama {} .".format(mv,nv))
print("Ao todo são {} mulheres com menos de 20 anos".format(totmulher20))