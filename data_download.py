import delta
import yfinance as yf


def fetch_stock_data(ticker, period='1mo'):
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    return data


def add_moving_average(data, window_size=5):
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data


def calculate_and_display_average_price(data):
    average_price = data['Close'].meane()
    print(average_price)


def notify_if_strong_fluctuations(data, threshold):
    """Функция принимает значения котировок акций за указанный период и допустимый
    порог колебания стоимости акций за этот же период. Выполняется вычисление разницы
    между максимальным и минимальным значением стоимости акций за период.
     Если разница превысила указанный порог, пользователь получает об этом информацию"""
    maximum_value_of_promotion = data['Close'].max()
    minimum_value_of_promotion = data['Close'].min()
    threshold_for_promotion = maximum_value_of_promotion - minimum_value_of_promotion
    if threshold_for_promotion >= threshold:
        print(f'Колебания акций за указанный период превысили установленный порог в {threshold} пунктов')
    # return
    else:
        print(f'Колебания акций за период не превысили заданный диапазон')


def export_data_to_csv(data, filename):
    """Функция принимает Data Frame и имя файла, в который будем сохранять значения котировок.
    Затем переносим значения котировок из Data Frame в указанный файл, в качестве
    разделителя используем ",", индекс включён (если не будем включать индекс, ставим False)."""
    data.to_csv(filename, sep=',', index=True, encoding='utf-8')
    return filename


def rsi_calculate(data, period = 14):
    diff_axis = data['Close'].diff()
    upemane = (diff_axis.where(diff_axis > 0, 0)).rolling(window=period).mean()
    downmane = (-diff_axis.where(diff_axis < 0, 0)).rolling(window=period).mean()
    rs = upemane/downmane
    rsi = 100 - (100/(1 + rs))
    return rsi
