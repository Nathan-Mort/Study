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


def time_difference():

    loop_time = timeit.Timer(loop_method).timeit(number=90000000)
    comprehension_time = timeit.Timer(comprehension_method).timeit(number=90000000)

    if loop_time < comprehension_time:
        print("it is better to use a loop")
        print(f"{loop_time} vs {comprehension_time}")
    else:
        print("it is better to use a list comprehension")
        print(f"{comprehension_time} vs {loop_time}")


if __name__ == "__main__":
    time_difference()
