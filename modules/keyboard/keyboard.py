from machine import Pin, SoftSPI, I2C
import time
import micropython
from settings import settings_module


class keyboard_module(object):
	global lastdisplay2
	lastdisplay2=""
	
	def __start__(self):
		self.button_up = Pin(20, Pin.IN, Pin.PULL_UP)
		self.button_ok = Pin(19, Pin.IN, Pin.PULL_UP)
		self.button_down = Pin(18, Pin.IN, Pin.PULL_UP)
		
		menu=0
		i2c = I2C(0, sda=Pin(16), scl=Pin(17), freq=400000)
		devices = i2c.scan()
		self.lcd = I2CLcd(i2c, 0x3f, 2, 16)
		self.lcd.clear()
		
		self.display(self,"KEYBOARD", 0, True)
		self.updatemenu(self, menu)
		
		while True:
			if not self.button_up.value() and not menu==0:
				menu=menu-1
				self.updatemenu(self, menu)
				while not self.button_up.value():
					time.sleep(0)
			if not self.button_down.value() and not menu==2:
				menu=menu+1
				self.updatemenu(self, menu)
				while not self.button_down.value():
					time.sleep(0)
			if not self.button_ok.value():
				self.selectoption(self, menu)
				while not self.button_ok.value():
					time.sleep(0)
		return
	
	def updatemenu(self, menu):
		if menu == -1:
			menu = 0
		if menu == 0:
			self.display(self," > keylogger    ", 1)
		if menu == 1:
			self.display(self," > bad usb      ", 1)
		if menu == 2:
			self.display(self," > other        ", 1)
		if menu == 3:
			menu = 4
	
	def selectoption(self, menu):
		if menu == 0:
			self.lcd.clear()
			self.display(self,"keylogger", 0, True)
			self.display(self,"press ok to stop", 1)
		if menu == 1:
			self.lcd.clear()
			self.display(self,"bad usb", 0, True)
			
			return
		if menu == 2:
			self.lcd.clear()
			self.display(self,"uwu2 ", 0)
			self.display(self,"uwu2 ", 1)
			
	def display(self, text, line, middle=False, lastdisplay=lastdisplay2):
		if middle:
			self.lcd.move_to(int(8-len(text)/2), line)
		else:
			self.lcd.move_to(0, line)
		if text!=lastdisplay:
			self.lcd.putstr(text)
		lastdisplay=text



