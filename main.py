from selenium import webdriver
import platform
import time

if "linux" in platform.platform().lower():
	PATH = "./chromedriver"
else:
	PATH = "./chromedriver.exe"

browser = webdriver.Chrome(PATH)

browser.get("https://teams.microsoft.com/go#")
time.sleep(5)
browser.close()
