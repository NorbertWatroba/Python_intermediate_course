import random


def random_with_sum(number_of_values: int, asserted_sum: int):
    trial = 0
    numbers = list(range(number_of_values))
    while True:
        trial += 1
        for i in range(number_of_values):
            numbers[i] = random.randint(1, 100)
        if sum(numbers) == asserted_sum:
            yield trial, numbers
            trial = 0


for _ in range(10):
    generated_flavours = next(random_with_sum(3, 100))
    print(generated_flavours)
