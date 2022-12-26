from decimal import Decimal as D
argument_list = []
i = D('0')
while i < 10:
    argument_list.append(i)
    i += D('0.1')

formula = input('Podaj wzór z x:\t')

for x in argument_list:
    print(f'{x:>3} - {eval(formula)}')
