import sys

def send_letter(email):
    with open('employees.tsv', 'r') as tsv_file:
        for line in tsv_file:
            email_column = line.strip().split('\t')[-1]
            if email in email_column:
                name  = email.strip().split('@')[0].split('.')[0]
                print(f"Dear {name.capitalize()}, welcome to our team. We are sure that it will be a pleasure to work with you. That’s a precondition for the professionals that our company hires.")
                break
            
if __name__ == '__main__':
    if len(sys.argv) == 2:
        send_letter(sys.argv[1])
    else:
        print("Uncorrect input")