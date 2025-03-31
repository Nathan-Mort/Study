from sys import argv
import urllib3
from bs4 import BeautifulSoup
import cProfile
import pstats


http = urllib3.PoolManager()


def get_html(ticker):
    url = f"https://finance.yahoo.com/quote/{ticker.upper()}/financials/?p={ticker.lower()}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110"
    }

    response = http.request("GET", url, headers=headers)

    if response.status != 200:
        raise Exception(f"URL doesn't exist: {url}")

    return response.data.decode("utf-8")


def get_financial_data(html, field):
    soup = BeautifulSoup(html, "html.parser")
    tables = soup.find_all("div", class_="row lv-0 yf-t22klz")

    if not tables:
        raise Exception(f"data for '{field}' not found")

    result = None

    for table in tables:
        title = table.find("div", class_="rowTitle yf-t22klz")
        if title and title.get_text(strip=True) == field:
            values = tuple(
                column.get_text(strip=True)
                for column in table.find_all(
                    "div", class_=["column yf-t22klz alt", "column yf-t22klz"]
                )
            )
            result = (field,) + values

    if result is None:
        raise Exception(f"field '{field}' not found")

    return result


def cprofiler_inf():
    profiler = cProfile.Profile()
    profiler.enable()

    main()

    profiler.disable()

    with open("pstats-cumulative.txt", "w") as f:
        stats = pstats.Stats(profiler, stream=f)
        stats.sort_stats("cumulative")
        stats.print_stats(5)


def main():
    if len(argv) != 3:
        raise Exception("Incorrect input")

    ticker = argv[1]
    field = argv[2]

    try:
        html = get_html(ticker)
        result = get_financial_data(html, field)
        print(result)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    cprofiler_inf()
