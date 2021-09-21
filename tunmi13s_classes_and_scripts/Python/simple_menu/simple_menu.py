import pygame
import lucia
from lucia import utils
import sys
import time
if not lucia.running: lucia.initialize()
class simple_menu:
	def __init__(self,*args,**kwargs):
		self.wrapping = kwargs.get("wrapping",False)
		self.repeat_edge = kwargs.get("repeat_edge",True)
		self.updown = kwargs.get("updown",True)
		self.leftright = kwargs.get("leftright",False)
		self.homeend = kwargs.get("homeend",True)
		self.clicksound = kwargs.get("clicksound","")
		self.entersound = kwargs.get("entersound","")
		self.wrapsound = kwargs.get("wrapsound","")
		self.opensound = kwargs.get("opensound","")
		self.edgesound = kwargs.get("edgesound","")
		self.items = []
		self.reference_items = []
		self.pool = lucia.audio_backend.SoundPool()
		self.music = lucia.audio_backend.Sound()
	def playclick(self):
		if not self.clicksound == "":
			self.pool.play_stationary(self.clicksound)
	def playwrap(self):
		if not self.wrapsound == "":
			self.pool.play_stationary(self.wrapsound)
	def playopen(self):
		if not self.opensound == "":
			self.pool.play_stationary(self.opensound)
	def playedge(self):
		if not self.edgesound == "":
			self.pool.play_stationary(self.edgesound)
	def playenter(self):
		if not self.entersound == "":
			self.pool.play_stationary(self.entersound)
	def add_item(self,name,internal_name = ""):
		if not name == "":
			self.items.append(str(name))
			if internal_name == "":
				self.reference_items.append(str(name))
			else:
				self.reference_items.append(str(internal_name))

	def get_item_name(self,position):
		if position > len(self.reference_items)-1 or position < 0: return ""
		else: return self.reference_items[position]
	def reset(self,factory = True):
		self.items.clear()
		self.reference_items.clear()
		if factory:
			self.__init__()
	def add_music(self,soundfile):
		try:
			self.music.load(soundfile)
		except: pass
	def run(self,title,interrupt = False):
		lucia.output.speak(title,interrupt)
		mpos = 0
		if self.music.is_active: self.music.play_looped()
		self.playopen()
		while True:
			lucia.process_events()
			time.sleep(0.005)
			if lucia.key_pressed(lucia.K_DOWN) and self.updown:
				if mpos == len(self.items)-1:
					if self.wrapping:
						self.playwrap()
						mpos = 0
						lucia.output.speak(self.items[mpos],True)
					else:
						self.playedge()
						if self.repeat_edge: lucia.output.speak(self.items[mpos],True)
				else:
					mpos += 1
					self.playclick()
					lucia.output.speak(self.items[mpos],True)
			if lucia.key_pressed(lucia.K_UP) and self.updown:
				if mpos == 0:
					if self.wrapping:
						self.playwrap()
						mpos = len(self.items)-1
						lucia.output.speak(self.items[mpos],True)
					else:
						self.playedge()
						if self.repeat_edge: lucia.output.speak(self.items[mpos],True)
				else:
					mpos -= 1
					self.playclick()
					lucia.output.speak(self.items[mpos],True)
			if lucia.key_pressed(lucia.K_RIGHT) and self.leftright:
				if mpos == len(self.items)-1:
					if self.wrapping:
						self.playwrap()
						mpos = 0
						lucia.output.speak(self.items[mpos],True)
					else:
						self.playedge()
						if self.repeat_edge: lucia.output.speak(self.items[mpos],True)
				else:
					mpos += 1
					self.playclick()
					lucia.output.speak(self.items[mpos],True)
			if lucia.key_pressed(lucia.K_LEFT) and self.leftright:
				if mpos == 0:
					if self.wrapping:
						self.playwrap()
						mpos = len(self.items)-1
						lucia.output.speak(self.items[mpos],True)
					else:
						self.playedge()
						if self.repeat_edge: lucia.output.speak(self.items[mpos],True)
				else:
					mpos -= 1
					self.playclick()
					lucia.output.speak(self.items[mpos],True)
			if lucia.key_pressed(lucia.K_HOME) and self.homeend:
				mpos = 0
				self.playedge()
				lucia.output.speak(self.items[mpos],True)
			if lucia.key_pressed(lucia.K_END) and self.homeend:
				mpos = len(self.items)-1
				self.playedge()
				lucia.output.speak(self.items[mpos],True)
			if lucia.key_pressed(lucia.K_PAGEUP) and self.music.is_active and self.music.volume < 0:
				self.music.volume = self.music.volume+5
			if lucia.key_pressed(lucia.K_PAGEDOWN) and self.music.is_active and self.music.volume > -75:
				self.music.volume = self.music.volume-5
			if lucia.key_pressed(lucia.K_ESCAPE): break
			if lucia.key_pressed(lucia.K_RETURN):
				if mpos < 0 or mpos > len(self.items): continue
				self.playenter()
				return mpos
		return -1
	def fade_music(self,fadespeed=30):
		if not self.music.is_active: return
		timer = lucia.utils.timer.Timer()
		while self.music.volume > -100:
			lucia.process_events()
			time.sleep(0.005)
			if timer.elapsed > fadespeed:
				timer.restart()
			self.music.volume = self.music.volume-1
