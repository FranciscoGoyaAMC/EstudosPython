nome = input('Digite seu nome: ')
print(f'Olá {nome} seja bem vindo(a)!')
valor1 = float(input('Digite o primeiro valor: '))
valor2 = float(input('Digite o segundo valor: '))
resultado = valor1/valor2
resultadoFormatado1 = float("%.2f" % resultado)
resultadoFormatado2 = float("%.3f" % resultado)
resultadoFormatado3 = float("%.4f" % resultado)
print(f'{nome} seu valor com 2 casas decimais é: {resultado:.2f}; com 3 casas decimais é: {resultado:.3f}; com 4 casas decimais é: {resultado:.4f}')
