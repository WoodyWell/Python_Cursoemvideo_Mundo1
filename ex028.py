from random import randint
from time import sleep
print('--==--'*12)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('--==--'*12)
n = randint(0,5)
num = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if n == num:
    print('Parabéns! Você conseguiu me vencer!')
else:
    print('Ganhei! Eu pensei no número {}, não no {}.'.format(n, num))
