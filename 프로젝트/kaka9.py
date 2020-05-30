import pywinauto
import time
from pywinauto.keyboard import send_keys
app = pywinauto.application.Application()



# 카카오톡 실행 후, 한번 클릭
app.start('c:\Program Files (x86)\Kakao\KakaoTalk\KakaoTalk.exe')

#대기 30초
time.sleep(30)


#클릭 후 비번입력
pywinauto.mouse.click(button='left', coords=(1121,795))
send_keys('Wlqwndfur423!{ENTER}')
