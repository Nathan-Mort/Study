import timeit


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


def time_difference():

    loop_time = timeit.Timer(loop_method).timeit(number=90000000)
    comprehension_time = timeit.Timer(comprehension_method).timeit(number=90000000)
    map_time = timeit.Timer(map_method).timeit(number=90000000)

    sorted_times = sorted([loop_time, comprehension_time, map_time])

    print(
        "it is better to use a map"
        if sorted_times[0] == "map"
        else (
            "it is better to use a loop"
            if sorted_times[0] == "loop"
            else "it is better to use a list comprehension"
        )
    )
    print(" vs ".join([str(time) for time in sorted_times]))


if __name__ == "__main__":
    time_difference()
