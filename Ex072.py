palavras = ('APRENDER','PROGRAMAR','LINGUAGEM',
            'PYTHON','CURSO','GRATIS',
            'ESTUDAR','PRATICAR','TRABALHAR',
            'MERCADO','PROGRAMADOR','FUTURO')

for p in palavras:
    print(f'\nNa palavra {p} temos ', end='')
    for count in p:
        if( count in 'AEIOU' ):
            print(count,end='')