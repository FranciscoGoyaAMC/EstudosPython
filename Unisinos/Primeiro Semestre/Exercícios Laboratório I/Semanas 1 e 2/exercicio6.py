from time import sleep

a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))
d = int(input('Digite o quarto número: '))
e = int(input('Digite o quinto número: '))
area_triangulo = (b * c) / 2
perimetro_retangulo = a + b + c + d
area_circulo = float(3.14 * e**2)

print('Calculando...')
sleep(2)

print(f'Considerando o segundo número como a base de um triângulo, e o terceiro número como sua altura. A área deste triângulo seria: {area_triangulo}')
print(f'Considerando que os quatro primeiros números inseridos formam as arestas de um retângulo. O seu perímertro seria: {perimetro_retangulo}')
print(f'Considerando que o quinto número digito seja o raio de um círculo. A sua área seria: {area_circulo}')
