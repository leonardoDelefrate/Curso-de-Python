times = ('Corinthians','Plameiras','Santos','Gremio','Cruzeiro','Flamengo','Vasco','Chapecoense',
         'Atlético','Botafogo','Atlético-PR','Bahia','São Paulo',
         'Fluminense','Sport Recife','EC Vitoria','Curitiba','Avaí','Ponte Preta','Atlético-GO')
print('-'*30)
print(f'Os 5 primeiros colocados foram:{times[0:5]}')
print('-'*30)
print(f'Os últimos 4 colocados foram:{times[-4:]}')
print('-'*30)
print(f'Times em ordem alfabética:{sorted(times)}')
print('-'*30)
print(f'Chapecoense está na {times.index("Chapecoense")+1} posição!')
print('-'*30)