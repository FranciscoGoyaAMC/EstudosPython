"""
 Adapte o código do exercício #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado
"""
"""
Calcula juros, dobro e metade de valor selecionado
Aumentar: aumenta x% do valor solicitado, por padrão valor é 1 a taxa é 10%
Diminuir: diminui x% do valor solicitado, por padrão valor é 1 a taxa é 10%
Dobro: dobra o valor solicitado, por padrão valor é 1
Metade: divide o valor solicitado, por padrão valor é 1
Moeda: Converte o valor solicitado para um padrão de escrita monetário, por padrão o valor é 1 e a cifra é o real (R$)
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


def moeda(val=1,cifra='R$'):
    """
    Moeda: Converte o valor solicitado para um padrão de escrita monetário, por padrão o valor é 1 e a cifra é o real (R$)
    Parâmetro val: valor que será escrito por padrão monetário
    Parâmetro cifra: a cifra da moeda
    """
    return f'{cifra}{val:.2f}'.replace('.',',')

