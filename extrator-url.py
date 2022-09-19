import re

class ExtratorUrl():
    def __init__(self, url):
        self.url = self.sanatiza_url(url)
        self.valida_url()

    def sanatiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def valida_url(self):
        if not self.url:
            raise ValueError("A URL está vazia")

        padrao_url = re.compile("(http(s)://)?(www.)?bytebank.com(.br)?/cambio")
        match = padrao_url.match(self.url)
        if not match:
            raise ValueError ("A URL não é valida")

    def get_url_base(self):
        indice_interrogacao = self.url.find("?")
        url_base = self.url[:indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        indice_interrogacao = self.url.find("?")
        url_parametros = self.url[indice_interrogacao+1:]
        return url_parametros
                
    def get_valor_parametros(self, parametro_de_busca):
        indice_parametro = self.get_url_parametros().find(parametro_de_busca)
        indice_valor = indice_parametro + len(parametro_de_busca) + 1
        indice_e_comercial = self.get_url_parametros().find("&", indice_valor)
        
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor :]
        else:
            valor = self.get_url_parametros()[indice_valor : indice_e_comercial]
        return valor

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return self.url

    def __eq__(self, other):
        return self.url == other.url

extrator_url = ExtratorUrl("bytebank.com/cambio?quantidade=100&moedaOrigem=1&moedaDestino=dolar")
#quantidade = extrator_url.get_valor_parametros("quantidade")
#print(quantidade)
#print(f"O tamnho da URL é de: {len(extrator_url)}")

valor_dolar = 5.5
moeda_origem = extrator_url.get_valor_parametros("moedaOrigem")
moeda_destino = extrator_url.get_valor_parametros("moedaDestino")
quantidade = extrator_url.get_valor_parametros("quantidade")

conversao = int(moeda_origem) * valor_dolar
print(conversao)

