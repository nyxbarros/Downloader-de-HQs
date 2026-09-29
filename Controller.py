import requests

from bs4 import BeautifulSoup

from Utils import Lista

class Controller:
    def controller(url: str):
        if 'https://tapas.io/' in url:
            return Controller.baixar_tepas_io(url)
        elif 'https://yurionair.top/' in url:
            return Controller.baixar_yurionair_top(url)
        elif 'https://ranfren.neocities.org/' in url:
            return Controller.baixar_ranfren(url)
        else:
            print('esse dominio não foi cadasttrado ainda')
            exit()
    
    def baixar_tepas_io(url):
        # acessar HTML
        headers = {
            "User-Agent": "Mozilla/5.0"
        }
        resposta = requests.get(url, headers=headers)
        html = Lista(str(BeautifulSoup(resposta.text, "html.parser")).split('\n')).map(lambda x: x.strip()).filter(lambda x: 'data-src' in x).map(lambda x: x.split(' '))

        # extrair links
        links = []
        for i, v in enumerate(html):
            for i2, v2 in enumerate(v):
                if 'data-src' in v2:
                    img = v2.split('=')[1]
                    links.append(img.replace('"', ''))
                    break
        return links
    
    def baixar_yurionair_top(url):
        # acessar HTML
        resposta = requests.get(url)
        html = Lista(str(BeautifulSoup(resposta.text, "html.parser")).split('\n')).map(func=lambda x: x.strip()).filter(lambda x: 'class="wp-manga-chapter-img"' in x).map(lambda x: x.replace('src=" http', 'src="https')).map(lambda x: x.split(' '))

        # extrair links
        links = []
        for i, v in enumerate(html):
            for i2, v2 in enumerate(v):
                if 'src' in v2:
                    img = v2.split('=')[1]
                    links.append(img.replace('"', '')[:-2])
                    break
        return links
    
    def baixar_ranfren(url):
        # acessar HTML
        resposta = requests.get(url)
        html = str(BeautifulSoup(resposta.text, "html.parser")).replace('><', '>\n<').split('\n')

        # apenas ficar com as tags que tem imagens da hq
        html = [i for i in html if 'img' in i]

        # extrair links
        links = []
        for i, v in enumerate(html):
            img = v.split('=')[1]
            links.append(img.replace('"', '')[:-2])
        return links





