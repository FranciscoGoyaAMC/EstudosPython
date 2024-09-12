"""
Faça um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
"""
def fatorial(n, show=False):
   n
   fat = 1
   while n > 0:
      if show == True:
         if n > 1:
            print(f'{n} x ',end='')
         else:
            print(f'{n} = ', end='')
      fat *= n
      n -= 1
   return fat

