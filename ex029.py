veloc = float(input('Qual a velocidade atual do carro? '))
if veloc >= 80:
    print('Você foi MULTADO por exceder o limite permitido de 80km/h.\n'
          'Você deverá pagar uma multa no valor de R$ {:.2f}.'.format((veloc - 80)*7))

else:
    print('Tenha um bom dia! Dirija com segurança.')
