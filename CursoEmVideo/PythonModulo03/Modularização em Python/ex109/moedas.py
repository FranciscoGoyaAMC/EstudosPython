"""
Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
"""
"""
Calcula juros, dobro e metade de valor selecionado
Aumentar: aumenta x% do valor solicitado, por padrão valor é 1 a taxa é 10%
Diminuir: diminui x% do valor solicitado, por padrão valor é 1 a taxa é 10%
Dobro: dobra o valor solicitado, por padrão valor é 1
Metade: divide o valor solicitado, por padrão valor é 1
Moeda: Converte o valor solicitado para um padrão de escrita monetário, por padrão o valor é 1 e a cifra é o real (R$)
"""
def aumentar(val=1,tax=10,cifr=False):
    """
    Aumentar: aumenta x% do valor solicitado, por padrão valor é 1 a taxa é 10%
    Parâmetro val: valor base que será incrementado, por padrão é 1
    Parâmetro taxa: quantos por cento será incrementado, por padrão é 10
    Parâmetro cifr: indica se quer que o valor seja formatado para um padrão monetário, por padrão é False
    Juro: calculo da % que será incrementado ao valor
    Retorno: valor com a taxa incrementada
    """
    juro = val * (tax/100)
    val += juro
    return val if not cifr else moeda(val)


def diminuir(val=1,tax=10,cifr=False):
    """
    Aumentar: aumenta x% do valor solicitado, por padrão valor é 1 a taxa é 10%
    Parâmetro val: valor base que será decrementado, por padrão é 1
    Parâmetro taxa: quantos por cento será decrementado, por padrão é 10
    Parâmetro cifr: indica se quer que o valor seja formatado para um padrão monetário, por padrão é False
    Juro: calculo da % que será decrementado do valor
    Retorno: valor com a taxa decrementada
    """
    juro = val * (tax/100)
    val -= juro
    return val if not cifr else moeda(val)


def dobro(val=1,cifr=False):
    """
    Dobro: Dobra o valor solicitado por parâmetro, por padrão o valor é 1
    Parâmetro val: valor que será dobrado, por padrão é 1
    Parâmetro cifr: indica se quer que o valor seja formatado para um padrão monetário, por padrão é False
    """
    val *= 2
    return val if not cifr else moeda(val)


def metade(val=1,cifr=False):
    """
    Metade: Divide o valor socilitado por parâmetro, por padrão o valor é 1
    Parâmetro val: valor que será dividido, por padrão é 1
    Parâmetro cifr: indica se quer que o valor seja formatado para um padrão monetário, por padrão é False
    """
    val /= 2
    return val if not cifr else moeda(val)


def moeda(val=1,cifra='R$'):
    """
    Moeda: Converte o valor solicitado para um padrão de escrita monetário, por padrão o valor é 1 e a cifra é o real (R$)
    Parâmetro val: valor que será escrito por padrão monetário
    Parâmetro cifra: a cifra da moeda
    """
    return f'{cifra}{val:.2f}'.replace('.',',')

