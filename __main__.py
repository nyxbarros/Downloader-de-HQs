from Downloader import Downloader
from pathlib import Path
import argparse
import json
import sys

def main():
    if len(sys.argv) == 1:
        Downloader.pelo_input()
    elif "-h" in sys.argv or "--help" in sys.argv:
        parser = argparse.ArgumentParser()
        parser.add_argument(" ", help="Usar o arquivo dados.json com input")
        parser.add_argument("JSON", help="Usar o arquivo dados.json com input")
        parser.add_argument("<local para salvar>", help="Pasta onde será salvo os arquivos baixados")
        parser.add_argument("<urls das HQs>", help="URLs das HQs que serão baixadas")
        parser.parse_args()
    elif not 'JSON' in sys.argv:
        Downloader.pelo_terminal(sys.argv)
    elif Path('dados.json').is_file():
        with open('dados.json', 'r', encoding='utf-8') as arq:
            dados = json.load(arq)
        Downloader.pelo_json(dados)
    else:
        print('Não foi possível baixar')
    

if __name__ == "__main__":
    main()


