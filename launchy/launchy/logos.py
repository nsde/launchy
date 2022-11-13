import requests

try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

title = 'Minecraft'

title = title.replace(' ', '+')
url = f'https://duckduckgo.com/?q={title}+wallpaper+site%3Areddit.com&iar=images&iaf=layout%3AWide&iax=images&ia=images'

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:84.0) Gecko/20100101 Firefox/84.0",
}

html = requests.get(url, headers=headers).text
print(html)

soup = BeautifulSoup(html, features='html.parser')
print(url)
print(soup.find_all('img', class_='tile--img__img', src=True))
