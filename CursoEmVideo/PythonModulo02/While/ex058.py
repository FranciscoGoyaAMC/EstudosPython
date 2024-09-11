"""
Melhore o jogo do exercício 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
"""
from random import randint

sorteado = randint(0,10)
usuario = int(input('Eu pensei em um número de 0 a 10. Tente adivinhar qual: '))
tentativas = 1

while usuario != sorteado:
    usuario = int(input('Não acertou. Tente outro número: '))
    tentativas += 1
print(f'Você acertou, o número era {sorteado}! Só precisou de {tentativas} tentativa(s)')
