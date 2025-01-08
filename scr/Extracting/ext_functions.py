"""Melhorias de implementação:
    - Documentar o código
    - Implementar o Logging
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

from dotenv import load_dotenv
from datetime import datetime as dt


load_dotenv()
#--------------- Bloco de Funções -----------------#

def split_tabs(lista) -> list | list:

    Seguros_S = list()
    Seguros_R = list()


    lista.pop(0) # No primeiro registro, encontra-se o link do site (por isso, é excluido.)

    for i in lista:
        
        if i[-16] == 'S':
            Seguros_S.append(i)
        elif i[-16] == 'R':
            Seguros_R.append(i)
        else:
            print("Erro Crítico: Nomenclatura ou arquivo modificado.\nRevisar Site imediatamente.")
            sys.exit()
    return Seguros_R, Seguros_S


def downloads_tab_S(hrefs_tab_S):
    nome_repositorio_temp = "temp_tbs_susep_S"
    local_repository = os.getenv("LOCAL_REPOSITORY")

    # Criar o diretório onde os arquivos serão armazenados
    dir_path = os.path.join(fr"{local_repository}\PI04 - Seguradora\contents", nome_repositorio_temp)
    print(dir_path)
    os.makedirs(dir_path, exist_ok=True)

    count = 0
    for link in hrefs_tab_S:
        if count != 2:
            try:
                # Nome do arquivo a partir da URL
                nome_tabela = link.split("/")[-1][:-4]
                file_path = os.path.join(dir_path, nome_tabela + ".csv")
                print(f'Baixando tabela {nome_tabela} | {dt.now()}')

                print("diretorio", dir_path)
                # Fazer o download da tabela
                response = requests.get(link, stream=True, verify= False)
                response.raise_for_status()  # Verifica se houve erro no download
                content = io.BytesIO(response.content)

                print("print do file_path: ", file_path)
                with zipfile.ZipFile(content, 'r') as zip:
                    zip.extractall(dir_path)

                # Salvar o conteúdo em um arquivo
                # with open(file_path, "wb") as file:
                #     for chunk in response.iter_content(chunk_size=1024):
                #         if chunk:
                #             file.write(chunk)

                print(f"Sucesso: tabela {nome_tabela} baixada para {file_path} | {dt.now()}")
                count += 1
            except Exception as e:
                print(f'Erro ao baixar {link}: {e}')
                count += 1

    print(f"Teste realizado | {dt.now()}")


