import urllib.request
try:
    site = urllib.request.urlopen('https://www.youtube.com')
except:
    print('\033[31mO site não está acessível no momento\033[m')
else:
    print('\033[32mO site está acessível no momento\033[m')

