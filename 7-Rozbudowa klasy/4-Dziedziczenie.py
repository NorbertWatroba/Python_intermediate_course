class Cake:
    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling):

        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.bakery_offer.append(self)

    def show_info(self):
        print("{}".format(self.name.upper()))
        print("Kind:        {}".format(self.kind))
        print("Taste:       {}".format(self.taste))
        if len(self.additives) > 0:
            print("Additives:")
            for a in self.additives:
                print("\t\t{}".format(a))
        if len(self.filling) > 0:
            print("Filling:     {}".format(self.filling))
        if __class__.__name__ == Cake:
            print('-' * 20)

    @property
    def full_name(self):
        return "--== {} - {} ==--".format(self.name.upper(), self.kind)


class SpecialCake(Cake):
    def __init__(self, name, kind, taste, additives, filling, occasion, shape, ornaments, text):
        super().__init__(name, kind, taste, additives, filling)
        self.occasion = occasion
        self.shape = shape
        self.ornaments = ornaments
        self.text = text

    def show_info(self):
        super().show_info()
        print(f'Occasion:    {self.occasion}')
        print(f'Shape:       {self.shape}')
        print(f'Ornaments:   {self.ornaments}')
        print(f'Text:        {self.text}')
        print('-' * 20)


birthday = SpecialCake('Birthday Cake', 'cake', 'sweet', [], 'cream', 'birthday',
                       'rectangular', 'hearts', 'Happy Birthday!')
wedding = SpecialCake('Wedding Cake', 'cake', 'sweet-sour', ['blueberries'], 'cream', 'wedding',
                      'circular', 'rings', 'Happy Marriage!')
birthday.show_info()
wedding.show_info()

for item in SpecialCake.bakery_offer:
    print(item.full_name)
    item.show_info()
