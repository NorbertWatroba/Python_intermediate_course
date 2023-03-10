class NoDuplicates:
    def __init__(self):
        self.lista = []

    def __call__(self, new_items: list):
        for item in new_items:
            if item not in self.lista:
                self.lista.append(item)

    def __str__(self):
        return str(self.lista)


my_no_dup_list = NoDuplicates()
print(my_no_dup_list)
my_no_dup_list(['keyboard', 'mouse'])
print(my_no_dup_list)
my_no_dup_list(['keyboard', 'mouse', 'pendrive'])
print(my_no_dup_list)
my_no_dup_list(['charger', 'pendrive'])
print(my_no_dup_list)
