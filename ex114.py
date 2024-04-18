import urllib.request
import urllib

try:
    site = urllib.request.urlopen("https://www.google.com.br/")
except:
    print("\033[31mO GOOGLE NÃO ESTÁ ACESSÍVEL :(\033[m")
else:
    print("\033[32mO GOOGLE ESTÁ ACESSÍVEL! :D\033[m")    
