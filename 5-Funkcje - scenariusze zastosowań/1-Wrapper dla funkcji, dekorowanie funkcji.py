import time


def create_time_wrapper(func):
    def wrapper_time(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'Funkcja {func.__name__} wykonana w czasie {end - start}')
        return result
    return wrapper_time


def get_sequence(n):
    if n <= 0:
        return 1
    else:
        v = 0
        for i in range(n):
            v += 1 + (get_sequence(i - 1) + get_sequence(i)) / 2
        return v


if __name__ == '__main__':
    wrapped = create_time_wrapper(get_sequence)
    wrapped(18)

