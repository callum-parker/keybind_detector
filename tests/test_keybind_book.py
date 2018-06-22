import unittest
import sys
import string
from pynput import keyboard

# required to import code
sys.path.append('..')

# the module to be tested
from keybind_book import Keybind_book

# additional required modules
from keybind_book.keybind_book_factory import Keybind_book_factory

class Utility_methods():
	test_save_location = "./test_data_save.pickle"

	# simple
	
	@staticmethod
	def get_simple_record_data():
		keyset = set()
		keyset.add("a")
		event = "test"
		data = ["hello", 123]
		test_record_data = [keyset, event, data]
		return test_record_data
		
	@staticmethod
	def get_simple_record():
		test_record_data = Utility_methods.get_simple_record_data()
		test_record = Keybind_book_factory.record(test_record_data)
		return test_record
	
	# extreme
	
	@staticmethod
	def get_extreme_record_data():
		# create the test data
		test_keys = set()
		
		for char in string.printable:
			test_keys.add(char)
			
		for other_key in keyboard.Key:
			test_keys.add(other_key.name)
		
		test_event_string = string.printable
		test_data = range(0, sys.maxsize)
			
		test_record_data = [test_keys, test_event_string, [test_data]]
		
		return test_record_data
	
	@staticmethod
	def get_extreme_record():
		test_record_data = Utility_methods.get_extreme_record_data()
		test_record = Keybind_book_factory.record(test_record_data)
		return test_record
	
	# other
	
	@staticmethod
	def get_keybind_book():
		test_keybind_book = Keybind_book(Utility_methods.test_save_location)
		return test_keybind_book

class Keybind_book_test_case(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.data_set_raw = [
		[],
		Utility_methods.get_simple_record_data(),
		Utility_methods.get_extreme_record_data()
		]
		cls.data_set  = [
		[],
		Utility_methods.get_simple_record(),
		Utility_methods.get_extreme_record()
		]
	
	def setUp(self):
		self.test_keybind_book = Utility_methods.get_keybind_book()
	
	# function test functions
	
	# these methods do not test for proper function as they require checking
	# both for cases where the record isnt present, and where it is
	def run_has_existing_record_test(self, record, key_combination):
		# perform the addition
		self.test_keybind_book.add(record)
		# perform the check
		present = self.test_keybind_book.has(key_combination)
		assert(present)
	
	def run_has_nonexistant_record_test(self, key_combination):
		# perform the check
		present = self.test_keybind_book.has(key_combination)
		# return the result
		assert(not present)
		
	def run_existing_lookup_test(self, record, key_combination):
		# perform the addition
		self.test_keybind_book.add(record)
		# perform the check
		results = self.test_keybind_book.lookup(key_combination)
		# return the result
		assert(results == record)
		
	def run_nonexistant_lookup_test(self, key_combination):
		# perform the check
		results = self.test_keybind_book.lookup(key_combination)
		# return the result
		assert(results == [])
		
	def run_create_test(self, record_data):
		key_combination = set()
		if len(record_data) != 0:
			# perform the creation
			self.test_keybind_book.create_keybind(record_data)
			expected_record = Keybind_book_factory.record(record_data)
			key_combination = expected_record["key_combination"]
			
			# test addition
			assert(self.test_keybind_book.has(key_combination))
			
			# test validity
			result = self.test_keybind_book.lookup(key_combination)[0]
			
			assert(Keybind_book_factory.is_valid_record(result))
		else:
			pass
			# we cant create a bad record with the factory
			with self.assertRaises(AssertionError):
				self.test_keybind_book.create_keybind(record_data)
	
	def run_add_test(self, record):
		if len(record) != 0:
			self.test_keybind_book.add(record)
		else:
			with self.assertRaises(AssertionError):
				self.test_keybind_book.add(record)
	
	def run_add_and_save_test(self, record):
		if len(record) != 0:
			self.test_keybind_book.add_and_save(record)
		else:
			with self.assertRaises(AssertionError):
				self.test_keybind_book.add_and_save(record)
		
	def run_existing_delete_test(self, record):
		# perform the addition
		self.test_keybind_book.add(record)
		# perform the check
		self.test_keybind_book.delete(record)
		
	def run_nonexistant_delete_test(self, record):
		# perform the check
		with self.assertRaises(AssertionError):
			self.test_keybind_book.delete(record)
	
	def run_load_test(self):
		# perform the action
		self.test_keybind_book.load()
		# no testing for proper function yet, just syntax
		
	def run_save_test(self):
		# perform the action
		self.test_keybind_book.save()
		# no testing for proper function yet, just syntax
		
	# test the class method runs the code its supposed to
	def run_is_keybinding_test(self, keybinding_record):
		result = Keybind_book.is_keybinding(keybinding_record)
		expected_result = Keybind_book_factory.is_valid_record(keybinding_record)
		# perform the check
		assert(result == expected_result)
		# return the result
		return result
		
	# tests with various data types
	
	def test_has_existing_record(self):
		for i in self.data_set:
			with self.subTest(i=i):
				if len(i) != 0:
					self.setUp()
					self.run_has_existing_record_test(i, i["key_combination"])
					
	def test_has_nonexistant_record(self):
		for i in self.data_set:
			with self.subTest(i=i):
				if len(i) != 0:
					self.setUp()
					self.run_has_nonexistant_record_test(i["key_combination"])
	
	#lookup run_existing_lookup_test
	def test_lookup_existing_record(self):
		for i in self.data_set:
			with self.subTest(i=i):
				if len(i) != 0:
					self.setUp()
					self.run_has_existing_record_test(i, i["key_combination"])
				
	def test_lookup_nonexistant_record(self):
		for i in self.data_set:
			with self.subTest(i=i):
				if len(i) != 0:
					self.setUp()
					self.run_has_nonexistant_record_test(i["key_combination"])
	
	def test_create_record(self):
		for i in self.data_set_raw:
			with self.subTest(i=i):
				self.setUp()
				self.run_create_test(i)
	
	def test_add_record(self):
		for i in self.data_set:
			with self.subTest(i=i):
				self.setUp()
				self.run_add_test(i)
	
	def test_add_and_save_record(self):
		for i in self.data_set:
			with self.subTest(i=i):
				if len(i) != 0:
					self.setUp()
					self.run_add_and_save_test(i)
	
	def test_delete_existing_record(self):
		for i in self.data_set:
			with self.subTest(i=i):
				if len(i) != 0:
					self.setUp()
					self.run_existing_delete_test(i)
	
	def test_delete_nonexistant_record(self):
		self.run_nonexistant_delete_test(Utility_methods.get_simple_record())
	
	def test_load_record(self):
		for i in self.data_set:
			with self.subTest(i=i):
				if len(i) != 0:
					self.setUp()
					self.test_keybind_book.add(i)
					self.test_keybind_book.save()
					self.run_load_test()
	
	def test_save_record(self):
		for i in self.data_set:
			with self.subTest(i=i):
				if len(i) != 0:
					self.setUp()
					self.test_keybind_book.add(i)
					self.run_save_test()
	
	#is_keybinding
	def test_is_keybinding(self):
		for i in self.data_set:
			with self.subTest(i=i):
				if len(i) != 0:
					self.setUp()
					self.run_is_keybinding_test(i)
	

if __name__ == '__main__':
    unittest.main()