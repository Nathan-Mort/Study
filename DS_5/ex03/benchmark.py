from functools import reduce
import timeit
from sys import argv


def loop_sum(num):
    result = 0
    for i in range(1, num + 1):
        result += i * i
    return result

def reduce_sum(num):
    return reduce(lambda res, x: res + x * x, range(1, num + 1), 0)

def time_loop(num, num_iter):
    loop_time = timeit.Timer(lambda: loop_sum(num_iter)).timeit(number=num)
    return loop_time

def time_reduce(num, num_iter):
    reduce_time = timeit.Timer(lambda: reduce_sum(num_iter)).timeit(number=num)
    return reduce_time

def choose_method():
    if len(argv) == 4:
        method = argv[1]
        num_calls = int(argv[2])
        num_iter = int(argv[3])
        if method == "loop":
            print(time_loop(num_calls, num_iter))
        elif method == "reduce":
            print(time_reduce(num_calls, num_iter))


if __name__ == "__main__":
    choose_method()
