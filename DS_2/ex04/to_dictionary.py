def to_dictionary():
    list_of_tuples = [
        ('Russia', '25'),
        ('France', '132'),
        ('Germany', '132'),
        ('Spain', '178'),
        ('Italy', '162'),
        ('Portugal', '17'),
        ('Finland', '3'),
        ('Hungary', '2'),
        ('The Netherlands', '28'),
        ('The USA', '610'),
        ('The United Kingdom', '95'),
        ('China', '83'),
        ('Iran', '76'),
        ('Turkey', '65'),
        ('Belgium', '34'),
        ('Canada', '28'),
        ('Switzerland', '26'),
        ('Brazil', '25'),
        ('Austria', '14'),
        ('Israel', '12')
        ]
    
    dictionary = dict()
    
    for country, num in list_of_tuples:
        if num not in dictionary:
            dictionary[num] = []  # Создаем список, если ключа еще нет
        dictionary[num].append(country)  # Добавляем страну в список значений
        
    print_dict(dictionary)    
        

def print_dict(dictionary):
    for num, countries in dictionary.items():
        for country in countries:
            print(f"'{num}' : '{country}'")
    
if __name__ == '__main__':
    to_dictionary()