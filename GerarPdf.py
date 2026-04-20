import os
import re
import requests
import shutil

from PIL import Image

from Controller import Controller

class GerarPdf:
    def __init__(self, local_para_salvar: str, url: str):
        self.url = url
        self.local_para_salvar = 'download/'+local_para_salvar if not local_para_salvar[0] == '/' else local_para_salvar
        self.imgs = []
        self.pdf = ''

    def baixar_imagens(self):
        # baixar as imagens
        import os
        print("Link acessado: "+self.url)
        links = Controller.controller(self.url)
        for i, v in enumerate(links):
            os.makedirs(self.local_para_salvar, exist_ok=True)  # cria a pasta se não existir
            
            resposta = requests.get(v)

            quantCasas = int(len(str(len(links))))

            with open(f"{self.local_para_salvar}/imagem{(i+1):0{quantCasas}}.jpg", "wb") as f:
                f.write(resposta.content)
                
            self.imgs.append(f"{self.local_para_salvar}/imagem{(i+1):0{quantCasas}}.jpg")

    def imgParaPdf(self, deletar_pasta_com_imagens = False):
        self.pdf = self.local_para_salvar + '.pdf'
        
        def extrair_numero(nome):
            numeros = re.findall(r"\d+", nome)
            return int(numeros[0]) if numeros else 0

        arquivos = sorted(
            [f for f in os.listdir(self.local_para_salvar) if f.endswith((".jpg", ".png", ".jpeg"))],
            key=extrair_numero
        )

        imagens = [
            Image.open(os.path.join(self.local_para_salvar, img)).convert("RGB")
            for img in arquivos
        ]

        if imagens:
            imagens[0].save(self.pdf, save_all=True, append_images=imagens[1:])
            print(f"Foi criado: {self.pdf}")
    
        if deletar_pasta_com_imagens:
            shutil.rmtree(self.local_para_salvar)