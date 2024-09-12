"""
Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
– Quantidade de notas
– A maior nota
– A menor nota
– A média da turma
– A situação (opcional)
- Adicione também a docstring
"""
def notas(*num,sit=False):
    """
    Função para analisar notas de diversos alunos calculando sua média e, se solicitado, dar a situação geral das notas, colocando tudo em um dicionário
    Parâmetro num: uma ou mais notas dos alunos
    Parâmetro sit: opcional para mostrar a situação geral das notas
    Return: dicionário com as especificações de maior e menor nota, calcula da média das notas e, se solicitado pelo sit, situação geral das notas
    """
    boletim = dict()
    if len(num) == 0:
        return 'Não foi passada nenhuma nota'
    else:
        boletim['Total de Notas'] = len(num)
        boletim['Maior nota'] = max(num)
        boletim['Menor nota'] = min(num)
        boletim['Media'] = sum(num)/len(num)
    if sit:
        if boletim['Media'] < 5:
            boletim['Situação'] = 'RUIM'
        if boletim['Media'] < 8:
            boletim['Situação'] = 'BOA'
        if boletim['Media'] > 8:
            boletim['Media'] = 'ÓTIMA'
        return boletim
    else:
        return boletim
