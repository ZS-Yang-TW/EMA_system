# 系統運行需求（EMA system requirement）
## Python 版本需求
目前 EMA 系統可以穩定在 **Python 3.10.5** 下運行。

請至 Python 官方網站下載 [3.10.5的版本]((https://www.python.org/downloads/))。

## Python 套件
1. **Manim** 

    `pip install manim`

    EMA 系統使用的動畫引擎。
2. **jupyter**

    `pip install jupyter`

    測試用的環境。
3. **azure-cognitiveservices-speech**

    `pip install azure-cognitiveservices-speech`

    用來生成語音的套件。
    
    更多更詳細的介紹請看 Azure Text-to-speech [官方文件](https://learn.microsoft.com/en-us/azure/cognitive-services/speech-service/get-started-text-to-speech?tabs=windows%2Cterminal&pivots=programming-language-python)
## 其他工具
1. **FFmpeg** 及 **MikTeX**

    請參照 Manim 的[官方說明](https://github.com/3b1b/manim)文件進行安裝。

2. **K-Lite**

    影音編碼解碼器，用以處理不同介面間的影片播放。
    點這邊 [下載](https://codecguide.com/download_kl.htm)


# 文件說明
以下說明是按照他的依賴順序編排的。
## EMA_system
### calculate.py
    用來計算問題，輸出詳解資料（Explantory Data）。

### addition_text_output.py
    用來輸出詳解語音文字稿。

### template.py
    內含各式模板類別，可做為模組引用至 addition.py。

### addition.py
    加法模板，用來生成加法詳解影片。
    內含：影音對齊功能。

# 使用方式
## 執行方式
執行方法建議是直接在終端機輸入:

`python addition.py`

### 輸出參數設定
可以在前面的"# FLAGS 參數設定"進行一些輸出的調整
```python
# FLAGS 參數設定
FLAGS = f"-v Warning --disable_caching -pqm"
SCENE = "EMA_output" # <- Set the Scene name
```

其中，**SCENE的名字務必和下面class的名稱對應**！

例如：
```python
# FLAGS 參數設定
FLAGS = f"-v Warning --disable_caching -pqm"
SCENE = "EMA_output" # <- Set the Scene name

# ——————————— 模板製作區塊 ——————————— # 
class EMA_output(addition):
    def construct(self):
        ...
```

### ⚠️使用警告⚠️
1. EMA 系統目前尚未經過路徑整合，所以對**路徑的正確性非常敏感的（Path sensitive）**。

    因此，務必注意**終端機的執行位置**，要在EMA_system這個路徑下執行。

2. 因為 EMA 系統需使用 Azure 的語音服務，請在良好的網路環境下執行 EMA 系統。


