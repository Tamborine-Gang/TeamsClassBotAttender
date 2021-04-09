from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import schedule
import platform
import time
from tkinter import *

class ui(Tk):
	def __init__(self):
		super(ui, self).__init__()
		self.layout()
		self.window_decoration()
		self.no_of_periods = 0
		self.time = ''
		self.periods = []

	def window_decoration(self):
		self.title('Set timetable')
		self.geometry('250x150')

	def layout(self):
		l = Label(self, text = "Welcome").pack()
		l = Label(self, text = "Enter the number of periods...").pack()
		e = Entry(self)
		e.pack()
		b = Button(self, text = "Submit", command = lambda: self.no_p_submit(e.get()))
		b.pack()

	def time_sub(self, t):
		self.get_time.destroy()
		self.time = t
	
	def ask_periods(self, n):
		for a in range(n):
			self.name = str(n)

			self.name = Tk()
			t = "Submit"

			self.name.title("Enter the period")
			l = Label(self.name, text = "Enter the period").pack()
			e = Entry(self.name)
			e.pack()
			b = Button(self.name, text = t, command = lambda: self.period_sent(e.get()))
			b.pack()

			self.name.mainloop()
		self.get_time =Tk()
		l = Label(self.get_time, text = 'Enter the starting time of your classes...').pack()
		e = Entry(self.get_time)
		e.pack()
		b = Button(self.get_time, text = 'Submit', command = lambda: self.time_sub(e.get()))
		b.pack()
		self.get_time.mainloop()

	def no_p_submit(self,p):
		self.destroy()
		self.no_of_periods = int(p)
		self.ask_periods(self.no_of_periods)

	def period_sent(self, t):
		self.name.destroy()
		self.periods.append(t)

print("LOADING THE UI")
win = ui()
win.mainloop()


time_table = win.periods
class login:
	def __init__(self):
		opt = Options()
		opt.add_experimental_option("prefs", { \
			"profile.default_content_setting_values.media_stream_mic": 1, 
			"profile.default_content_setting_values.media_stream_camera": 1,
			"profile.default_content_setting_values.geolocation": 1, 
			"profile.default_content_setting_values.notifications": 1 
		})
		if "linux" in platform.platform().lower():
			PATH = "./chromedriver"
		else:
			PATH = "./chromedriver.exe"
		self.browser = webdriver.Chrome(PATH, options=opt)
		print("INITIALIZED THE BROWSER")
		self.load_creds()
		print("LOADED THE CREDENTIALS")
		self.load_site()
		print("SENT AND LOADED THE SITE")
		self.login(self.username, self.password)
		self.wait_till_load()

	def load_site(self):
		# comment to let it collapse haha
		self.browser.get("https://teams.microsoft.com/go#")

	def load_creds(self):
		with open('username.txt', "r") as f:
			self.username = f.readlines()
		with open('password.txt', "r") as f:
			self.password = f.readlines()

	def login(self, username, password):
		username_in = self.browser.find_element_by_xpath('/html/body/div/form[1]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/input[1]')
		username_in.send_keys(username)
		time.sleep(1)
		try:
			n_but = WebDriverWait(self.browser, 10).until(
				EC.presence_of_element_located((By.ID, "idSIButton9"))
			)
		finally:
			n_but.click()
		print("DONE USERNAME SUBMIT PROCESS")
		time.sleep(1)
		try:
			pass_in = WebDriverWait(self.browser, 10).until(
				EC.presence_of_element_located((By.XPATH, "/html/body/div/form[1]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/input"))
			)
		finally:
			pass_in.send_keys(password)
		s_but = self.browser.find_element_by_xpath("/html/body/div/form[1]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div[3]/div[2]/div/div/div/div/input")
		s_but.click()
		print("SUBMITTED THE PASSWORD")
		time.sleep(1)
		try:
			no_but = WebDriverWait(self.browser, 10).until(
				EC.presence_of_element_located((By.ID, "idBtn_Back"))
			)
		finally:
			no_but.click()

		print("GOING TO WAIT FOR THE HOMEPAGE AFTER DOING ALL TASKS FOR LOGIN SUCCESSFULLY")

	def wait_till_load(self):
		try:
			e = WebDriverWait(self.browser, 100).until(
				EC.presence_of_element_located((By.ID, "channel-list-favorites-section-selectable-header"))
			)
		finally:
			print("THE SITE IS NOW LOADED, NOW COMING TO MAIN PART")

def get_channels(browser):
	gen = browser.find_element_by_xpath('//*[@id="channel-19:8d5bc02fac144d02b2d0f7863ec2dce1@thread.tacv2"]/a/div[1]/span')
	bio = browser.find_element_by_xpath('//*[@id="channel-19:87f17b8dcd6b45459ffa939d728afa55@thread.tacv2"]/a/div[1]/span')
	chem = browser.find_element_by_xpath('//*[@id="channel-19:076418579c704a6c83089e8748c3231a@thread.tacv2"]/a/div[1]/span')
	eng = browser.find_element_by_xpath('//*[@id="channel-19:e43f0b3b194443f195e7a708117a86e6@thread.tacv2"]/a/div[1]/span')
	it = browser.find_element_by_xpath('//*[@id="channel-19:46487a0ccef1439cb80b0fd5f5082d71@thread.tacv2"]/a/div[1]/span')
	math = browser.find_element_by_xpath('//*[@id="channel-19:7a5ff6e52e164307b60f35cb8b20c078@thread.tacv2"]/a/div[1]/span')
	phy = browser.find_element_by_xpath('//*[@id="channel-19:d70f912272954ef5ac2b170c0323b5c8@thread.tacv2"]/a/div[1]/span')
	sst = browser.find_element_by_xpath('//*[@id="channel-19:628cce7ebafd45de9781f7e6acf8393c@thread.tacv2"]/a/div[1]/span')
	hin = browser.find_element_by_xpath('//*[@id="channel-19:95e4284cb1704affabb3647c2448d4db@thread.tacv2"]/a/div[1]/span')
	class_lis = [['gen', gen], ['bio', bio], ['chem', chem], ['eng', eng], ['it', it], ['math', math], ['phy', phy], ['sst', sst], ['hin', hin]]
	return class_lis

def join_class(driver, period):
	period.click()
	print("GOT IN THE CHANNEL")
	time.sleep(5)
	joinbtn = l.browser.find_element_by_class_name("ts-calling-join-button")
	joinbtn.click()
	time.sleep(5)
	webcam = driver.find_element_by_xpath('//*[@id="page-content-wrapper"]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[2]/toggle-button[1]/div/button/span[1]')
	if(webcam.get_attribute('title')=='Turn camera off'):
		webcam.click()
		print("TURNED OFF THE CAMERA")
	time.sleep(1)
	microphone = driver.find_element_by_xpath('//*[@id="preJoinAudioButton"]/div/button/span[1]')
	if(microphone.get_attribute('title')=='Mute microphone'):
		microphone.click()
		print("TURNED OFF THE MICROPHONE")
	time.sleep(1)
	joinnowbtn = driver.find_element_by_xpath('//*[@id="page-content-wrapper"]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[1]/div/div/button')
	joinnowbtn.click()
	print("POGPOGPOGPOG SUCCESFULLY JOINT CLASS")

def leave_class(driver, period):
	driver.find_element_by_class_name("ts-calling-screen").click()
	time.sleep(1)
	driver.find_element_by_xpath('//*[@id="hangup-button"]').click()

def scheduler(browser, lis):
	print("TIME FOR DOING THE TASK")
	for a in lis:
		join_class(browser, a)
		print("JOINT CLASS ", a)
		print("NOW IN SLEEP MODE FOR 40 MINS UNTILL LEAVING CLASS")
		time.sleep(2400) # 2400
		leave_class(browser, a)
		print("LEFT CLASS ", a)
		print("NOW IN SLEEP MODE FOR 20 MINS UNTILL NEXT CLASS")
		time.sleep(1200)  # 1200

l = login()


class_lis = get_channels(l.browser)
print("GOT THE CHANNELS OF YOUR TEAM")
x_path_lis = []

for a in time_table:
	for i in range(len(class_lis)):
		if a == class_lis[i][0]:
			x_path_lis.append(class_lis[i][1])
			break
print("DONE ARRANGING YOUR CHANNELS WITH YOUR TIME TABLE ENTERED")

schedule.every().day.at(win.time).do(lambda: scheduler(l.browser, x_path_lis))
print("DONE SCHEDULING")

while True:
	schedule.run_pending()
	time.sleep(1)
