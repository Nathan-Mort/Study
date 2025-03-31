class Research:
    def file_reader(self):
        with open("data.csv", 'r') as data_file:
            lines  = [line.strip() for line in data_file.readlines()]
            return lines
        
def print_file():
    file = Research()
    file_contents = file.file_reader()
    for line in file_contents:
        print(line)
        
if __name__ == '__main__':
    print_file()