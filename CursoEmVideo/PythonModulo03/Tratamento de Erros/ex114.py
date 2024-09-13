"""
Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
"""
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('Não foi possível acessar o site')
else:
    print('Foi possível acessar o site')
    