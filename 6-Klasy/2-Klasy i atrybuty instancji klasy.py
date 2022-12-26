class Cake:
    def __init__(self, name, kind, taste, additives=None, filling='nothing'):
        self.name = name
        self.kind = kind
        self.taste = taste
        if additives is None:
            self.additives = []
        else:
            self.additives = additives
        self.filling = filling

cake1 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolate', 'nuts'], 'cream')
muffin1 = Cake('Chocolate Muffin', 'muffin', 'chocolate', 'chocolate')
meringue1 = Cake('Super Sweet Meringue', 'meringue', 'very sweet')

bakery_offer = [cake1, muffin1, meringue1]
for i in bakery_offer:
    print(f'{i.name} - {i.kind} main taste: {i.taste} with additives of {i.additives}, filled with {i.filling}')