from time import sleep

def escreva(txt):
    print('-'*len(txt))
    print(txt)
    print('-'*len(txt))

def contador(inicio, fim, passo):
    escreva(f'Contando de {inicio} até {fim} andando de {abs(passo)} em {abs(passo)}')
    if inicio < fim:
        for i in range(inicio, fim+1, passo):
            print(f'{i}', end=' ')
    else:
        if passo < 0:
            for i in range(inicio, fim, passo):
                print(f'{i}', end=' ')
        for i in range(inicio, fim, - passo):
            print(f'{i}', end=' ')
    print('Fim')

contador(1,10,1)
contador(20,0,8)

inicio = int(input('A partir de que número devo iniciar a contagem? '))
fim = int(input('Até que número devo contar? '))
passo = int(input('De quantos em quantos números devo contar? '))

contador(inicio, fim, passo)
