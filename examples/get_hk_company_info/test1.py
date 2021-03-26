import pandas as pd
from eastmoney.company_info import hk_stock_basic, index_repo
from eastmoney.monitor import print_progress
import time, random

stock_tb1 = pd.read_excel("./全部港股代码.xlsx", sheet_name="港股主板", dtype={"股票代码": str})
stock_tb2 = pd.read_excel("./全部港股代码.xlsx", sheet_name="港股创业板")
stock_tb = pd.concat([stock_tb1, stock_tb2], axis=0)
panel_list_all = []
n = stock_tb.shape[0]
for i, name, code in zip(range(n), stock_tb['简称'], stock_tb['股票代码']):
    panel_list, success = hk_stock_basic(str(code))
    if success == 0:
        panel_list_all.append(panel_list)
        sleep_time = random.random() * 0.04 + 0.08
        time.sleep(sleep_time)
    else:
        print(code, success)
    print_progress(i, n)
panel_df = pd.DataFrame(data=panel_list_all,
                        columns=index_repo["company_info_basic_hk"])
panel_df.to_excel("HK-Stock-Results.xlsx", index=False)
