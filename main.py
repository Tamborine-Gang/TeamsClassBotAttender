# imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import platform
import time

def load_site():
	# load the site
	browser.get("https://teams.microsoft.com/go#")


def login(username, password):
	# username 
	input_field = browser.find_element_by_xpath('/html/body/div/form[1]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/input[1]')
	input_field.send_keys(username)
	next_button = browser.find_element_by_xpath("/html/body/div/form[1]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div/div/div[4]/div/div/div/div/input")
	next_button.click()

	#password
	time.sleep(1)
	password_field = browser.find_element_by_xpath("/html/body/div/form[1]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/input")
	password_field.send_keys(password)
	login_button = browser.find_element_by_xpath("/html/body/div/form[1]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div[3]/div[2]/div/div/div/div/input")
	login_button.click()

	# stay signed in 
	time.sleep(1)
	no_but = browser.find_element_by_xpath('/html/body/div/form/div/div/div[1]/div[2]/div/div[2]/div/div[3]/div[2]/div/div/div[1]/input')
	no_but.click()

	time.sleep(15)

	teams_mode_but = browser.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/app-bar/nav/ul/li[2]/button')
	teams_mode_but.click()
	
# credentials loading
with open('./username.txt', 'r') as f:
	username = f.readlines()
with open('./password.txt', 'r') as f:
	password = f.readlines()

# operating system detection for chromdriver
if "linux" in platform.platform().lower():
	PATH = "./chromedriver"
else:
	PATH = "./chromedriver.exe"

# init the driver
browser = webdriver.Chrome(PATH)

load_site()
time.sleep(3)

login(username, password)
