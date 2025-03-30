# Create a Python script that tests whether the Pudim website is accessible from the computer being used.
import urllib.request

try:
    site = urllib.request.urlopen('https://www.pudim.com.br')

except urllib.error.URLError:
    print('\033[1;31mThis website is not working !\033[0m')

else:
    print('\033[1;32mThis web site is working !\033[0m')