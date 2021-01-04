import os
import sys
import time
import yaml
import pyperclip as pp
import pyautogui as pg

os.chdir(os.path.dirname(sys.argv[0]))

with open('settings.yaml','r',encoding="utf-8") as file:
    obj = yaml.safe_load(file)
path = (obj['path'])
if(obj['resolution']) == "WQHD":
    y = 80
    savey = 1395
elif(obj['resolution']) == "FHD":
    y = 90
    savey = 1040

s = 0

print("原稿の行数を入力してください")
st = input()
print("行数を：" + st + '行としてマクロを実行します')
counter = int(st)

pg.click(20, y,1, 0.1,'left')
while s < counter:
    print(F"{s+1}行目を実行")
    pg.click(20, y,2, 0.1,'left')
    pg.click(240, savey,1, 0.1,'left')
    pp.copy(F"{path}yukari{s+1}")
    pg.hotkey('ctrl','v')
    pg.hotkey('enter')
    s = s+1
    y = y + 13
    time.sleep(1.5)
sys.exit()