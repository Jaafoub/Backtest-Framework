import pandas as pd
import numpy as np
from yahoo_data import *

def compute_daily_return( df ):
    ret = df / df.shift( 1 ) -1
    return( ret )
def compute_daily_return_yahoo( ticker, start_date, end_date ):
    data =  yahoo_stock_data_ticker( ticker, start_date, end_date )
    close = data['Close']
    return( compute_daily_return( close ) )

def compute_annualized_volatility_yahoo( ticker, start_date, end_date, window_in_years = 1 ):
    ret = compute_daily_return_yahoo( ticker, start_date, end_date )
    return( compute_annualized_vol( ret, window_in_years ) )

def compute_annualized_vol(ret, window_in_years):
    N = window_in_years * 252
    vol = ret.rolling( N ).std()
    annualized_vol = np.sqrt( 252 ) * vol
    return( annualized_vol )
