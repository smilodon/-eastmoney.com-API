import pandas as pd
from eastmoney.company_info import us_stock_basic, index_repo
import time, random

stock_tb = pd.read_excel("./data/全部美股代码.xlsx")
panel_list_all = []
for name, code in zip(stock_tb['股票名称'], str(stock_tb['代码2'])):
    panel_list, success = us_stock_basic(code)
    if success == 0:
        panel_list_all.append(panel_list)
        sleep_time = random.random() * 0.04 + 0.08
        time.sleep(sleep_time)
    else:
        print(code, success)
panel_df = pd.DataFrame(data=panel_list_all,
                        columns=index_repo["company_info_basic_us"])
panel_df.to_excel("./results/US-Stock-Results.xlsx", index=False)
