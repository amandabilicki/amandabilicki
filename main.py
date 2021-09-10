import requests
import os
import pandas as pd
from zipfile import ZipFile

def baixar_arquivo(url, endereco):
    """faz requisiçao ao servidor"""
    resposta = requests.get(url)
    if resposta.status_code == requests.codes.OK:
        with open(endereco, 'wb') as novo_arquivo:
            novo_arquivo.write(resposta.content)
        print("Download finalizado. Salvo em: {}".format(endereco))
        """mostra o local onde foi salvo o arquivo"""
    else:
        resposta.raise_for_status()

if __name__ == "__main__":
    BASE_URL = 'http://200.152.38.155/CNPJ/K3241.K03200Y{}.D10710.EMPRECSV.zip'
    OUTPUT_DIR = 'output'
    for i in range(1, 2):  # define o range de arquivos disponiveis na pagina  e faz o loop para download
        nome_arquivo = os.path.join(OUTPUT_DIR, 'CNPJ_Empresa_{}.zip'.format(i))
        baixar_arquivo(BASE_URL.format(i), nome_arquivo)


file_ext = ZipFile

with ZipFile('/home/Amanda/PycharmProjects/Raspagem-Pipeline-RoitBank/output/CNPJ_Empresa_1.zip', 'r') as z:
    z.printdir()
    z.extractall('/home/Amanda/PycharmProjects/Raspagem-Pipeline-RoitBank/output/Arquivos_csv')

arquivo = pd.reader_csv('K3241.K03200Y1.D10710.EMPRECSV', sep=';', encodings='ISO-8859-1', nrows=50)
