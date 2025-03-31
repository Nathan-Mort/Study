class Must_read:
    with open("data.csv", 'r') as data_file:
        lines  = [line.strip() for line in data_file.readlines()]
        print('\n'.join(lines))
        

if __name__ == '__main__':
    read_file = Must_read()