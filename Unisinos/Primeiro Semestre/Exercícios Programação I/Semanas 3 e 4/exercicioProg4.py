def grauFinal(grauA,grauB):
    if (grauA + grauB) / 2 >= 6.99:
        print('Parabéns, você passou')
    else:
        print('Você precisa fazer o Grau C')

grauA = float(input('Digite sua nota do Grau A: '))
grauB = float(input('Digite sua nota do Grau B: '))

if grauA < 0 or grauB < 0:
    print('Erro!')
else:
    grauFinal(grauA,grauB)
