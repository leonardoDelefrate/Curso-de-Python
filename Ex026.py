vel = float(input('Digite quantos km/h está o seu veículo '))
multa = (vel - 80) * 7
if vel > 80:
    print('Você foi multado. A velocidade máxima permitida é de 80km/h. valor da multa é: {} R$'.format( multa ))
else:
    print(' Você está na velocidade permitida, dirija com segurança e tenha um bom dia!')
