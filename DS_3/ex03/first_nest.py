from sys import argv
import os


class Research:

    def __init__(self, file_path):
        self.file_path = file_path

    def file_reader(self, has_header=True):

        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"Файл '{self.file_path}' не найден.")

        with open(self.file_path, "r") as data_file:
            lines = [line.strip() for line in data_file.readlines()]
            if len(lines) < 2:
                raise ValueError("Неверное количество строк")

            if has_header:
                header = lines[0].split(",")
                if len(header) != 2:
                    raise ValueError("Неверное количество заголовков")
                data_lines = lines[1:]
            else:
                data_lines = lines

            data_list = []
            for line in data_lines[1:]:
                values = line.split(",")
                if len(values) != 2 or not all(value in ["0", "1"] for value in values):
                    raise ValueError("Неверное содержание строк")
                data_list.append([int(value) for value in values])

        return data_list

    class Calculations:

        def counts(self, data_list):
            heads = sum(row[0] for row in data_list)
            tails = sum(row[1] for row in data_list)
            return heads, tails

        def fractions(self, heads, tails):
            total = heads + tails
            if total != 0:
                head_fraction = (heads / total) * 100
                tail_fraction = (tails / total) * 100
            return head_fraction, tail_fraction


def print_all():

    file_path = argv[1]
    research_file = Research(file_path)
    file_contents = research_file.file_reader()
    print(file_contents)

    calculations = Research.Calculations()
    heads, tails = calculations.counts(file_contents)
    print(heads, tails)

    head_fraction, tail_fraction = calculations.fractions(heads, tails)
    print(head_fraction, tail_fraction)


if __name__ == "__main__":
    print_all()
