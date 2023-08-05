salario = float(input('Digite o seu salário atual para calcular o aumento: '))
if salario <= 1250:
    sal = salario * 1.15
else:
    sal = salario * 1.10
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario, sal))
