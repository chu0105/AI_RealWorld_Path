import requests
import os

url = "https://upload.wikimedia.org/wikipedia/commons/1/1d/Badminton_Shuttlecock_%28Feather%29.jpg"
headers = {'User-Agent': 'Mozilla/5.0'}
# 使用點號 '.' 代表當前目錄
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'real_shuttlecock.jpg')

try:
    response = requests.get(url, headers=headers)
    with open(path, 'wb') as f:
        f.write(response.content)
    print(">>> [成功] 真實羽球影像已下載！")
except Exception as e:
    print(f">>> [失敗] 下載出錯: {e}")
