from bs4 import BeautifulSoup
with open('arquivo02.html', 'r') as f:
	soup = BeautifulSoup(f, 'lxml')

from bs4.element import NavigableString, Tag

for tag in soup.descendants:
	if isinstance(tag, NavigableString):
		print(tag)
	else:
		print(tag.name)

for tag in soup.descendants:
	if isinstance(tag, Tag):
		print(tag)

# diferença entre strings e stripped_strings - remove espaços

for string in soup.aside.strings:
	print(repr(string))

for string in soup.aside.stripped_strings:
	print(repr(string))

