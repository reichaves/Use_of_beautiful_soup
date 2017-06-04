import requests

#método post

url='http://www.buscacep.correios.com.br/sistemas/buscacep/resultadoBuscaCepEndereco.cfm'

payload = {'relaxation':	'12240000',
'tipoCEP':	'ALL',
'semelhante':	'N'}

response = requests.post(url, data=payload)

with open('correios.html', 'w') as f:
	f.write(response.text)
	
