import timeit
from sys import argv


def get_list():
    emails = [
        "john@gmail.com",
        "james@gmail.com",
        "alice@yahoo.com",
        "anna@live.com",
        "philipp@gmail.com",
    ] * 5
    return emails


def loop_method():
    result = []
    emails = get_list()
    for email in emails:
        result.append(email)
    return result


def comprehension_method():
    emails = get_list()
    return [email for email in emails]


def identity_function(email):
    return email


def map_method():
    emails = get_list()
    return list(map(identity_function, emails))


def filter_method():
    emails = get_list()
    return list(filter(identity_function, emails))


def time_loop(num):
    loop_time = timeit.Timer(loop_method).timeit(number=num)
    return loop_time


def time_comprehension(num):
    comprehension_time = timeit.Timer(comprehension_method).timeit(number=num)
    return comprehension_time


def time_map(num):
    map_time = timeit.Timer(map_method).timeit(number=num)
    return map_time


def time_filter(num):
    filter_time = timeit.Timer(filter_method).timeit(number=num)
    return filter_time


def choose_method():
    if len(argv) == 3:
        method = argv[1]
        num = int(argv[2])
        if method == "loop":
            print(time_loop(num))
        elif method == "list_comprehension":
            print(time_comprehension(num))
        elif method == "map":
            print(time_map(num))
        elif method == "filter":
            print(time_filter(num))


if __name__ == "__main__":
    choose_method()
