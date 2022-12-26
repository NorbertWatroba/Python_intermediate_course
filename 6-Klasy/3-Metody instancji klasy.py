class Cake:
    def __init__(self, name, kind, taste, additives:list=[], filling=None):
        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling

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

bakery_offer = [cake1, muffin1, meringue1]
bakery_offer[1].set_filling("vanilla cream")
# bakery_offer[2].add_additives(["coca powder", "coconuts"])
print("Today in our offer:")
for i in bakery_offer:
    i.show_info()
