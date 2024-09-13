def arquivo_existe(txt):
    try:
        a = open(txt, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo(txt):
    try:
        a = open(txt, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo')
    else:
        print(f'Arquivo {txt} criado com sucesso')


def ler_arquivo(txt):
    try:
        a = open(txt, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        for i in a:
            dado = i.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<20}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq,txt='Desconhecido',int=0):
    try:
        a= open(arq, 'at')
    except:
        print('Erro ao abrir o arquivo')
    else:
        try:
            a.write(f'{txt};{int}\n')
        except:
            print('Erro ao cadastrar')
        else:
            print('Cadastro realizado com sucesso')
