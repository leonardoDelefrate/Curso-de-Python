print('-------------------')
print('LISTAGEM DE PREÇOS')
print('-------------------')
tabela = ('Lápis',1.75,
          'Borracha',2.00,
          'Caderno',15.9,
          'Estojo',25.00,
          'Transferidor',4.20,
          'Compasso',9.99,
          'Mochila',120.32,
          'Canetas',22.30,
          'Livro',34.90)
for item in range(0,len(tabela)):
    if item % 2 == 0:
        print(f'{tabela[item]:.<30}', end='')
    else:
        print(f'{tabela[item]:>5}')