from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pyautogui
import pyperclip


url = "https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com"
browser = webdriver.Chrome("c:/chromedriver.exe")
browser.implicitly_wait(5) #페이지가 로딩될때까지는 최대 5초동안 기다려준다. 
browser.maximize_window() #화면 최대화
browser.get(url) #페이지 열기

#아이디 입력창
id = browser.find_element(By.CSS_SELECTOR,"#id")
id.click()
pyperclip.copy("presidentkjk")
pyautogui.hotkey("ctrl","v")
# 위에 있던 명령어는 사람이 입력하는것처럼 하고 다음명령어는 봇이 입력하는 걸로 인식
# id.send_keys("presidentkjk")
time.sleep(2)

#비밀번호 입력창
pw = browser.find_element(By.CSS_SELECTOR,"#pw")
pw.click()
pyperclip.copy("kjk21c31906")
pyautogui.hotkey("ctrl","v")
# 위에 있던 명령어는 사람이 입력하는것처럼 하고 다음명령어는 봇이 입력하는 걸로 인식
# pw.send_keys("kjk21c31906")
time.sleep(2)

#로그인 버튼
login_btn = browser.find_element(By.CSS_SELECTOR,"#log\.login")
login_btn.click()