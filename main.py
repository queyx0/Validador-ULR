url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"

# Sanatização 
url = url.strip()

# Validação
if url == "":
    raise ValueError('A URL está vazia')

# Separa base de parametros
indice_interrogacao = url.find('?')
url_base = url[:indice_interrogacao]
url_parametros = url[indice_interrogacao+1:]
print(url_parametros)

# Busca valor de um parametro
parametro_de_busca = 'quantidade'
indice_parametro = url_parametros.find(parametro_de_busca)
indice_valor = indice_parametro + len(parametro_de_busca) + 1
print(indice_valor)
indice_e_comercial = url_parametros.find('&', indice_valor)

if indice_e_comercial == -1:
    valor = url_parametros[indice_valor :]
else:
    valor = url_parametros[indice_valor : indice_e_comercial]
print(valor)
