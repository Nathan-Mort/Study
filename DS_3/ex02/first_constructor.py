from sys import argv
import os

class Research:
    def __init__(self, file_path):
        self.file_path = file_path
    
    def file_reader(self):
        
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"Файл '{self.file_path}' не найден.")
        
        with open(self.file_path, 'r') as data_file:
            lines  = [line.strip() for line in data_file.readlines()]
            if len(lines) < 2:
                raise ValueError("Неверное количество строк")
            
            header = lines[0]. split(',')
            if len(header) != 2:
                raise ValueError("Неверное количество заголовков")
            
            for line in lines[1:]:
                values = line.split(',')
                if len(values) != 2 or not all(value in ['0', '1'] for value in values):
                    raise ValueError("Неверное содержание строк")
                
        return lines
        
def print_file():
    file_path = argv[1]
    research_file = Research(file_path)
    file_contents = research_file.file_reader()
    for line in file_contents:
        print(line)
        
if __name__ == '__main__':
    print_file()