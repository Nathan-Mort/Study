import sys

def set_clients():
    clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com',
               'john@snow.is', 'bill_gates@live.com', 'mark@facebook.com',
               'elon@paypal.com', 'jessica@gmail.com']
    return set(clients)

def set_participants():
    participants = ['walter@heisenberg.com', 'vasily@mail.ru',
                    'pinkman@yo.org', 'jessica@gmail.com', 'elon@paypal.com',
                    'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']
    return set(participants)

def set_recipients():
    recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']
    return set(recipients)

def call_center():
    to_call = set_clients() - set_recipients()
    print(f"[{', '.join(to_call)}]")
    
def potential_clients():
    potent = set_participants() - set_clients()
    print(f"[{', '.join(potent)}]")
    
def loly_program():
    loly = set_clients() - set_participants()
    print(f"[{', '.join(loly)}]")
    
def what_business_task():
    if len(sys.argv) == 2:
        if sys.argv[1] == 'call_center':
            call_center()
        elif sys.argv[1] == 'potential_clients':
            potential_clients()
        elif sys.argv[1] == 'loly_program':
            loly_program()
        else:
            print('Unkonwn business task')
    else:
        print('Uncorrect number of arguments')
    
if __name__ == '__main__':
    what_business_task()