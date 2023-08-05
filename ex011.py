altura = int(input('Qual a altura da parede? '))
largura = int(input('Qual a largura da parede? '))
area = altura * largura
print('Considerando a altura e a largura informada, temos o valor de {} metros quadrados.'.format(area))
print('Uma vez que cada litro de tinta é capaz de pintar 2 metros quadrados, você precisará de {} litros de tinta para completar a pintura.'.format(area / 2))
