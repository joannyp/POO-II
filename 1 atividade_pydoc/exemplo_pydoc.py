'''
    DESCRIPTION

    Essa funcao recebe um numero como parametro e retorna o fatorial desse numero

    Foi utilizado o padrao Sphinx para documentar o codigo

    Author: Joanny Eva
    Email: joannypacheco@hotmail.com
    Date: 24/05/2021
'''

def fatorial(n):
    '''

    :param n: int
        valor do tipo inteiro
    :raise:
        so aceita valores do tipo inteiro

    :return:
        vai retornar o fatorial de n
    '''

    fat = 1
    while n > 1:
        fat *= n
        n -= 1

    return fat

print("O fatorial de {} é {}".format(4, fatorial(4)))