altura= float(input('Quanto de altura a parede possui?'))
largura= float(input('Quanto de largura a parede possui?'))
area= largura * altura
litros= area/2
print('Sua parede possui uma área de {},portanto, você precisará de {}litros de tinta para pinta-la'.format(area,litros))