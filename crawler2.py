import requests
from bs4 import BeautifulSoup

# Specify url: url
url = 'https://192.168.50.195/ossim/#dashboard/overview/overview'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Extracts the response as html: html_doc
html_doc = r.text

# Create a BeautifulSoup object from the HTML: soup
soup = BeautifulSoup(html_doc, 'lxml')

# Prettify the BeautifulSoup object: pretty_soup
pretty_soup = soup.prettify()

# Print the response

x = eval(input("enter 1 to get all links and 2 to get entire code\n"))
if(x==2):
    print(pretty_soup)

elif(x==1):
    for link in soup.find_all('a'):
        print(link.get('href'))
