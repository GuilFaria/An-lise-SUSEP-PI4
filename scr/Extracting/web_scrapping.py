import requests

from bs4 import BeautifulSoup


def fetch_page(url):
    geted = requests.get(url, verify=False)

    return geted.text

def parse_page(html):
    soap = BeautifulSoup(html, 'html.parser')
    
    downloads_links = soap.find_all('a', class_="external-link")
    hrefs = [link['href'] for link in downloads_links]


    return hrefs