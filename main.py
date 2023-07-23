from modules.helpers.index import stockData

def main():
    symbol = 'AAPL'

    stock_price = stockData.get_stock_price(symbol)
    pe_ratio = stockData.get_pe_ratio(symbol)

    print(f'{symbol} stock price: {stock_price}')
    print(f'{symbol} P/E ratio: {pe_ratio}')

if __name__ == '__main__':
    main()
