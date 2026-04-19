from GerarPdf import GerarPdf
from ValidadorDeJson import ValidadorDeJson
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
                tam = len(str(len(historia['urls'])))
                for i,v in enumerate(historia['urls']):
                    pdf = GerarPdf(f'{historia["nome"]}/{historia["nome"]} - cap {(i+1):0{tam}}', v)
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