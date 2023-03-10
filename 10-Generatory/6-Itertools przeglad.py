import itertools as it


def get_factors(x):
    ret_list = []
    for i in range(1, x):
        if x % i == 0:
            ret_list.append(i)
    return ret_list


print(get_factors(20))

candidate_list = [x for x in range(10000)]
filtered_list = it.filterfalse(lambda x: sum(get_factors(x)) != x, candidate_list)
for number in filtered_list:
    print(number, get_factors(number))


# ========================================================================================


def check_if_has_dividers(x):
    for i in range(2, x):
        if x % i == 0:
            return True
    else:
        return False


prime_numbers = list(it.filterfalse(lambda x: check_if_has_dividers(x), range(1, 10000)))
print(prime_numbers)
print(prime_numbers[:10])

prime_numbers = it.islice(it.filterfalse(lambda x: check_if_has_dividers(x), range(1, 10000000)), 10)
print(list(prime_numbers))
