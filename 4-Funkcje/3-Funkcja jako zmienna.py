def double(x):
    return 2 * x


def square(x):
    return x ** 2


def negative(x):
    return -x


def div2(x):
    return x / 2


number = 8
transformations = [double, square, div2, negative]
transformations2 = [square, square, div2, double]
tmp_return_value = number

for transformation in transformations2:
    tmp_return_value = transformation(tmp_return_value)
    print(tmp_return_value)
