import os


def ilosc_slow(_path):
    f = open(_path)
    text = f.read()
    count = len(text.split())
    return count


if __name__ == '__main__':
    path = r'/2-Zmienne i kod/plik.txt'
    # =================================================== #
    if os.path.isfile(path):
        print(f'Ilość słów w pliku: {ilosc_slow(path)}')

    os.path.isfile(path)
    # =================================================== #
    os.path.isfile(path) and print(f'Ilość słów w pliku: {ilosc_slow(path)}')
