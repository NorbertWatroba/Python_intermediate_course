class Cake:
    known_types = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel', 'other']
    bakery_offer = []


    def __init__(self, name:str, kind:str, taste:str, additives:list, filling:str=None, gluten_free:bool=False, text:str=''):
        self.name = name
        if kind in Cake.known_types:
            self.kind = kind
        else:
            self.kind = 'other'
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        Cake.bakery_offer.append(self)
        self.__gluten_free = gluten_free
        if self.kind == 'cake' or text == '':
            self.__text = text
        else:
            self.__text = ''
            print(f'Cannot add text "{text}" to {self.name}')


    def show_info(self):
        print(f'''| {self.name.upper():29}|
| Kind:        {self.kind:16}|
| Taste:       {self.taste:16}|''')
        if self.additives:
            print(f'| Additives:{"":19}|')
            for a in self.additives:
                print(f'|{"":14}{a:16}|')
        if self.filling:
            print(f'| Filling:     {self.filling:16}|')
        print(f'| Gluten-free: {self.__gluten_free:<16}|')
        print(f'|{"-"*30}|')


    def set_filling(self, filling):
        self.filling = filling

    def add_additives(self, additives:list):
        self.additives.extend(additives)


    def __get_text(self):
        return self.__text

    def __set_text(self, new_text):
        if self.kind == 'cake':
            self.__text = new_text
        else:
            print(f'Cannot add text "{new_text}" to {self.name}')

    Text = property(__get_text, __set_text)

cake1 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolate', 'nuts'], 'cream', False, 'Happy Anniversary!')
muffin1 = Cake('Chocolate Muffin', 'muffin', 'chocolate', ['chocolate'], None, False, 'wrong text')
meringue1 = Cake('Super Sweet Meringue', 'meringue', 'very sweet', [],None, True, '')
waffle1 = Cake('Cocoa waffle', 'waffle', 'cocoa', [], 'cocoa', False, 'Happy birthday!')

for item in Cake.bakery_offer:
    print(dir(item))
print("="*100)
cake1.Text = 'Merry Christmas'
meringue1.Text = 'not allowed'
print("="*100)
for item in Cake.bakery_offer:
    print(dir(item))
