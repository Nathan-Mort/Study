import sys

def to_tsv_file(orig_file):
    with open(orig_file, 'r') as email_file:
        emails = email_file.readlines()
        with open('employees.tsv', 'w') as tsv_file:
            tsv_file.write('Name\tSurname\tE-mail\n')
            for email in emails:
                name, surname = email.strip().split('@')[0].split('.')
                tsv_file.write(f"{name.capitalize()}\t{surname.capitalize()}\t{email}")

if __name__ == '__main__':
    if len(sys.argv) == 2:
        to_tsv_file(sys.argv[1])
    else:
        print("Uncorrect input")