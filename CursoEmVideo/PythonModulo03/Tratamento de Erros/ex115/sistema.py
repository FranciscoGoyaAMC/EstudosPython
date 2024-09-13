"""
Faça um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.
"""
import sys
sys.path.append(r'C:\Users\franc\Desktop\Programação\Python\Exercícios_Guanabara\PythonModulo03\Tratamento de Erros')
from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'
if arquivo_existe(arq):
    print('Arquivo encontrado com sucesso')
else:
    print('Falha ao encontrar o arquivo')
    criar_arquivo(arq)

while True:
    opc = menu(['Cadastrar Nova Pessoa','Ver Pessoas Cadastradas','Sair do Sistema'])
    if opc == 1:
        sleep(1)
        cabecalho('CADASTRO DE NOVA PESSOA')
        nome = str(input('Digite o nome: ')).strip().capitalize()
        idade = leia_int('Digite a idade: ')
        cadastrar(arq,nome,idade)
    elif opc == 2:
        sleep(1)
        cabecalho('PESSOAS CADASTRADAS')
        ler_arquivo(arq)
    elif opc == 3:
        sleep(1)
        cabecalho('Sistema finalizado')
        break
    else:
        sleep(1)
        print('\033[31mErro! Opção Inválida\033[m')
    sleep(2)
