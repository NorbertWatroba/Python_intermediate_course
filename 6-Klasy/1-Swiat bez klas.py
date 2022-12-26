
def show_cake_info(cake):
    print(f'{cake["taste"]} cake with {cake["glaze"]} glaze with text "{cake["text"]}" of {cake["weight"]} kg')


cake_01 = {'taste' : 'vanilla',
           'glaze' : 'chocolate',
           'text'  : 'happy Birthday',
           'weight': 0.7}

cake_02 = {'taste' : 'tee',
           'glaze' : 'lemon',
           'text'  : 'Happy Python Coding',
           'weight': 1.3}

cakes = [cake_01, cake_02]

for c in cakes:
    show_cake_info(c)

