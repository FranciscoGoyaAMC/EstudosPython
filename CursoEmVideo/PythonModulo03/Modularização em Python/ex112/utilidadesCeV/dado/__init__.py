"""
Ex112:
Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função input(), mas com uma validação de dados para aceitar apenas valores que seja monetários.
"""
def leia_dinheiro(n):
    valido = False
    while not valido:
        msg = str(input(n)).replace(',','.').strip()
        if msg.isalpha() or msg == '':
            print(f'Erro! "{msg}" não é um valor válido.')
        else:
            valido = True
            return float(msg)

