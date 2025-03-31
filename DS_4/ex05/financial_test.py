from sys import argv
import requests
from bs4 import BeautifulSoup
import pytest
from unittest.mock import Mock


def get_html(ticker):

    url = f"https://finance.yahoo.com/quote/{ticker.upper()}/financials/?p={ticker.lower()}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110"
    }
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception(f"URL doesn't exist: {url}")

    return response


def get_financial_data(response, field):
    soup = BeautifulSoup(response.text, "html.parser")
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


def main():
    if len(argv) != 3:
        raise Exception("Incorrect input")

    ticker = argv[1]
    field = argv[2]

    try:
        response = get_html(ticker)
        result = get_financial_data(response, field)
        print(result)
    except Exception as e:
        print(e)


def test_get_successful_html(mocker):
    # успешный запрос
    mock_response_success = Mock()
    mock_response_success.status_code = 200
    mock_response_success.text = "<html>Success</html>"

    mocker.patch("requests.get", return_value=mock_response_success)

    response = get_html("AAPL")
    assert response.status_code == 200
    assert response.text == "<html>Success</html>"


def test_get_exist_html(mocker):
    # ошибочный запрос
    mock_response_404 = Mock()
    mock_response_404.status_code = 404

    mocker.patch("requests.get", return_value=mock_response_404)

    with pytest.raises(Exception, match="URL doesn't exist"):
        get_html("INVALID_TICKER")


def test_get_financial_data_returns_tuple(mocker):

    mock_response = Mock()
    mock_response.text = """
    <div class="row lv-0 yf-t22klz">
        <div class="rowTitle yf-t22klz">Total Revenue</div>
        <div class="column yf-t22klz">2021</div>
        <div class="column yf-t22klz">5000</div>
    </div>
    """

    result = get_financial_data(mock_response, "Total Revenue")
    assert isinstance(result, tuple), "Возвращаемый тип должен быть кортежем"


def test_get_financial_data_returns_values(mocker):

    mock_response = Mock()
    mock_response.text = """
    <div class="row lv-0 yf-t22klz">
        <div class="rowTitle yf-t22klz">Total Revenue</div>
        <div class="column yf-t22klz">2021</div>
        <div class="column yf-t22klz">5000</div>
    </div>
    """

    expected_result = ("Total Revenue", "2021", "5000")

    result = get_financial_data(mock_response, "Total Revenue")

    assert (
        result == expected_result
    ), f"Ожидалось {expected_result}, но получено {result}"


def test_get_financial_data_no_tables():

    mock_response = Mock()
    mock_response.text = "<html>No tables here</html>"

    with pytest.raises(Exception, match="data for 'Total Revenue' not found"):
        get_financial_data(mock_response, "Total Revenue")


def test_get_financial_data_field_not_found():

    mock_response = Mock()
    mock_response.text = """
    <div class="row lv-0 yf-t22klz">
        <div class="rowTitle yf-t22klz">Other Field</div>
        <div class="column yf-t22klz">2021</div>
        <div class="column yf-t22klz">5000</div>
    </div>
    """
    with pytest.raises(Exception, match="field 'Total Revenue' not found"):
        get_financial_data(mock_response, "Total Revenue")


if __name__ == "__main__":
    main()
