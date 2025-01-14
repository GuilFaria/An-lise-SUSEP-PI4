import urllib3
import logging
from dotenv import load_dotenv
from datetime import datetime as dt

from web_scrapping import *
from ext_functions import *


load_dotenv()

urllib3.disable_warnings()

local_repository = os.getenv("LOCAL_REPOSITORY")


datenow = dt.now().strftime("%d/%m/%y") 


date_mes_nome = dt.now().strftime("%m_%y") 

if not os.path.exists(fr"{local_repository}\PI04 - Seguradora\log\{date_mes_nome}"):
    os.makedirs(fr"{local_repository}\PI04 - Seguradora\log\{date_mes_nome}")

logging.basicConfig(filename=fr"{local_repository}\PI04 - Seguradora\log\{date_mes_nome}\ext_{dt.now().strftime(r'%d-%H~%M~%S')}.log",
                    level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


if __name__ == '__main__':
    url = "https://www.gov.br/susep/pt-br/central-de-conteudos/dados-estatisticos/bases-anonimizadas/bases_auto"
    request = fetch_page(url)
    links = parse_page(request)
    hrefs_table_r, hrefs_table_s = split_tabs(links)
    downloads_tab_S(hrefs_table_s)
    downloads_tab_R(hrefs_table_r)