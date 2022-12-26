from urllib.request import urlretrieve

pages = [
    {'name': 'onet', 'url': 'https://www.onet.pl'},
    {'name': 'udemy', 'url': 'https://www.udemy.com'},
    {'name': 'gmail', 'url': 'https://www.gmail.com'},
]

path = r'./2-Zmienne i kod/sites/'

for site in pages:
    name = f'{site["name"]}.html'
    try:
        urlretrieve(site["url"], f'{path}{name}')
    except OSError:
        print('Error occurred')
        break
else:
    print('Operation successful')
