import functools
from time import time, sleep

@functools.lru_cache(100)
def fib(n):
    sleep(0.1)
    if n < 2:
        result = n
    else:
        result = fib(n - 1) + fib(n - 2)

    return result

start = time()
print(f'fib: {fib(35)}')
end = time()
print(f'time: {end - start}')
print(fib.cache_info())

print('-'*60)
start = time()
print(f'fib: {fib(36)}')
end = time()
print(f'time: {end - start}')
print(fib.cache_info())
