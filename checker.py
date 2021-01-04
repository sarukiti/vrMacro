import ctypes
import pyautogui
try:
    while True:
        if ctypes.windll.user32.GetAsyncKeyState(0x01) == 0x8000:
		    ### ここにクリック時の動作を記入する ###
            x, y = pyautogui.position()
            print(str(x) + ':' + str(y))

except KeyboardInterrupt:
    print('終了')