import urllib3

from web_scrapping import *
from ext_functions import *

urllib3.disable_warnings()

if __name__ == '__main__':
    url = "https://www.gov.br/susep/pt-br/central-de-conteudos/dados-estatisticos/bases-anonimizadas/bases_auto"
    request = fetch_page(url)
    links = parse_page(request)
    hrefs_table_r, hrefs_table_s = split_tabs(links)
    downloads_tab_S(hrefs_table_s)