from urllib import response
import requests

response = requests.get('https://www.naver.com') 
html = response.text
print(html)