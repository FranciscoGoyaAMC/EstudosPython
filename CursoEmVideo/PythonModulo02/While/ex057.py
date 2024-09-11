"""
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores M ou F. Caso esteja errado, peça a digitação novamente até ter um valor correto.
"""
sexo = str(input('Digite [M] para masculino ou [F] para feminino: ')).strip().upper()[0]

while (sexo != "M") and (sexo != "F"):
    print('Opção inválida')
    sexo = str(input('Digite [M] para masculino ou [F] para feminino: ')).strip().upper()[0]
print('Cadastro feito com sucesso')
