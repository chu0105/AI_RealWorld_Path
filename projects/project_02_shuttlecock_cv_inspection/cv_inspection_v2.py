import cv2
import numpy as np
import os
import requests

# 1. 獲取絕對路徑
current_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_dir, 'real_shuttlecock.jpg')

# 2. 定義一個「救援下載」函數
def rescue_download(path):
    print(">>> [救援啟動] 正在從備用來源下載真實羽球圖...")
    # 這是 Unsplash 上的高品質羽球圖
    url = "https://images.unsplash.com/photo-1626225967045-9410dd993c4c?q=80&w=1000&auto=format&fit=crop"
    try:
        response = requests.get(url, timeout=10)
        with open(path, 'wb') as f:
            f.write(response.content)
        print(">>> [成功] 救援圖片已存檔！")
        return True
    except:
        print(">>> [失敗] 救援下載也失敗了，請檢查網路。")
        return False

# 3. 讀取並檢查影像
image = cv2.imread(image_path)

# 如果檔案太小或讀不到，啟動救援
if image is None or os.path.getsize(image_path) < 1000:
    if rescue_download(image_path):
        image = cv2.imread(image_path)

if image is None:
    print(">>> [嚴重錯誤] 依然無法讀取影像，請手動放一張照片到資料夾。")
    exit()

# 4. 工業級視覺處理流水線 (A級底座技能)
# A. 轉灰階
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# B. 高斯模糊 (去雜訊)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
# C. Canny 邊緣檢測
edges = cv2.Canny(blurred, 50, 150)

# 5. 儲存結果
cv2.imwrite(os.path.join(current_dir, 'shuttlecock_edges_v2.png'), edges)
cv2.imwrite(os.path.join(current_dir, 'shuttlecock_gray_template.png'), gray)

print(f"\n>>> [分析完成] 成果報告：")
print(f">>> 1. 原始圖片路徑: {image_path}")
print(f">>> 2. 生成邊緣偵測: shuttlecock_edges_v2.png")
