class ValidadorDeJson:
    def validar(lista_json):
        if type(lista_json) is not list:
            return 'o json precisa ser uma lista'
        for i, obj in enumerate(lista_json):
            if 'nome' not in obj:
                return f'No elemento {i+1}, falta propriedade "nome"'
            if type(obj['nome']) is not str:
                return f'A propriedade "nome" do elemento {i+1} precisa ser do tipo string'
            if 'urls' not in obj:
                return f'No elemento {i+1}, falta propriedade "urls"'
            if type(obj['urls']) is not list:
                return f'A propriedade "urls" do elemento {i+1} precisa ser do tipo list'
            for i2, obj2 in enumerate(obj["urls"]):
                if type(obj2) is not str:
                    return f'A url {i2+1} do elemento {i+1} precisa ser do tipo string'
        return True