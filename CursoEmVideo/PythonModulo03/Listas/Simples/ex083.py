"""
Faça um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
"""
expressao = str(input('Digite uma expressão matemática: '))
abrem = []
fecham = []
for simbolo in expressao:
    if simbolo == "(":
        abrem.append("(")
    elif simbolo == ")":
        fecham.append(")")
if len(abrem) == len(fecham):
    print('Sua expressão é válida')
else:
    print('Sua expressão não é válida')
