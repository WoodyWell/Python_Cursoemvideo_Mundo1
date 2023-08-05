d = float(input('Qual a distância da viagem? '))
print('Você está prestes a começar uma viagem de {:.2f}km.'.format(d))
if d <= 200:
    preço = d * 0.50
else:
    preço = d * 0.45
print('O preço da passagem será: R${}'.format(preço))
