import pandas as pd
import pandas_datareader.data as web
from datetime import datetime as dt

def getHistData(symbol): 
    df = web.DataReader(symbol, 'yahoo', '2016-01-01')
    return df

df_symbols = pd.read_csv("entity-symbols.csv")
                             
getHistData('msft')
