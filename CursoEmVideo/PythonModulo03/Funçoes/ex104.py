"""
Faça um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico
"""
def leia_int(txt):
    num = str(input(txt))
    if num.isnumeric():
        num = int(num)
        return num
    else:
        return 'Erro! Número inválido'      
    

num = leia_int('Digite um número: ')
print(num)
