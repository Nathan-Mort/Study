import sys

def companies():
    COMPANIES = {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX',
        'Tesla': 'TSLA',
        'Nokia': 'NOK'
        }
    return COMPANIES

def stocks():
    STOCKS = {
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37
        }
    return STOCKS

def pars_string(string):
    return [part.strip() for part in string.strip().split(',')]  # yдаляем лишние пробелы для каждого элемента, получается список


def is_correct_arg(parts):
    is_correct = True
    if any(len(part) == 0 for part in parts):
        is_correct = not is_correct
    return is_correct

def get_price(part):
    companies_dict = companies()
    stocks_dict = stocks()
    symbol = companies_dict.get(part.capitalize())
    
    if symbol and symbol in stocks_dict:
        price = stocks_dict[symbol]
    else:
        price = None
    return price

def get_company(part):
    companies_dict = companies()
    stocks_dict = stocks()
    if part.upper() in stocks_dict:
        company_name = [name for name, symbol in companies_dict.items() if symbol == part.upper()]
        if company_name:
            company = company_name[0]
        else:
            company = None
    else:
        company = None
    return company
    
    
def print_all(parts):
    for part in parts:
        price = get_price(part)
        company_name = get_company(part)
        if price is not None:
            print(f"{part.capitalize()} stock price is {price}")
        elif company_name is not None:
            print(f"{part.upper()} is a ticker symbol for {company_name}")
        else:
            print(f"{part} is an unknown company or an unknown ticker symbol")

def main_func():
    if len(sys.argv) == 2:
        parts = pars_string(sys.argv[1])
        if is_correct_arg(parts):
            print_all(parts)

if __name__ == '__main__':
    main_func()