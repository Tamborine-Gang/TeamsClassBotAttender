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
