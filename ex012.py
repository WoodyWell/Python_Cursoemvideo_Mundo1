p = float(input('Qual o valor do produto? '))
novo = p - (p * 5 / 100)
print('Aplicando o desconto de 5%, o valor final do produto fica por: R${:.2f}'.format(novo))
