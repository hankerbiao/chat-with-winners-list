import os.path

import akshare as ak
from datetime import datetime

start_date = "20200101"
data_path = "data"

today = datetime.today().strftime('%Y%m%d')
file_name_stock = f"{start_date}-{today}-股票.csv"  # 股票信息
file_name_securities_sales_department = f"{start_date}-{today}-营业部.csv"  # 证券营业部信息

os.makedirs(os.path.join(data_path, today), exist_ok=True)
stock_sava_path = os.path.join(data_path, today, file_name_stock)
department_sava_path = os.path.join(data_path, today, file_name_securities_sales_department)

if os.path.exists(stock_sava_path):
    print(f"{file_name_stock} 最新数据已存在.")
else:
    print("开始下载龙虎榜股票明细数据...")
    stock_lhb_detail_em_df = ak.stock_lhb_detail_em(start_date=start_date, end_date=today)
    stock_lhb_detail_em_df.to_csv(stock_sava_path, index=False)
    print(f"已保存{file_name_stock}到{data_path}目录下.")

if os.path.exists(department_sava_path):
    print(f"{file_name_securities_sales_department} 最新数据已存在.")
else:
    print(f"开始下载证券营业部信息...")
    stock_lhb_hyyyb_em_df = ak.stock_lhb_hyyyb_em(start_date=start_date, end_date=today)
    stock_lhb_hyyyb_em_df.to_csv(department_sava_path, index=False)
