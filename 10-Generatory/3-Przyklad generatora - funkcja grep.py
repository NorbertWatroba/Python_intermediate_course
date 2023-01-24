from pathlib import Path
import requests


def gen_get_file_lines(file: Path):
    for line in open(file):
        yield line.replace('\n', '')


def check_web_page(url):
    try:
        code = requests.get(url).status_code
        return code == 200
    except Exception:
        return False


root = Path('./3files')
gen_get_files = (path for path in root.glob('*') if path.is_file())

for file in gen_get_files:
    for line in gen_get_file_lines(file):
        print(f'{file} - {line} - {check_web_page(line)}')

'''
with open('3files/pl.txt', 'w') as f:
    f.write('http://www.wykop.pl/\n')
    f.write('http://www.ale-beka-jest-taki-adres.pl/\n')
    f.write('http://www.demotywatory.pl')

with open('3files/com.txt', 'w') as f:
    f.write('http://www.realpython.com/\n')
    f.write('http://www.nonexistenturl.com/\n')
    f.write('http://www.stackoverflow.com')
'''