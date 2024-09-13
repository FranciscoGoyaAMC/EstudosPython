def linha(msg=42):
    return '-' * msg


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def leia_int(txt):
    from time import sleep
    while True:
        try:
            num = int(input(txt))
        except (ValueError, TypeError):
            sleep(1)
            print(f'\033[31mErro')
            print(f'Valor digitado não é um valor válido')
            print(f'Favor digitar um valor válido\033[m')
            print(linha())
            continue
        else:
            return num


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for i in lista:
        print(f'\033[33m[{c}]\033[m \033[34m{i}\033[m')
        c += 1
    print(linha())
    resp = leia_int('Digite a opção desejada: ')
    print(linha())
    return resp

