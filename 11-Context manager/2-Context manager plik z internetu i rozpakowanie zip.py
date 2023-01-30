from pathlib import Path
import requests
from zipfile import ZipFile


class FileFromWeb:
    def __init__(self, url: str, tmp_file: str):
        self.url = url
        self.tmp_file = Path(tmp_file)

    def __enter__(self):
        response = requests.get(self.url)
        with open(self.tmp_file, 'wb') as file:
            file.write(response.content)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.tmp_file.unlink()


with FileFromWeb('https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip', 'tmp_file') as f:
    with ZipFile(f.tmp_file, 'r') as z:
        a_file = z.namelist()[0]
        print(a_file)
        z.extract(a_file, '.', None)
