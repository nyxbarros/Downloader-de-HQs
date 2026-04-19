# Meu Projeto

Idiomas:
- [English](README.md)
- Português (atual)
- [Español](README.es.md)

## SOBRE

Projeto tem por finalidade permitir a possibilidade de baixar HQs e quadrinhos de plataformas online que não tenham uma forma de ler offline nativamente, para possibilitar a leitura completamente offline, por meio de aparelhos como kindle


## COMO CLONAR O PROGRAMA
```
git clone git@github.com:nyxbarros/Downloader-de-HQs.git
```

## COMO INSTALAR
```sh
cd Downloader-de-HQs/
chmod +777 setup.sh
./setup.sh
``` 

## COMO USAR

comando de ajuda: `python3 . -h`

### POR MEIO DE PARAMETROS BASH
1. rodar o comando de inicialização:
    ```bash

    python3 . <pasta onde será salvo as imagens> <URLs dos capítulos>
    ```

### POR MEIO DE JSON
1. condigurar o arquivo dados.json
    1. Objeto
        ```json
        {
            "nome":"<titulo da história>",
            "urls": [
                <lista das urls completas de cada capitulo>
            ]
        }
        ```
    2. Lista
        ```json
        [
            <Objeto 1>,
            <Objeto 2>,
            <Objeto 3>,
            ...
            <Objeto n>
        ]
        ```
2. rodar o comando de inicialização
    ```bash
    cd "<caminho até o diretório>/Downloader de HQs/"
    python3 . JSON
    ```

#### EXEMPLO DE JSON
```
[
    {
        "nome":"café com leite",
        "urls": [
            "https://tapas.io/episode/3229980",
            "https://tapas.io/episode/3229989",
            "https://tapas.io/episode/3244182",
            "https://tapas.io/episode/3310705",
            "https://tapas.io/episode/3412364",
            "https://tapas.io/episode/3574664"
        ]
    }
]
```

### POR MEIO DE INPUT PYTHON
1. rodar o comando de inicialização
    ```bash
    cd "<caminho até o diretório>/Downloader de HQs/"
    python3 .
    ```
2. preencher o primeiro input com protocolo + dominio do site
3. preencher o segundo e demais inputs com as URLs dos capítulos
4. enviar um input vazio para prosseguir o processo

## FONTES JÁ PROGRAMADAS
* https://tapas.io/

## COMO ADICIONAR OUTRAS PLATAFORMAS
Quem faz toda a gerencia de quais sites estão cadastrados ou não é o Controller.py, para adicionar algum site, precisa ir na função Controller.controller(), adicionar o site lá e criar uma função que extraia apenas os links das imagens da história que está no html retornado e que retorne a lista de urls