import pandas as pd
import yfinance as yf
import yahoo_fin.stock_info as yahooApi

class StockData:
    @staticmethod
    def fetch_stock_data(symbol):
        stock_data = yf.Ticker(symbol)
        return stock_data.history(period='1y')

    @staticmethod
    def get_stock_price(symbol):
        data = StockData.fetch_stock_data(symbol)
        if not data.empty:
            return data['Close'].iloc[-1]
        else:
            return None

    @staticmethod  
    def get_pe_ratio(symbol):
        quote_table = yahooApi.get_quote_table(symbol)
                # Convert the dictionary to a DataFrame and transpose it
        quote_table = pd.DataFrame(quote_table).T
        pe_ratio = quote_table.loc["PE Ratio (TTM)"]
        return pe_ratio
