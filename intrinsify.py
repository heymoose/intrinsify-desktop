import pandas as pd
import os
import quandl
import time
import config


auth_tok = config.quandl_auth_token

data = quandl.get("WIKI/KO", authtoken = auth_tok)

print(data)