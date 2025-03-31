def data_types():
    int_var = 123
    str_var = 'Hello'
    float_var = 123.123
    bool_var = True
    list_var = [123, 1.2, 'python', [1, 2, 3]] # изменяемый упорядоченный набор элементов
    tuple_var = (1, 2.4, 'd', (1, 2, 3), [1, 'a'])  # неизменяемые упорядоченные коллекции элементов (кортежи)
    dict_var = {'School21' : 'ptp',
                'Python' : 'Snake'} # ассоциативный массив, пары «ключ-значение», где каждый ключ является уникальным 
    set_var = {1, 2.3, 'f', (1, 3)} # изменяемый набор уникальных и неупорядоченных элементов
    
    types = [type(var).__name__ for var in 
             [int_var, str_var, float_var, bool_var, list_var, dict_var, tuple_var, set_var]]
    print('[', ', '.join(types), ']', sep = '')

if __name__ == '__main__':
    data_types()