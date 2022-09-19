import re

# https://www.bytebank.com.br/cambio

padrao_url = re.compile('(http(s)://)?(www.)?bytebank.com(.br)?/cambio')
match = padrao_url.match(self.url)
    if not match:
        raise ValueError ('A URL não é valida')