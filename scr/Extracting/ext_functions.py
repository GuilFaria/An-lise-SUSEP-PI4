"""Melhorias de implementação:
    - Documentar o código *
    - Implementar o Logging *
    - Implementar o Contrato de Dados
    
    Fase 2 - Recompilação e Otimização:
    - Implementar o Parquet
    - Orquestrador
    
    Fase 3 - Conexão com o Data lake
    - Implementar o Google Cloud Storage
    
    Fase 4 - Tratamento dos Dados
    
    Fase 5 - DataViz
    
    Fase 6 - Machine Learning"""

import os
import io
import requests
import sys
import zipfile  
import io
import urllib3
import logging

from dotenv import load_dotenv
from datetime import datetime as dt

load_dotenv()

#--------------- Bloco de Funções -----------------#

def split_tabs(lista) -> list | list:

    Seguros_S = list()
    Seguros_R = list()

    logging.info("Realizando a separação das bases")
    lista.pop(0) # No primeiro registro, encontra-se o link do site (por isso, é excluido.)

    for i in lista:
        
        if i[-16] == 'S':
            Seguros_S.append(i)
        elif i[-16] == 'R':
            Seguros_R.append(i)
        else:
            logging.critical("Nomenclatura ou arquivo modificado. (Revisar Site imediatamente)")
            sys.exit()
    
    logging.info("Separação finalizada")
    return Seguros_R, Seguros_S


def downloads_tab_S(hrefs_tab_S):
    nome_repositorio_temp = "temp_tbs_susep_S"
    local_repository = os.getenv("LOCAL_REPOSITORY")
    
    logging.info("Criando diretório para download dos arquivos")
    # Criar o diretório onde os arquivos serão armazenados
    dir_path = os.path.join(fr"{local_repository}\PI04 - Seguradora\contents", nome_repositorio_temp)
    logging.debug(dir_path)
    os.makedirs(dir_path, exist_ok=True)
    
    logging.info(f"Diretório criado em: {dir_path}")
    count_downloads = 0

    logging.info("Iniciando download dos arquivos")
    for link in hrefs_tab_S:
            try:

                # Nome do arquivo a partir da URL
                nome_tabela = link.split("/")[-1][:-4]
                file_path = os.path.join(dir_path, nome_tabela + ".csv")
                logging.info(f'Baixando tabela {nome_tabela}')

                logging.debug("Diretorio:", dir_path)

                # Fazer o download da tabela
                response = requests.get(link, stream=True, verify= False)
                response.raise_for_status()  # Verifica se houve erro no download
                content = io.BytesIO(response.content)

                logging.debug("print do file_path: ", file_path)
                
                with zipfile.ZipFile(content, 'r') as zip:
                    zip.extractall(dir_path)


                logging.info(f"Sucesso: tabela {nome_tabela} baixada para {file_path}")
                count_downloads += 1
                
            except Exception as e:
                logging.warning(f'Erro ao baixar {link}: {e}')
                
    logging.info(f"Carga das tabelas Ss realizada com sucesso. Total de arquivos baixados: {count_downloads}")

def downloads_tab_R(hrefs_tab_R):
    nome_repositorio_temp = "temp_tbs_susep_R"
    local_repository = os.getenv("LOCAL_REPOSITORY")
    
    logging.info("Criando diretório para download dos arquivos R")
    # Criar o diretório onde os arquivos serão armazenados
    dir_path = os.path.join(fr"{local_repository}\PI04 - Seguradora\contents", nome_repositorio_temp)
    logging.debug(dir_path)
    os.makedirs(dir_path, exist_ok=True)
    
    logging.info(f"Diretório criado em: {dir_path}")
    count_downloads = 0

    logging.info("Iniciando download dos arquivos")
    for link in hrefs_tab_R:
            try:

                # Nome do arquivo a partir da URL
                nome_tabela = link.split("/")[-1][:-4]
                file_path = os.path.join(dir_path, nome_tabela + ".csv")
                logging.info(f'Baixando tabela {nome_tabela}')

                logging.debug("Diretorio:", dir_path)

                # Fazer o download da tabela
                response = requests.get(link, stream=True, verify= False)
                response.raise_for_status()  # Verifica se houve erro no download
                content = io.BytesIO(response.content)

                logging.debug("print do file_path: ", file_path)
                
                with zipfile.ZipFile(content, 'r') as zip:
                    zip.extractall(dir_path)


                logging.info(f"Sucesso: tabela {nome_tabela} baixada para {file_path}")
                count_downloads += 1
                
            except Exception as e:
                logging.warning(f'Erro ao baixar {link}: {e}')
                
    logging.info(f"Carga das tabelas Rs realizada com sucesso. Total de arquivos baixados: {count_downloads}")

