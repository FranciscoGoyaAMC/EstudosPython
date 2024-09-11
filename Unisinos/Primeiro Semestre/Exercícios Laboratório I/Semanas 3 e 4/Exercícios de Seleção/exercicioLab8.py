from time import sleep

while True:
    print('Digite 1 para somar dois valores')
    print('Digite 2 para subtrair dois valores')
    print('Digite 3 para multiplicar dois valores')
    print('Digite 4 para dividir dois valores')
    print('Digite 5 para realizar uma potência entre dois valores')
    print('Digite 6 para realizar uma radiciação entre dois valores')
    print('Digite qualquer outro número para sair')
    sleep(0.5)
    acao = int(input('Digite sua opção: '))
    if acao == 1:
        valor1 = int(input('Digite seu primeiro número: '))
        valor2 = int(input('Digite seu segundo número: '))
        valor_total = valor1 + valor2
        print('Calculando...')
        sleep(2)
        print(f'A soma dos valores é: {valor_total}')
    elif acao == 2:
        valor1 = int(input('Digite seu primeiro número: '))
        valor2 = int(input('Digite seu segundo número: '))
        valor_total = valor1 - valor2
        print('Calculando...')
        sleep(2)
        print(f'A subtração dos valores é: {valor_total}')
    elif acao == 3:
        valor1 = int(input('Digite seu primeiro número: '))
        valor2 = int(input('Digite seu segundo número: '))
        valor_total = valor1 * valor2
        print('Calculando...')
        sleep(2)
        print(f'A multiplicação dos valores é: {valor_total}')
    elif acao == 4:
        valor1 = int(input('Digite seu primeiro número: '))
        valor2 = int(input('Digite seu segundo número: '))
        if valor2 != 0:
            valor_total = valor1 / valor2
            print('Calculando...')
            sleep(2)
            print(f'A divisão dos valores é: {valor_total}')
        else:
            print('Erro! Impossível dividir por zero')
    elif acao == 5:
        valor1 = int(input('Digite seu primeiro número: '))
        valor2 = int(input('Digite seu segundo número: '))
        valor_total = valor1 ** valor2
        print('Calculando...')
        sleep(2)
        print(f'A potência dos valores é: {valor_total}')
    elif acao == 6:
        valor1 = int(input('Digite seu primeiro número: '))
        valor2 = int(input('Digite seu segundo número: '))
        valor_total = (valor1**(1/valor2))
        print('Calculando...')
        sleep(2)
        print(f'A radiciação dos valores é: {valor_total}')
    else:
        print('Você saiu do programa')
        break
