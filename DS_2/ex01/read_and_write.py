def csv_to_tsv(line):
    in_quotes = False 
    tsv_line = []
    current_field = []
    
    for char in line:
        if char == '"':
            in_quotes = not in_quotes               # меняем на противоположное(в кавычках/не в кавычках)
        elif char == ',' and not in_quotes:         # если мы не в кавычках
            tsv_line.append(''.join(current_field)) # преобразуем в строку и добавляем в список tsv_line
            current_field = []
        else:
            current_field.append(char) 
            
    tsv_line.append(''.join(current_field))
    return '\t'.join(tsv_line)   # с помощью .join()  список преобразуем в строку с разделителями табуляциями

def file_replace():
    csv_file = open("ds.csv", "r")
    tsv_file = open("ds.tsv", "w")
    for csv_line in csv_file:
        tsv_line = csv_to_tsv(csv_line.strip())
        tsv_file.write(tsv_line + '\n')
    csv_file.close()
    tsv_file.close()
     
        
if __name__ == '__main__':
    file_replace()