import data_download as dd
import data_plotting as dplt


def main():
    print("Добро пожаловать в инструмент получения и построения графиков биржевых данных.")
    print(
        "Вот несколько примеров биржевых тикеров, которые вы можете рассмотреть: AAPL (Apple Inc), GOOGL (Alphabet Inc), MSFT (Microsoft Corporation), AMZN (Amazon.com Inc), TSLA (Tesla Inc).")
    print(
        "Общие периоды времени для данных о запасах включают: 1д, 5д, 1мес, 3мес, 6мес, 1г, 2г, 5г, 10л, с начала года, макс.")

    ticker = input("Введите тикер акции (например, «AAPL» для Apple Inc):»")
    # period = input("Введите период для данных (например, '1mo' для одного месяца): ")
    first_day = input('Введите дату первого котировочного дня в формате YYYY-MM-DD: ')
    end_day = input('Введите дату последнего котировочного дня в формате YYYY-MM-DD: ')
    # Fetch stock data
    # stock_data = dd.fetch_stock_data(ticker, period)
    stock_data = dd.fetch_stock_data(ticker, first_day, end_day)
    # Add moving average to the data
    stock_data = dd.add_moving_average(stock_data)

    # Add RSI to the data
    stock_data = dd.rsi_calculate(stock_data)

    # Plot the data
    # dplt.create_and_save_plot(stock_data, ticker, period)
    dplt.create_and_save_plot(stock_data, ticker, f'{first_day} to {end_day}')


if __name__ == "__main__":
    main()
