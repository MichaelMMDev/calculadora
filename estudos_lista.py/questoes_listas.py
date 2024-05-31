usuarios=['Michael', 'Augusto', 'Jakissum', 'Adrieli', 'Rosa Thaís']
senhas=[1234, 5432, 3697, 121418, 63673]

user1=input('OLá usuário, digite seu nome de usuário, DEFINIDO ANTERIORMENTE! : ')

senh1=(input('OLá usuário, digite sua senha, DEFINIDA ANTERIORMENTE! : '))


if user1 in usuarios and senh1 in senhas:
    print('Estamos feliz em lhe receber. Continue navegando! :) ')

else:
    print('Tente novamente, usuário ou senha estão incorretos')