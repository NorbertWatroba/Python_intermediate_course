import pickle
import glob

class Cake:
    known_types = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel', 'other']
    bakery_offer = []


    def __init__(self, name:str, kind:str, taste:str, additives:list, filling:str=None, gluten_free:bool=False, text:str=''):
        Cake.bakery_offer.append(self)
        self.name = name
        if kind in Cake.known_types:
            self.kind = kind
        else:
            self.kind = 'other'
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
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
        print(f'| Text:{"":24}|\n|{self.Text:^30}|')
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

    def save_to_file(self, path):
        with open(path, "bw") as f:
            pickle.dump(self, f)

    @classmethod
    def read_from_file(cls, path):
        with open(path, "br") as f:
            obj = pickle.load(f)
        cls.bakery_offer.append(obj)
        return obj

    @staticmethod
    def get_bakery_files(directory='.'):
        return glob.glob(fr'{directory}/*.bakery')


cake1 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolate', 'nuts'], 'cream', text='Happy Anniversary!')
muffin1 = Cake('Chocolate Muffin', 'muffin', 'chocolate', ['chocolate'])
meringue1 = Cake('Super Sweet Meringue', 'meringue', 'very sweet', [], gluten_free=True)
waffle1 = Cake('Cocoa waffle', 'waffle', 'cocoa', [], 'cocoa')

cake1.save_to_file(r'cake1.bakery')
cake2 = Cake.read_from_file(r'cake1.bakery')
cake2.show_info()

print(dir(cake2))
cake2.text = 'Happy birthday!'
cake2.show_info()
cake2.save_to_file(r'cake2.bakery')
files = Cake.get_bakery_files()
for file in files:
    print(file)
for item in Cake.bakery_offer:
    print(item.name)
