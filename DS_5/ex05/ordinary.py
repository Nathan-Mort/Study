import sys
import resource


def read(file):
    with open(file, "r") as f:
        data = [f.readlines()]
    return data


if __name__ == "__main__":
    file = sys.argv[1]
    data = read(file)
    for line in data:
        pass

    usage = resource.getrusage(resource.RUSAGE_SELF)
    peak_memory = usage.ru_maxrss / (1024**2)
    user_system_time = usage.ru_utime + usage.ru_stime

    print(f"Peak Memory Usage = {peak_memory:.3f} GB")
    print(f"User Mode Time + System Mode Time = {user_system_time:.2f}s")
