import requests
import os


def save_url_to_file(url, file_path):
    r = requests.get(url, stream=True)
    with open(file_path, "wb") as f:
        f.write(r.content)


url = 'http://www.mobilo24.eu/spis/'
dir = './1.files'
tmpfile = 'download.tmp'
file = 'spis.html'

tmpfile_path = os.path.join(dir, tmpfile)
file_path = os.path.join(dir, file)

try:
    if os.path.isfile(tmpfile_path):
        os.remove(tmpfile_path)
        print('deleted temp file')
    save_url_to_file(url, tmpfile_path)
    with open(tmpfile_path, 'r') as tmp, open(file_path, 'w') as file:
        content = tmp.read()
        file.write(content)
except Exception as e:
    print(e)
else:
    print('Operation successful!')
finally:
    if os.path.isfile(tmpfile_path):
        os.remove(tmpfile_path)
    print('Process finished')
