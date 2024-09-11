from time import sleep

nome = input('Digite seu nome: ').strip().upper()
pratica_grauA = float(input('Digite sua nota da Atividade Prática do Grau A: '))
teorica_grauA = float(input('Digite sua nota da Atividade Teórica do Grau A: '))
prova_lab_grauB = float(input('Digite sua nota da Prova em Laboratório do Grau B: '))
teste_teorico_grauB = float(input('Digite sua nota do Teste Teórico do Grau B: '))
trabalho_extra_grauB = float(input('Digite sua nota do Trabalho Extraclasse do Grau B: '))

print('Calculando notas...')
sleep(2)

total_grauA = (pratica_grauA * 0.45) + (teorica_grauA * 0.55)
total_grauB = (prova_lab_grauB * 0.6) + (teste_teorico_grauB * 0.2) + (trabalho_extra_grauB * 0.2)
total_disciplina = (total_grauA * 0.33) + (total_grauB * 0.67)

print(f'{nome} sua nota no Grau A é: {total_grauA:.2f}', end=',')
print(f' sua nota no Grau B é: {total_grauB:.2f}', end='')
print(f' e sua nota final na disciplina é: {total_disciplina:.2f}')
