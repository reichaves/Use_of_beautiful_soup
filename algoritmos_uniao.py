import requests 
from bs4 import BeautifulSoup
import saraiva1
import novatec1

def func_novatec (nome_livro):
	url = 'http://www.novatec.com.br/busca.php'
	r = novatec1.post_http(url, nome_livro)
	lista_produto = []
	if r:
		lista_produto = novatec1.parse_html(r.text)
	return lista_produto

def func_saraiva (nome_livro):
	url = 'http://busca.saraiva.com.br/'
	r = saraiva1.get_http(url, nome_livro)
	
	if r: 
		lista_produtos = saraiva1.get_produtos(r.text)
		lista = saraiva1.get_http_page_produto(lista_produtos)
	return lista

def main(nome_livro):
	d_produtos = {}
	lista_produto = func_novatec(nome_livro)
	d_produtos.update({'novatec':lista_produto})

	lista = func_saraiva(nome_livro)
	d_produtos.update({'saraiva':lista})

	return d_produtos

if __name__ == '__main__':
	nome_livro = input ("Nome do livro: ")
	d_produtos = main(nome_livro)
	print(d_produtos)

