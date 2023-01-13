import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('O site não está acessível no momento')
else:
    print('O site está acessível. Tudo ok')