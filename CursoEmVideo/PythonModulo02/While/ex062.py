"""
 Melhore o exercício 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos. 
"""
n = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
c = 10

while c != 0:
    for i in range(1, c + 1):
        print(n)
        n = n + r
    c = int(input('Deseja saber mais valores da razão? Caso queira digite quantos, se não digite 0 para parar: '))
print('Fim')
