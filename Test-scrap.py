from bs4 import BeautifulSoup
import urllib.request
import csv

urlpage = 'https://www.matchendirect.fr/classement-foot/france/classement-ligue-1.html'

page = urllib.request.urlopen(urlpage)

soup = BeautifulSoup(page, 'html.parser')

table = soup.find('table', attrs={'id': 'tableau_classement'})

results = table.find_all('tr')

rows = []
rows.append(['Equipe', 'Pts', 'J', 'G', 'N', 'P', 'BP', 'BC', 'Diff'])

data = []

for result in results:
    data.append(result.find_all('td')) 
    if len(data) == 0:
        continue

#for dt in data:
    #for equipe in dt:
       #print(equipe.getText())

def dataToJson(data):
    for classement in data:
        for equipe_info in classement:
            if(int(equipe_info.getText())){
                #to continue
            }

#pts = data[1].getText()
#j = data[2].getText()
#g = data[3].getText()
#n = data[4].getText()
#p = data[5].getText()
#bp = data[6].getText()
#bc = data[7].getText()
#diff = data[8].getText()

#print(equipe)