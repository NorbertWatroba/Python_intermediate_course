from pathlib import Path
from itertools import groupby


def scan_tree(path: Path):
    for location in path.glob('*'):
        if location.is_dir():
            yield {'type': 'dir', 'path': location}
            yield from scan_tree(location)
        else:
            yield {'type': 'path', 'path': location}

'''
listing = scan_tree(Path('/Users/norbertwatroba/PycharmProjects/Python_intermediate_course'))

for element in listing:
    print(element['type'], element['path'])'''

listing = scan_tree(Path('/Users/norbertwatroba/PycharmProjects/Python_intermediate_course'))
listing = sorted(listing, key=lambda x: x['type'])
for element_type, elements in groupby(listing, lambda x: x['type']):
    print(element_type, list(map(lambda x: x['path'].name, elements)))
