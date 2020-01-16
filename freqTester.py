from bs4 import BeautifulSoup
import requests
import csv
import lxml
import pyttsx3

engine = pyttsx3.init()
source = requests.get('https://www.space.com/16105-asteroid-belt.html').text


soup = BeautifulSoup(source, 'lxml')
yup: str = ''

exempt =[]

with open('list.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        exempt.append(row)

for t in soup.find('div', {"id": 'article-body'}).text:
    yup = yup + t

print(yup)
yup = yup.lower()
for x in exempt:
    yup = yup.replace(x[0], ' ')
print(yup)
def freq(str):
    str = str.split()
    str2 = []
    total = 0
    for i in str:

        if i not in str2:
            str2.append(i)

    for i in range(0, len(str2)):

        #print('Freq of ', str2[i], 'is :', str.count(str2[i]))
        total = total + str.count(str2[i])

    avg = total / len(str2)
    print(avg)
    for i in range(0,len(str2)):
        if str.count(str2[i]) > avg * 2:
            print (str2[i], ' : ', str.count(str2[i]))

freq(yup)