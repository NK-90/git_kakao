import pywinauto
import time
from pywinauto.keyboard import send_keys
app = pywinauto.application.Application()


#대기 후 실행
time.sleep(100)


#카카오톡 실행
app.start('c:\Program Files (x86)\Kakao\KakaoTalk\KakaoTalk.exe')


#10초 대기후, 비번입력
time.sleep(10)
send_keys('Wlqwndfur423!{ENTER}')
