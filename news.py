from bs4 import BeautifulSoup
import requests

counter = 1

result = requests.get('https://www.bbc.co.uk/')
content = result.content
html_parser = BeautifulSoup(content, 'html.parser')
html_span = html_parser.find_all('span', 'top-story__title')
html_link = html_parser.find_all('a', 'top-story')

for link, title in zip(html_link, html_span):
    link = link.attrs['href']
    title = title.string.strip()
    print(f'{counter}) {title}: {link}')
    counter += 1

