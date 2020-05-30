import pywinauto
from pywinauto.application import Application
from pywinauto.keyboard import send_keys
app = Application()



app.start('c:\Program Files (x86)\Kakao\KakaoTalk\KakaoTalk.exe')



for i in range(1000):
    try:

        w_handle = pywinauto.findwindows.find_windows(title=u'\uce74\uce74\uc624\ud1a1', class_name='EVA_Window')[0]
        window = app.window(handle=w_handle)
        window.click_input()
        send_keys('Wlqwndfur423!{ENTER}')

    except:
        pass




