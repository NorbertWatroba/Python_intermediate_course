def combinations(products, promotions, customers):
    for product in products:
        for promotion in promotions:
            for customer in customers:
                yield f'{product} - {promotion} - {customer}'


products = ["Product {}".format(i) for i in range(1, 4)]
promotions = ["Promotion {}".format(i) for i in range(1, 2)]
customers = ['Customer {}'.format(i) for i in range(1, 5)]


for c in combinations(products, promotions, customers):
    print(c)
