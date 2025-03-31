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
            dictionary[num] = []
        dictionary[num].append(country) 
        
    return dictionary
        
def sort_dict(original_dict):
    k_sorted_dict = dict(sorted(original_dict.items(), key=lambda x: int(x[0]), reverse=True))
    return k_sorted_dict

    
def print_keys_dictionary(dictionary):
    for countries in dictionary.values():
        countries.sort()
        print(f"{'\n'.join(countries)}")
        
if __name__ == '__main__':
    print_keys_dictionary(sort_dict(to_dictionary()))