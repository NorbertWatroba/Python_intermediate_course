import itertools as it
from math import factorial

notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']

for combination in it.permutations(notes, 4):
    print(combination)

count = factorial(len(notes)) / factorial((len(notes)-4))
print(f'{count} opcji')
print('='*25)

for combination in it.product(notes, repeat=4):
    print(combination)

count = pow(len(notes), 4)
print(f'{count} opcji')
