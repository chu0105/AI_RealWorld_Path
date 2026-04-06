import pandas as pd
import matplotlib.pyplot as plt

# 1. 讀取數據 (A級底座能力：資料處理)
df = pd.read_csv('shuttlecock_data.csv')

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
