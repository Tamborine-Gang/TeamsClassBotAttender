from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import platform
import time
import sqlite3

conn = sqlite3.connect("teamsbot.db")
cursor = conn.cursor()

class TeamsClassAttender:
    def __init__(self, browser, username, password):
        self.browser= browser
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS timetable(monday VARCHAR(255), tuesday VARCHAR(255), wednesday VARCHAR(255), thursday VARCHAR(255), friday VARCHAR(255));
        """)
        self.makeTable()
        self.loadSite()
        time.sleep(3)
        self.login(username, password)

    def makeTable(self):
        monday = input("Time table for monday Example(maths, english, sst, hindi, german): ")
        tuesday = input("Time table for tuesday Example(maths, english, sst, hindi, german): ")
        wednesday = input("Time table for wednesday Example(maths, english, sst, hindi, german): ")
        thursday = input("Time table for thursday Example(maths, english, sst, hindi, german): ")
        friday = input("Time table for friday Example(maths, english, sst, hindi, german): ")

        if(monday == "pass"):
            cursor.execute("select monday from timetable")
            monday = cursor.fetchall()

        if(tuesday == "pass"):
            cursor.execute("select tuesday from timetable")
            tuesday = cursor.fetchall()

        if(wednesday == "pass"):
            cursor.execute("select wednesday from timetable")
            tuesday = cursor.fetchall()

        if(thrusday == "pass"):
            cursor.execute("select thursday from timetable")
            tuesday = cursor.fetchall()

        if(friday == "pass"):
            cursor.execute("select friday from timetable")
            tuesday = cursor.fetchall()
        
        
        periods = {
            "monday" : monday,
            "tuesday": tuesday,
            "wednesday": wednesday,
            "thursday": thursday,
            "friday": friday}

        print(periods)

    def loadSite(self):
        browser.get("https://teams.microsoft.com/go#")

    def login(self, username, password):
        #Fill username 
        input_field = browser.find_element_by_xpath('/html/body/div/form[1]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/input[1]')
        input_field.send_keys(username)

	
	#Fill password
        time.sleep(1)
        password_field = browser.find_element_by_xpath("/html/body/div/form[1]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/input")
        password_field.send_keys(password)
        login_button = browser.find_element_by_xpath("/html/body/div/form[1]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div[3]/div[2]/div/div/div/div/input")
        login_button.click()

	
	# stay signed in 
        time.sleep(5)
        no_but = browser.find_element_by_xpath('/html/body/div/form/div/div/div[1]/div[2]/div/div[2]/div/div[3]/div[2]/div/div/div[1]/input')
        no_but.click()

        time.sleep(15)

        teams_mode_but = browser.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/app-bar/nav/ul/li[2]/button')
        teams_mode_but.click()



if "linux" in platform.platform().lower():
	PATH = "./chromedriver"
else:
	PATH = "./chromedriver.exe"

with open('./username.txt', 'r') as f:
	username = f.readlines()
with open('./password.txt', 'r') as f:
	password = f.readlines()
	
browser = webdriver.Chrome(PATH)
TeamsClassAttender(browser, username, password)
