from .keybind_book import Keybind_book

import os
import threading

from pynput import keyboard

name = "keybind_detector"

class Keybind_detector (threading.Thread):
	def __init__(self, callback, existing_file_path = None):
		# data
		self.default_file_path = "keybindings.pickle"
		
		# set member variables
		self.kb_listener = keyboard.Listener(
			on_press=self.on_press,
			on_release=self.on_release)
		
		self.file_path = existing_file_path
		self.active_keys = set()
		self.callback = callback
		
		# perform appropriate setup depending on if we got a specified file name
		if self.file_path != None:
			self.keybind_list = Keybind_book(self.file_path)
			self.keybind_list.load()
		else:
			self.file_path = self.default_file_path
			self.keybind_list = Keybind_book(self.file_path)
			
			# check if our default file exists and load it, and if not create it
			if os.path.isfile(self.file_path):
				self.keybind_list.load()
			else:
				self.keybind_list.save()
		
		# init base class
		threading.Thread.__init__(self)
		
		# base class properties
		self.daemon = True
	
	def run(self):
		self.kb_listener.join()
		
	def is_active(self):
		return self.kb_listener.running
	
	def stop(self):
		self.kb_listener.stop()
		
	def start(self):
		self.kb_listener.start()
		self.run()
	
	def on_press(self, key):
		self.active_keys.add(key)
		
	def on_release(self, key):
		self.check_for_keybinds()
		self.active_keys.remove(key)
		
	def check_for_keybinds(self):
		if self.keybind_list.has(self.active_keys):
			keybind = self.keybind_list.lookup(self.active_keys)
			if Keybind_book.is_keybinding(keybind):
				pass
			self.callback(keybind)
