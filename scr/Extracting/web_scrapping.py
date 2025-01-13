import logging.config
import requests
import logging

from bs4 import BeautifulSoup


#/--------------Funções para o Web Scrapping-------------/

def fetch_page(url):
    logging.info(f"Iniciando o requerimento para a página: {url}")
    geted = requests.get(url, verify=False)
    if geted.status_code == 200:
        logging.info(f"Requerimento para a página {url} realizado com sucesso")
    else:
        logging.critical(f"Requerimento para a página {url} falhou")

    return geted.text

def parse_page(html):
    logging.info("Realizando o Scrapping da página")
    soap = BeautifulSoup(html, 'html.parser')
    
    downloads_links = soap.find_all('a', class_="external-link")
    hrefs = [link['href'] for link in downloads_links]
    logging.info("Scrapping dos Links de referência realizado com sucesso")

    return hrefs