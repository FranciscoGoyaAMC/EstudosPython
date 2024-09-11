"""
Faça um programa que leia uma frase qualquer e diga se ela é um palíndromo
"""
frase = str(input('Digite uma frase: ')).strip().upper().strip("!").strip(".").strip(",").strip(";").strip(":").strip("^").strip("~").strip("´").strip("`")
palavras_frase = frase.split()
frase_junto = "".join(palavras_frase)
reverso = frase[::-1]
palavras_reverso = reverso.split()
reverso_junto = "".join(palavras_reverso)

if frase_junto == reverso_junto:
    print(f'A frase {frase} de trás pra frente fica {reverso}, logo ela é um palíndromo.')
else:
    print(f'A frase {frase} de trás pra frente fica {reverso}, logo ela não é um palídromo.')
