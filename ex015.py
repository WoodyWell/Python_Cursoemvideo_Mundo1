km = float(input('Quantos km foram rodados? '))
dias = float(input('Quantos dias foram alugados? '))
tkm = km * 0.15
tdias = dias * 60
total = tkm + tdias
print('O preço a pagar por ter utilizado o carro por {:.0f} dias e rodado {:.2f} km é: R${:.2f}'.format(dias, km, total))
