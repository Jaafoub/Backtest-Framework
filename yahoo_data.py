import pandas as pd
import pandas_datareader.data as web
import datetime as dt

def yahoo_stock_data_ticker( ticker, start_date, end_date ):
    return( web.DataReader(ticker, 'yahoo',start_date,end_date ) )

def yahoo_stock_data_tickers( tickers, start_date, end_date ):
    all_data = {}
    for i in tickers:
        all_data[ticker] = yahoo_stock_data_ticker( ticker, start_date, end_date )
    return( all_data )

def save_yahoo_data_tickers( tickers, start_date, end_date, path = '/Users/OUBAITA/Desktop/temp/' ):
    for ticker in tickers:
        save_yahoo_data_ticker( ticker, start_date,end_date, path = path )

def save_yahoo_data_ticker( ticker, start_date, end_date, path = '/Users/OUBAITA/Desktop/temp/'):
    full_path = '{}{}.csv'.format(path,ticker)
    df = yahoo_stock_data( ticker, start_date, end_date )
    df.to_csv( full_path )




