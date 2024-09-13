"""
Reescreva a função leiaInt() que fizemos no exercício 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
"""
def leia_int(txt):
    while True:
        try:
            num = int(input(txt))
        except (ValueError, TypeError):
            print(f'Valor digitado não é um valor válido')
            print(f'Favor digitar um valor válido')
            continue
        else:
            return num   


def leia_float(txt):
    while True:
        try:
            num = float(input(txt))
        except (ValueError, TypeError):
            print(f'Valor digitado não é um valor válido')
            print(f'Favor digitar um valor válido')
            continue
        except KeyboardInterrupt:
            print(f'Programa interrompido')
            return 0
        else:
            return num 


num = leia_int('Digite um número inteiro: ')
print(f'O valor digitado foi {num}')
num2 = leia_float('Digite um valor com ponto flutuante: ')
print(f'O valor digitado foi {num2}')
