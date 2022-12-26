import math
import time
formulas_list = [
    'abs(x**3 - x**0.5)',
    'abs(math.sin(x) * x**2)',
]
argument_list = []
for i in range(10000):
    argument_list.append(i / 10)

results_list = []
for formula in formulas_list:
    print(f'We are working on {formula} formula '.center(200, '-'))
    start = time.time()
    for x in argument_list:
        results_list.append(eval(formula))

    print(f'min value: {min(results_list)}\t max value: {max(results_list)}')
    stop = time.time()
    print(f'loop duration time: {stop - start}')
    results_list.clear()
print('='*200)
for formula in formulas_list:
    compiled_formula = compile(formula, '', mode='eval')
    print(f'We are working on a compiled {formula} formula '.center(200, '-'))
    start = time.time()
    for x in argument_list:
        results_list.append(eval(compiled_formula))

    print(f'min value: {min(results_list)}\t max value: {max(results_list)}')
    stop = time.time()
    print(f'loop duration time: {stop - start}')
