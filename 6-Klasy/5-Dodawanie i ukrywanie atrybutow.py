class Cake:
    known_types = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel', 'other']
    bakery_offer = []

    def __init__(self, name: str, kind: str, taste: str, additives: list, filling: str = None, gluten_free: bool = False):
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

    def show_info(self):
        print(f'''| {self.name.upper():29}|
| Kind:        {self.kind:16}|
| Taste:       {self.taste:16}|''')
        if self.additives:
            print(f'| Additives:{"":19}|')
            for a in self.additives:
                print(f'|\t{a:23}|')
        if self.filling:
            print(f'| Filling: {self.filling:20}|')
        print(f'| Gluten-free: {self.__gluten_free:<16}|')
        print(f'|{"-"*30}|')

    def set_filling(self, filling):
        self.filling = filling

    def add_additives(self, additives: list):
        self.additives.extend(additives)


cake1 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolate', 'nuts'], 'cream', False)
muffin1 = Cake('Chocolate Muffin', 'muffin', 'chocolate', ['chocolate'], None, False)
meringue1 = Cake('Super Sweet Meringue', 'meringue', 'very sweet', [], None, True)
cake04 = Cake('Cocoa waffle', 'waffle', 'cocoa', [], 'cocoa', False)


meringue1.__gluten_free = False
meringue1.show_info()
print(f'{dir(meringue1)=}\n')
meringue1._Cake__gluten_free = False
meringue1.show_info()
print(f'{dir(meringue1)=}\n')
