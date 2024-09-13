"""
Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.
"""
"""
Calcula juros, dobro e metade de valor selecionado
Aumentar: aumenta x% do valor solicitado, por padrão valor é 1 a taxa é 10%
Diminuir: diminui x% do valor solicitado, por padrão valor é 1 a taxa é 10%
Dobro: dobra o valor solicitado, por padrão valor é 1
Metade: divide o valor solicitado, por padrão valor é 1
"""
def aumentar(val=1,tax=10):
    """
    Aumentar: aumenta x% do valor solicitado, por padrão valor é 1 a taxa é 10%
    Parâmetro val: valor base que será incrementado, por padrão é 1
    Parâmetro taxa: quantos por cento será incrementado, por padrão é 10
    Juro: calculo da % que será incrementado ao valor
    Retorno: valor com a taxa incrementada
    """
    juro = val * (tax/100)
    val += juro
    return val


def diminuir(val=1,tax=10):
    """
    Aumentar: aumenta x% do valor solicitado, por padrão valor é 1 a taxa é 10%
    Parâmetro val: valor base que será decrementado, por padrão é 1
    Parâmetro taxa: quantos por cento será decrementado, por padrão é 10
    Juro: calculo da % que será decrementado do valor
    Retorno: valor com a taxa decrementada
    """
    juro = val * (tax/100)
    val -= juro
    return val


def dobro(val=1):
    """
    Dobro: Dobra o valor solicitado por parâmetro, por padrão o valor é 1
    Parâmetro val: valor que será dobrado, por padrão é 1
    """
    val *= 2
    return val


def metade(val=1):
    """
    Metade: Divide o valor socilitado por parâmetro, por padrão o valor é 1
    Parâmetro val: valor que será dividido, por padrão é 1
    """
    val /= 2
    return val

