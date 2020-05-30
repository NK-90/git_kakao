import pywinauto
import time
from pywinauto.keyboard import send_keys
app = pywinauto.application.Application()


#대기 후 실행
time.sleep(35)


# 카카오톡 실행 후, 한번 클릭
pywinauto.mouse.click(button='left', coords=(866,513))
app.start('c:\Program Files (x86)\Kakao\KakaoTalk\KakaoTalk.exe')
pywinauto.mouse.click(button='left', coords=(866,513))

# #10초 대기후에  한번클릭&비번입력
time.sleep(10)
pywinauto.mouse.click(button='left', coords=(866,513))
time.sleep(10)
send_keys('Wlqwndfur423!{ENTER}')




