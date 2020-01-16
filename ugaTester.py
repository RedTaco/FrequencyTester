from bs4 import BeautifulSoup
import requests
import csv
import lxml
import pyttsx3

engine = pyttsx3.init()
source = requests.get('https://www.admissions.uga.edu/admissions/transfer/').text


soup = BeautifulSoup(source, 'lxml')
yup: str = ''

exempt =[]
with open('list.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        exempt.append(row)
print(exempt)
for t in soup.find('div', {"class": 'site-content'}).text:
    yup = yup + t

yup = yup.lower()
print(yup)
for x in exempt:
    yup = yup.replace(x[0], ' ')

print(yup)
engine.setProperty('rate', 325)
engine.say(yup)

engine.runAndWait()
