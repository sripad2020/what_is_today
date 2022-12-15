from bs4 import BeautifulSoup
import requests
url='https://nationaltoday.com/what-is-today/'
text=requests.get(url).text
output=[]
names=[]
soap=BeautifulSoup(text,'html.parser')
for link in soap.find_all('h3'):
    text=link.get_text()
    names.append(text)
for link in soap.find_all('p'):
    tet=link.get_text()
    output.append(tet)
for i in range(39):
    print('\n')
    print(names[i])
    print(output[i+1])
    print('\n')