import unittest
import sys
import string
from pynput import keyboard

# required to import code
sys.path.append('..')

# the module to be tested
from keybind_book.keybind_book_factory import Keybind_book_factory

class Keybind_book_factory_test_case(unittest.TestCase):
	
	def test_empty_book(self):
		book = Keybind_book_factory.create_keybind_book([])
		assert(book == [])
		
	def test_single_record_book(self):
		keyset = set()
		keyset.add("a")
		event = "test"
		data = ["hello", 123]
		test_record = [keyset, event, data]
		
		book = Keybind_book_factory.create_keybind_book([test_record])
		assert(Keybind_book_factory.is_valid_book(book))

	def test_extreme_data_book(self):
		# create a test data list
		test_keys = set()
		
		for char in string.printable:
			test_keys.add(char)
			
		for other_key in keyboard.Key:
			test_keys.add(other_key.name)
		
		test_event_string = string.printable
		test_data = range(0, sys.maxsize)
			
		test_record = [test_keys, test_event_string, [test_data]]
	
		book = Keybind_book_factory.create_keybind_book([test_record])
		assert(Keybind_book_factory.is_valid_book(book))

if __name__ == '__main__':
    unittest.main()