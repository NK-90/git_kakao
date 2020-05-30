import pywinauto
import time
from pywinauto.keyboard import send_keys
app = pywinauto.application.Application()



#카카오톡 실행
app.start('c:\Program Files (x86)\Kakao\KakaoTalk\KakaoTalk.exe')


#잠시대기후 비번입력
time.sleep(1.7)
pywinauto.mouse.click(button='left', coords=(1121,795))
send_keys('Wlqwndfur423!{ENTER}')