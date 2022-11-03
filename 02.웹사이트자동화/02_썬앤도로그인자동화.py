from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pyautogui
import pyperclip


url = "https://www.sonndau.com/login?back_url=L3Nvbm5kYXU%3D&used_login_btn=Y"
browser = webdriver.Chrome("c:/chromedriver.exe")
browser.implicitly_wait(5) #페이지가 로딩될때까지는 최대 5초동안 기다려준다. 
browser.maximize_window() #화면 최대화
browser.get(url) #페이지 열기

#아이디 입력창
id = browser.find_element(By.CSS_SELECTOR,"#w202201066d2942e87eedf > div > div > form > div.input_block > div:nth-child(1) > input[type=text]")
id.click()
pyperclip.copy("presidentkjk@naver.com")
pyautogui.hotkey("ctrl","v")
# 위에 있던 명령어는 사람이 입력하는것처럼 하고 다음명령어는 봇이 입력하는 걸로 인식
# id.send_keys("presidentkjk@naver.com")
time.sleep(2)

#비밀번호 입력창
pw = browser.find_element(By.CSS_SELECTOR,"#w202201066d2942e87eedf > div > div > form > div.input_block > div.input_form.brt > input[type=password]")
pw.click()
pyperclip.copy("kjk21c31906")
pyautogui.hotkey("ctrl","v")
# 위에 있던 명령어는 사람이 입력하는것처럼 하고 다음명령어는 봇이 입력하는 걸로 인식
# pw.send_keys("kjk21c31906")
time.sleep(2)

#로그인 버튼
login_btn = browser.find_element(By.CSS_SELECTOR,"#w202201066d2942e87eedf > div > div > form > p > button")
login_btn.click()