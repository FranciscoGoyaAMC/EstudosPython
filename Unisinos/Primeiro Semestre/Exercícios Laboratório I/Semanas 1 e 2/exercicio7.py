from time import sleep

nota1 = float(input('Digite sua nota do trabalho: '))
nota2 = float(input('Digite sua nota da prova: '))
nota3 = float(input('Digite sua nota do teste: '))
nota_final = (nota1 * 0.1) + (nota2 * 0.7) + (nota3 * 0.3)

print('Calculando...')
sleep(2)

print(f'{nota_final:.2f} é a sua nota final no semestre')
