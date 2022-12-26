from os import path
import requests
import functools


def save_url_file(url, directory, file, msg):
    print(msg.format(file))

    r = requests.get(url, stream=True)
    file_path = path.join(directory, file)

    with open(file_path, "wb") as f:
        f.write(r.content)


directory = r'C:\Users\Norbe\Desktop\Udemy\Python\Python dla średniozaawansowanych\5-Funkcje - scenariusze zastosowań'
msg = "Please wait: {}"
save_url_to_dir = functools.partial(save_url_file, directory=directory, msg=msg)

url = 'http://mobilo24.eu/spis'
file = 'spis.html'
save_url_to_dir(url=url, file=file)

url = 'https://www.mobilo24.eu/wp-content/uploads/2015/11/Mobilo_logo_kolko_512-565b1626v1_site_icon.png'
file = 'logo.png'
save_url_to_dir(url=url, file=file)
