import random
print("Sou seu computador...")
numero = random.randint(0,10)
print("Pensei em um número entre 0 e 10... você consegue adivinha-lo?")
r = ''.strip()
palpite = 0
while(r != "ganhou" ):
    jogador = int(input('Faça sua jogada!'))
    palpite += 1
    if( jogador < numero):
        print('Um pouco mais... você quase acertou!')
    elif(jogador > numero):
        print('Um pouco menos... você quase acertou!')
    elif(jogador == numero):
        print('Você acertou!')
        r = "ganhou"
print('Você acertou com {} palpites!'.format(palpite))

