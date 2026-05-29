import pandas as pd
import matplotlib.pyplot as plt
import os  # 增加這個模組，處理作業系統路徑

# 1. 自動獲取「這支程式碼檔案」所在的資料夾路徑
# __file__ 代表這支檔案自己，abspath 取絕對路徑，dirname 取資料夾名
current_dir = os.path.dirname(os.path.abspath(__file__))

# 2. 合併路徑，確保無論在哪啟動，都能正確指到同資料夾下的 CSV
csv_path = os.path.join(current_dir, 'shuttlecock_data.csv')

# 3. 讀取數據 (現在無論在哪按按鈕都行了！)
df = pd.read_csv(csv_path)

# ...後面的繪圖邏輯不變...
# 2. 自動清理：填補 Usage_Count 的缺失值為 0
df['Usage_Count'] = df['Usage_Count'].fillna(0)

# 3. 數據運算：計算所有球的平均品質
avg_quality = df['Quality_Score'].mean()
print(f"\n>>> 分析完成！")
print(f">>> 目前羽球平均品質得分: {avg_quality:.2f}")

# 4. 自動畫圖 (輸出為報表圖片)
plt.figure(figsize=(10, 6))
plt.bar(df['Date'], df['Quality_Score'], color='skyblue')
plt.axhline(y=avg_quality, color='red', linestyle='--', label=f'Average: {avg_quality:.2f}')
plt.title('Shuttlecock Quality Analysis Report', fontsize=14)
plt.xlabel('Date')
plt.ylabel('Quality Score')
plt.legend()

# 儲存結果
plt.savefig('quality_report.png')
print(">>> 分析報表 'quality_report.png' 已成功生成！")
