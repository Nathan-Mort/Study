import sys

def get_price(name_company):
    COMPANIES = {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX',
        'Tesla': 'TSLA',
        'Nokia': 'NOK'
        }

    STOCKS = {
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37
        }
    
    name_company = name_company.capitalize() # делает первый символ заглавным остальные строчными
    
    if name_company in COMPANIES:
        print(STOCKS[COMPANIES[name_company]])
    else:
        print('Unknown company')
            
            
            
def check_arg():
    if len(sys.argv) == 2:
        get_price(sys.argv[1])
        

if __name__ == '__main__':
    check_arg()