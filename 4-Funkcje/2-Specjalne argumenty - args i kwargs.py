# Zadanie 1
def calculate_paint(efficiency_ltr_per_m2, *args):
    total_area = sum(args)
    print(f'You need {total_area * efficiency_ltr_per_m2}l')


calculate_paint(2, 25, 25, 25, 25)
rooms_to_paint = [40, 20, 30, 10]
calculate_paint(2, *rooms_to_paint)


# Zadanie 2
def log_it(*args):
    with open(r'.\log_it.txt', 'a') as file:
        for text in args:
            file.write(text)
            file.write(' ')
        file.write('\n')


log_it('Starting processing forecasting')
log_it('ERROR', 'Not enough data', 'invoices', '2020')
