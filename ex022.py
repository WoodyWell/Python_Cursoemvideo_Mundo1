nome = str(input('Digite o seu nome completo: ')).strip()
print('Analisando o seu nome...')
print('O seu nome com todas as letras maiúsculas: {}'.format(nome.upper()))
print('O seu nome com todas as letras minúsculas: {}'.format(nome.lower()))
print('Quantidade de letras no seu nome completo: {}'.format(len(nome) - nome.count(' ')))
#print('O seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
