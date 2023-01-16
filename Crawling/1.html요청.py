"""
날짜 : 2023/01/16
이름 : 진윤희
내용 : 파이썬 HTML 요청 실습하기
"""
import requests as req

url = 'https://naver.com'

html = req.get(url).text
print(html)