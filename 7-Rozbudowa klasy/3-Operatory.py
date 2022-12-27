class Cake:
    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling):

        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        Cake.bakery_offer.append(self)

    def __str__(self):
        additives = ", ".join(self.additives)
        return f'{self.kind} {self.name} with {additives}'

    def __iadd__(self, other):
        if isinstance(other, str):
            self.additives.append(other)
        elif isinstance(other, list) and all(isinstance(elem, str) for elem in other):
            self.additives.extend(other)
        else:
            raise Exception(f"Added element has to be type 'str' or 'list[str]'!")
        return self

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
        print('-' * 20)


cake01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolate', 'nuts'], 'cream')
print(cake01)
cake01 += 'text'
print(cake01)
cake01 += ['1', '2']
print(cake01)
