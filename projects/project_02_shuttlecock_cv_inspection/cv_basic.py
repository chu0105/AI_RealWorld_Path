import cv2
import numpy as np
import os

# 1. 獲取路徑
current_dir = os.path.dirname(os.path.abspath(__file__))

# 2. 建立一個「虛擬羽球」影像 (如果你現在手邊沒照片，我們先用程式畫一個)
# 建立一個黑底畫布
image = np.zeros((400, 400), dtype="uint8")
# 畫一個白色的三角形 (模擬羽球頭)
cv2.setRNGSeed(42)
pts = np.array([[200, 100], [150, 300], [250, 300]], np.int32)
cv2.fillPoly(image, [pts], 255)
# 畫幾條線 (模擬羽毛)
cv2.line(image, (150, 300), (100, 380), 255, 2)
cv2.line(image, (250, 300), (300, 380), 255, 2)

# 3. 核心視覺算法：Canny 邊緣檢測
# 這是辨識物體形狀最經典的演算法
edges = cv2.Canny(image, 100, 200)

# 4. 儲存結果
cv2.imwrite(os.path.join(current_dir, 'shuttlecock_template.png'), image)
cv2.imwrite(os.path.join(current_dir, 'detected_edges.png'), edges)

print(">>> 視覺分析完成！")
print(">>> 原圖 'shuttlecock_template.png' 與邊緣偵測圖 'detected_edges.png' 已生成。")
