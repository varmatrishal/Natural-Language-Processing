"""
Name:           Trishal Varma & Angelina Boudro

Human Language Technologies
Objective:      Web Crawling and collecting related websites
"""
import sys
import urllib
from urllib import request
from bs4 import BeautifulSoup
import requests
import re
from nltk.tokenize import sent_tokenize



first_url = 'https://www.fcbarcelona.com/en/'
r = requests.get(first_url)
data = r.text
soup = BeautifulSoup(data, "html.parser")

# write URL to urls.txt
with open('urls.txt', 'w') as f:
    for link in soup.find_all('a'):
        print(link.get('href'))
        f.write(str(link.get('href')) + '\n\n')
        link_str = str(link.get('href'))
        print(link_str)
        if 'Barcelona' in link_str or 'barcelona' in link_str:
            if link_str.startswith('/url?q='):
                link_str = link_str[7:]
                print('MOD:', link_str)
            if '&' in link_str:
                i = link_str.find('&')
                link_str = link_str[:i]
            if link_str.startswith('http') and 'google' not in link_str:
                f.write(link_str + '\n')

with open('urls.txt', 'r') as f:
    urls = f.read().splitlines()
for u in urls:
    print(u)

my_url = 'https://www.fcbarcelona.com/en/'
#Building a Knowledge Base
text = "FC Barcelona is one of the best clubs in the world. Barcelona was founded in 1899, November 8th. Barcelona currently has the best football player in the world \n\n"
text1 = "Messi has scored over 800 goals in his Career, with 700+ for Barcelona" "At Just the age of 33, he is considered a club legend \n\n"
text2 = "Barcelona is managed by Ronald Koeman, a legendary player who played for Barcelona as well, and now is the coach \n\n"
text3 = "If you ever come to the city of Barcelona, you have to visit the Camp Nou stadium, it is the largest stadium in Europe \n\n"

sent = sent_tokenize(text)
sent1 = sent_tokenize(text1)
sent2 = sent_tokenize(text2)
sent3 = sent_tokenize(text3)

f = open("knowl.txt", "w")
for i in range(10):
    f.write(text)
    f.write(text2)
    f.write(text1)
    f.write(text3)
f.close()
# visibility
def visible(element):
    if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
        return False
    elif re.match('<!--.*-->', str(element.encode('utf-8'))):
        return False
    return True

html = urllib.request.urlopen(my_url)
soup = BeautifulSoup(html, "html.parser")
data = soup.findAll(text=True)
result = filter(visible, data)
temp_list = list(result)
temp_str = ' '.join(temp_list)
temp_str


req = urllib.request.Request(my_url, headers={'User-Agent': 'Mozilla/5.0'})
with open('urls.txt', 'r') as input:
    for (counter, line) in enumerate(input):
        with open('filename{0}.txt'.format(counter), 'w', encoding='utf-8') as output:
            html = urllib.request.urlopen(my_url)
            soup = BeautifulSoup(html, "html.parser")
            data = soup.findAll(text=True)
            result = filter(visible, data)
            temp_list = list(result)
            temp_str = ' '.join(temp_list)
            output.write(temp_str)

print("end of crawler")
