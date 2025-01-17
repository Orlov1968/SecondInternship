import data_download as dd
import data_plotting as dplt


def main():
    print("Добро пожаловать в инструмент получения и построения графиков биржевых данных.")
    print(
        "Вот несколько примеров биржевых тикеров, которые вы можете рассмотреть: AAPL (Apple Inc), GOOGL (Alphabet "
        "Inc), MSFT (Microsoft Corporation), AMZN (Amazon.com Inc), TSLA (Tesla Inc).")
    print(
        "Общие периоды времени для данных о запасах включают: 1д, 5д, 1мес, 3мес, 6мес, 1г, 2г, 5г, 10л, "
        "с начала года, макс.")

    ticker = input("Введите тикер акции (например, «AAPL» для Apple Inc):»")
    # period = input("Введите период для данных (например, '1mo' для одного месяца): ")
    first_day = input('Введите дату первого котировочного дня в формате YYYY-MM-DD: ')
    end_day = input('Введите дату последнего котировочного дня в формате YYYY-MM-DD: ')
    '''Создал словарь с нумерацией стилей'''
    style_dict = {
        '1': 'Solarize_Light2',
        '2': '_classic_test_patch',
        '3': '_mpl-gallery',
        '4': '_mpl-gallery-nogrid',
        '5': 'bmh',
        '6': 'classic',
        '7': 'dark_background',
        '8': 'fast',
        '9': 'fivethirtyeight',
        '10': 'ggplot',
        '11': 'grayscale',
        '12': 'seaborn-v0_8',
        '13': 'seaborn-v0_8-bright',
        '14': 'seaborn-v0_8-colorblind',
        '15': 'seaborn-v0_8-dark',
        '16': 'seaborn-v0_8-dark-palette',
        '17': 'seaborn-v0_8-darkgrid',
        '18': 'seaborn-v0_8-deep',
        '19': 'seaborn-v0_8-muted',
        '20': 'seaborn-v0_8-notebook',
        '21': 'seaborn-v0_8-paper',
        '22': 'seaborn-v0_8-pastel',
        '23': 'seaborn-v0_8-poster',
        '24': 'seaborn-v0_8-talk',
        '25': 'seaborn-v0_8-ticks',
        '26': 'seaborn-v0_8-white',
        '27': 'seaborn-v0_8-whitegrid',
        '28': 'tableau-colorblind10'
    }
    '''Распечатывается перечень стилей и их нумерация'''
    for key, value in style_dict.items():
        print(f"{key}: {value}")
    num_of_style = input("Введите номер выбранного стиля для графика: ")
    # Fetch stock data
    # stock_data = dd.fetch_stock_data(ticker, period)
    stock_data = dd.fetch_stock_data(ticker, first_day, end_day)
    # Add moving average to the data
    stock_data = dd.add_moving_average(stock_data)

    # Add RSI to the data
    stock_data = dd.rsi_calculate(stock_data)

    # Plot the data
    # dplt.create_and_save_plot(stock_data, ticker, period)
    dplt.create_and_save_plot(stock_data, ticker, f'{first_day} to {end_day}', style_dict[num_of_style])


if __name__ == "__main__":
    main()
