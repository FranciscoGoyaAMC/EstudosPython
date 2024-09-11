user = input('Digite seu usuário: ')
password = input('Digite sua senha: ')
cont = 1

while user != 'user10' and password != 'password1234':
    if cont == 3:
        print('Número máximo de tentativas excedido')
        break

    user = input('Digite seu usuário: ')
    password = input('Digite sua senha: ')
    cont = cont + 1

if user == 'user10' and password == 'password1234':
    print('Login efetuado com sucesso')
