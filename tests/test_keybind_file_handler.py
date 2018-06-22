import unittest
import sys
import string
from pynput import keyboard

# required to import code
sys.path.append('..')

# the module to be tested
from keybind_book.keybind_file_handler import Keybind_file_handler

class Keybind_file_handler_test_case(unittest.TestCase):
	def test_write_and_read(self):
		# test data components
		int_data = range(0, sys.maxsize)
		float_data = None
		str_data = string.printable
		key_set_data = set()
		
		for char in string.printable:
			key_set_data.add(keyboard.KeyCode.from_char(char))
		for other_key in keyboard.Key:
			key_set_data.add(other_key)
		
		test_data = [
		int_data,
		float_data,
		str_data,
		key_set_data
		]
		
		Keybind_file_handler.save_keybind_data("./test_data_save.pickle", test_data)
		loaded_data = Keybind_file_handler.load_keybind_data("./test_data_save.pickle")
		assert(test_data == loaded_data)

if __name__ == '__main__':
    unittest.main()