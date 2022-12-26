class Cake:
    known_types = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel', 'other']
    bakery_offer = []

    def __init__(self, name, kind, taste, additives:list, filling=None):
        self.name = name
        if kind in Cake.known_types:
            self.kind = kind
        else:
            self.kind = 'other'
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        Cake.bakery_offer.append(self)

    def show_info(self):
        print(f'''| {self.name.upper():29}|
| Kind:    {self.kind:20}|
| Taste:   {self.taste:20}|''')
        if self.additives:
            print(f'| Additives:{"":19}|')
            for a in self.additives:
                print(f'|\t{a:23}|')
        if self.filling:
            print(f'| Filling: {self.filling:20}|')
        print(f'|{"-"*30}|')


    def set_filling(self, filling):
        self.filling = filling


    def add_additives(self, additives:list):
        self.additives.extend(additives)


cake1 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolate', 'nuts'], 'cream')
muffin1 = Cake('Chocolate Muffin', 'muffin', 'chocolate', ['chocolate'])
meringue1 = Cake('Super Sweet Meringue', 'meringue', 'very sweet')
cake04 = Cake('Cocoa waffle', 'waffle', 'cocoa', [], 'cocoa')
print(isinstance(cake1, Cake))
print(type(muffin1) == Cake)
print('='*100)
print(vars(cake1))
print('-'*100)
print(vars(Cake))
print('='*100)
print(dir(cake1))
print('-'*100)
print(dir(Cake))