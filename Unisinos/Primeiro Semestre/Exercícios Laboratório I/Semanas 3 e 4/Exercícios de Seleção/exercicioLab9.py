grauA = float(input('Digite sua nota do Grau A: '))
grauB = float(input('Digite sua nota do Grau B: '))
if grauA < 0 or grauB < 0:
    print('Erro! Grau digitado com valor negativo')
else:
    grau_final = (grauA * 0.3) + (grauB * 0.7)
    if grau_final >= 6:
        print(f'Você tirou: {grau_final:.2f}. Parabéns! Está aprovado!')
    else:
        print(f'Você tirou:{grau_final:.2f}. Você precisa fazer a prova de Grau C')
