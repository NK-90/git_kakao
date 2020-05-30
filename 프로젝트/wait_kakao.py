import pywinauto
from pywinauto.keyboard import send_keys
app = pywinauto.application.Application()



#앱을 시작한다
app.start('c:\Program Files (x86)\Kakao\KakaoTalk\KakaoTalk.exe')



#앱이 나올때까지 대기한 후, 나오면 윈도우 인자값(=val)을 받아온다
val = pywinauto.timings.wait_until_passes(20, 0.5, lambda: pywinauto.findwindows.find_windows(title=u'\uce74\uce74\uc624\ud1a1', class_name='EVA_Window')[0])
window = app.window(handle=val)



#비번을 입력한다
send_keys('Wlqwndfur423!{ENTER}')
