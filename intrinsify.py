import pandas as pd
import os
import quandl
import time
import config


api_key = config.quandl_api_key

data = quandl.get("WIKI/KO", api_key = api_key)

print(data)