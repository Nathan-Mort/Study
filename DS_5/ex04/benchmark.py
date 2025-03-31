import timeit
import random
from collections import Counter


def generation_list():
    return [random.randint(0, 100) for _ in range(100000)]


def counter_to_dictionary(gen_list):
    
    count_dict = Counter(gen_list)
    return count_dict


def counter_most_common_numbers(gen_list):
    
    counter = Counter(gen_list)
    most_common = counter.most_common(10)
    return most_common


def my_func_to_dictionary(gen_list):
    
    count_dict = {}

    for item in gen_list:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1

    return count_dict


def my_func_most_common_numbers(gen_list):
    
    count_dict = my_func_to_dictionary(gen_list)

    sorted_count_dict = sorted(
        count_dict.items(), key=lambda item: item[1], reverse=True
    )

    most_common = [(key, value) for (key, value) in sorted_count_dict[:10]]

    return most_common


def func_time(gen_list):

    time_my_func = timeit.Timer(lambda: my_func_to_dictionary(gen_list)).timeit(
        number=1
    )
    time_counter = timeit.Timer(lambda: counter_to_dictionary(gen_list)).timeit(
        number=1
    )
    time_my_top = timeit.Timer(lambda: my_func_most_common_numbers(gen_list)).timeit(
        number=1
    )
    time_counter_top = timeit.Timer(
        lambda: counter_most_common_numbers(gen_list)
    ).timeit(number=1)

    print(f"my function: {time_my_func}\nCounter: {time_counter}")
    print(f"my top: {time_my_top}\nCounter: {time_counter_top}")


def main():
    gen_list = generation_list()
    func_time(gen_list)


if __name__ == "__main__":
    main()
