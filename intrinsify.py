import sys
import pandas as pd
import datetime as dt
from iexfinance import Stock
from iexfinance import get_historical_data
from iexfinance import get_market_tops
from iexfinance import get_stats_intraday

def float_to_currency_string(num):
    return '${:,.2f}'.format(float(num))

def float_to_percentage_string(num):
    return '{:.2f}%'.format(float(num))

def format_result_string(*args):
    return '  |  '.join(args)

default_ticker = 'KO'

if len(sys.argv) == 1:
    print(f"No ticker passed in as an arguement, default to {default_ticker}")
    ticker = default_ticker
else:
    ticker = sys.argv[1]

stock = Stock(ticker, output_format='pandas')

stock_name = stock.get_company_name()['companyName'].to_string()
stock_price = stock.get_price()['price'][ticker]
stock_eps = stock.get_key_stats()[ticker]['latestEPS']
flat_growth_estimate = 5
aaa_corporate_bond_yield = 3.56
stock_intrinsic_value = (stock_eps * (8.5 + (2 * flat_growth_estimate)) * 4.4) / aaa_corporate_bond_yield
norm_stock_intrinsic_value = stock_intrinsic_value / stock_price

print(format_result_string(stock_name,
                           ticker.upper(),
                           float_to_currency_string(stock_price),
                           float_to_percentage_string(flat_growth_estimate),
                           float_to_percentage_string(aaa_corporate_bond_yield),
                           float_to_currency_string(stock_eps),
                           float_to_currency_string(stock_intrinsic_value),
                           '{:.2f}'.format(norm_stock_intrinsic_value)))