from manim import *
from pathlib import Path
import os

# 引入模板
from EMA_system.template import *

# FLAGS 參數設定
FLAGS = f"-v Warning --disable_caching -pqm"
SCENE = "muti_addition" # <- Set the Scene name

# ——————————— 模板製作區塊 ——————————— # 
class muti_addition(addition):
    def construct(self):
        self.muti_addition([1,2,3,1,2,3,5,12,3,3,1,2],(-5,2))
        
# ——————————— 模板製作區塊 ——————————— # 

if __name__ == '__main__':
    script_name = f"{Path(__file__).resolve()}" #獲取本文件的位置
    os.system(f"manim {script_name} {SCENE} {FLAGS}")   #設定命令參數