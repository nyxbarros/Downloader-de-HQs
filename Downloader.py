from GerarPdf import GerarPdf
from Utils import Lista
from ValidadorDeJson import ValidadorDeJson
from pathlib import Path
import os
import requests

class Downloader:
    def pelo_input():
        local_para_salvar = input('Pasta onde será salvada as imagens baixadas: ')
        while True:
            url = input('Página html do tepas.io a ser baixada: ')
            if url == '':
                print("fechar programa")
                break
            r = requests.head(url, timeout=5)
            if r != 200:
                print(r.status_code)
            else:
                pdf = GerarPdf(local_para_salvar, url)
                pdf.baixar_imagens_do_site()
                pdf.imgParaPdf()
        
    def pelo_json(dados):
        json_valido = ValidadorDeJson.validar(dados)
        if json_valido == True:
            for historia in dados:
                historia["nome"] = historia["nome"].strip()
                pasta = Path('download/'+historia["nome"])
                if pasta.is_dir():
                    comeco = len(Lista(os.listdir(pasta)).filter(lambda x: x.lower().endswith(".pdf")))
                else:
                    comeco = 0
                tam = len(str(len(historia['urls'])))
                for i,v in enumerate(historia['urls']):
                    pdf = GerarPdf(f'{historia["nome"]}/{historia["nome"]} - cap {(i+1+comeco):0{tam}}', v)
                    pdf.baixar_imagens()
                    pdf.imgParaPdf(True)
        else:
            print(json_valido)
            
    def pelo_terminal(argumentos):
        local_para_salvar = argumentos[0]
        urls = argumentos[:1]
        for url in urls:
            pdf = GerarPdf(local_para_salvar, url)
            pdf.baixar_imagens()
            pdf.imgParaPdf()