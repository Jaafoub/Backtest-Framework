import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def compute_annualized_pnl( position, daily_return ):
    index = position.index
    start_date = min(index)
    end_date =  max(index)
    dates = pd.DataFrame( index = pd.date_range(start=start_date,end=end_date,freq = 'D') )
    merged = pd.merge(dates, position, how='left',left_index=True, right_index=True )
    merged.fillna(method='ffill', inplace=True)
    pnl = pd.merge(daily_return, merged, how='left',left_index=True,right_index=True)


