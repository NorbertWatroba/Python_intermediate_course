import time


class Combinations:
    def __init__(self, products: list, promotions: list, customers: list):
        self.products = products
        self.promotions = promotions
        self.customers = customers

        self.current_product = 0
        self.current_promotion = 0
        self.current_customer = 0

    def __next__(self):
        if self.current_customer >= len(self.customers):
            self.current_customer = 0
            self.current_promotion += 1

        if self.current_promotion >= len(self.promotions):
            self.current_promotion = 0
            self.current_product += 1

        if self.current_product >= len(self.products):
            raise StopIteration()

        item_to_return = f'{self.customers[self.current_customer]} - {self.promotions[self.current_promotion]} - {self.products[self.current_product]}'
        self.current_customer += 1
        return item_to_return

    def __iter__(self):
        return self


products = ["Product {}".format(i) for i in range(1, 500)]

promotions = ["Promotion {}".format(i) for i in range(1, 50)]

customers = ['Customer {}'.format(i) for i in range(1, 500)]

'''
combinations = []

for i in products:
    for j in promotions:
        for k in customers:
            combinations.append("{} - {} - {}".format(i, j, k))
'''

combinations = Combinations(products, promotions, customers)

for c in combinations:
    # here an analysis will be done - currently, just nothing happens :)
    pass

time.sleep(10)
