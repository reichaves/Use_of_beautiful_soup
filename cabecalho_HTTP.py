import requests

from bs4 import BeautifulSoup

url = 'http://michaelis.uol.com.br/busca?'

payload ={'r':	'0',
'f':	'0',
't':	'0',
'palavra':	'talk'}

r = requests.get(url, params=payload)

with open('michaelis.html', 'w', encoding='utf-8') as f:
	f.write(r.text)

print(r.request.headers)
