from time import sleep
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))
print('VERIFICANDO...')
sleep(2)
print('O maior número digitado é: {}'.format(max(n1, n2, n3)))
print('O menor número digitado é: {}'.format(min(n1, n2, n3)))
