acertou = False

for i in range(0,6):
    senha = input('Defina sua senha: ')
    if(senha.isdigit() and len(senha) >= 5 and len(senha) <= 10):
        print('Senha cadastrada com sucesso!')
        acertou = True
        break
    else:
        print('Senha inválida.')
if(not(acertou)):
    print('Quantidade de tentativas excedida!')
