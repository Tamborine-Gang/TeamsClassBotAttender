from selenium import webdriver
import platform
import time

if "linux" in platform.platform().lower():
	PATH = "./chromedriver"
else:
	PATH = "./chromedriver.exe"
browser = webdriver.Chrome(PATH)

browser.get("https://www.youtube.com")
time.sleep(10)
browser.close()