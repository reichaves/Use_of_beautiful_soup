import requests
from bs4 import BeautifulSoup
r = requests.get("http://atendimentovirtual.spu.planejamento.gov.br/Consultas/Fin_Pedido.asp")
soup = BeautifulSoup(r.text, 'lxml')
print(soup)
