import pandas as pd
import numpy as np
import os
from datetime import datetime, timedelta

# 1. 自動定位路徑
current_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(current_dir, 'shuttlecock_data.csv')

# 2. 生成 1000 筆隨機數據
np.random.seed(42) # 固定種子，確保每次生成的「隨機」都一樣，方便除錯
dates = [(datetime(2026, 4, 6) + timedelta(days=i)).strftime('%Y-%m-%d') for i in range(1000)]
types = np.random.choice(['RSL_No1', 'Yonex_AS30', 'Victor_Master'], 1000)

# 模擬品質分數：平均 75，標準差 10
# 這就是 A 級人才的思維：用數學模型模擬現實
quality = np.random.normal(75, 10, 1000).clip(0, 100) 

df_large = pd.DataFrame({
    'Date': dates,
    'Type': types,
    'Usage_Count': np.random.randint(5, 50, 1000),
    'Quality_Score': quality
})

# 3. 覆蓋存檔
df_large.to_csv(csv_path, index=False)
print(f">>> [成功] 已生成 1000 筆模擬數據並存入 {csv_path}")
