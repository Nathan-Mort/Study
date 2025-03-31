import sys

def company_and_price(ticker):
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
    
    ticker = ticker.upper()
    
    if ticker in STOCKS:
        company_name = [name for name, symbol in COMPANIES.items() if symbol == ticker]
        if company_name:
            print(company_name[0], STOCKS[ticker])
        else:
            print('Unknown ticker')
    else:
        print('Unknown ticker')


def check_arg():
    if len(sys.argv) == 2:
        company_and_price(sys.argv[1])
        

if __name__ == '__main__':
    check_arg()