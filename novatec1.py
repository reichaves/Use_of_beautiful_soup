import requests
from bs4 import BeautifulSoup

def post_http(url, nome_livro): 
	payload = {'palavra':	nome_livro,
			'enviar':	'Buscar'}

	try:
		return requests.post(url, data=payload)
	except (requests.exceptions.HTTPError, requests.exceptions.RequestException, requests.exceptions.ConnectionError, requests.exceptions.Timeout) as e:
		print (str(e))
		pass 
	except Exception as e:
		raise
	return None 

def tratar_dados(lista_auxiliar):
	preco = lista_auxiliar[6].replace('Preço: ', '')
	d = {'titulo': lista_auxiliar[0],
	      'url_capa': lista_auxiliar[7],
	      'url_produto': lista_auxiliar[8],
	       'preco': lista_auxiliar[6]}
	return d 

def parse_html(content): 
	soup = BeautifulSoup(content, 'lxml')

	produtos = soup.find_all('table')[10].find_all('td')

	'''f = open('td.html', 'w', encoding='utf-8') 

	for produto in produtos:
		f.write(str(produto))
		f.write('\n\n\n')

	f.close'''

	lista_auxiliar = []
	lista_produto = []
	url = 'http://www.novatec.com.br/'
	url_capa = ''
	url_produto =''

	for produto in produtos:
		tag_a = produto.find('a')
		if tag_a:
			if tag_a.next_element.next_element.name == 'img':
				url_capa = format(tag_a.img.get('src'))
				url_produto = "{0}{1}".format(url, tag_a.get('href'))
				

		for string in produto.stripped_strings: 
			if (string == 'Esgotado'):
				continue
			lista_auxiliar.append(string)
		if(len(lista_auxiliar) > 6):
			lista_auxiliar.append(url_capa)
			lista_auxiliar.append(url_produto)
			lista_produto.append(tratar_dados(lista_auxiliar))
		
		del lista_auxiliar[:]

	if (len(lista_produto) > 0):
		del lista_produto[0]
	return lista_produto
		

	

if __name__ == '__main__':
	url = 'http://www.novatec.com.br/busca.php'
	r = post_http(url, nome_livro)

	#with open('result.html', 'w', encoding='utf-8') as f:
	#	f.write(r.text)

	lista_produto = []

	if r:
		lista_produto = parse_html(r.text)
	print(lista_produto)
