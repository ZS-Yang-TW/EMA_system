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
    用來