# 海康工業相機 (Hikrobot) 視覺開發手冊

## 1. 硬體規格紀錄
- **型號**: MV-CE120-10UC (USB 3.0 介面)
- **解析度**: 1200 萬畫素
- **核心功能**: BGR8 格式轉換、即時 Canny 檢測。

## 2. 軟體邏輯詳解 (	est.py)
### A. SDK 初始化
- 透過 MvImport 調用海康底層驅動。
- 使用 cast 與 POINTER 處理 Python 與 C 語言之間的記憶體指針問題。

### B. 即時影像處理流水線 (Pipeline)
1. **Grab**: MV_CC_GetOneFrameTimeout (抓取原始數據)。
2. **Convert**: MV_CC_ConvertPixelType (將 Bayer 格式轉為 OpenCV 可讀的 BGR)。
3. **Analyze**: 轉灰階 -> 高斯模糊 -> **Canny 邊緣檢測**。
4. **Display**: 雙視窗對照顯示。

## 3. 操作指令
- **[q]**: 安全關閉相機並釋放記憶體（這點非常重要，否則下次會無法開啟）。
- **[s]**: 自動生成時間戳記存檔，用於建立羽球瑕疵數據庫 (Dataset)。

## 4. 針對「羽毛質量不佳」的對策
- 調整 cv2.Canny(blurred, 50, 150) 中的數字。
- 如果羽毛太亂，增加高斯模糊核大小，例如 (7, 7)。
