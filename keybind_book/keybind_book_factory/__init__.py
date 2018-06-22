from pynput import keyboard

class Keybind_book_factory:

	# data structure signature
	# [ [(keyboard.Key or keyboard.KeyCode, ...), event_string, [anything_you_like]], ... ]
	
	
	# object creation static methods
	
	@staticmethod
	def create_keybind_book(keybind_data_array):
	
		keybind_book = []
		
		for new_record in keybind_data_array:
			new_record = Keybind_book_factory.record(new_record)
			keybind_book.append(new_record)
			
		# check new data structure is correct
		assert(Keybind_book_factory.is_valid_book(keybind_book))
		
		return keybind_book
	
	@staticmethod
	def record(record_data):
		# reject records with an incorrect number of elements
		assert(len(record_data) == 3)
		
		new_record = {}
		
		new_record["key_combination"] = Keybind_book_factory.key_combination(record_data[0])
		new_record["event"] = Keybind_book_factory.event(record_data[1])
		new_record["data"] = record_data[2]
		
		
		return new_record
	
	
	@staticmethod
	def key_combination(key_combination_data):
		# reject records with no keys to trigger them
		assert(len(key_combination_data) > 0)
		
		new_key_combination = set()
		
		for key_data in key_combination_data:
			key = Keybind_book_factory.key(key_data)
			new_key_combination.add(key)
			
		return new_key_combination
	
	@staticmethod
	def key(key_data):
		#this is messy
		bad_input_message = "Bad input: supplied key character" + str(key_data) + "is not a valid key"
		
		if len(key_data) == 1:
			# check if the key is a valid KeyCode and if so return that
			# just in case
			try:
				new_key = keyboard.KeyCode.from_char(key_data)
			except:
				raise bad_input_message
			
			return new_key
			
		else:
			# iterate through the possible keys to find a match
			# i can probably make this less terrible
			for key_enum in keyboard.Key:
				if key_enum.name == key_data:
					new_key = key_enum
					return new_key
		
		# no match found, bad input
		raise ValueError(bad_input_message)
	
	@staticmethod
	def event(event_data):
		return str(event_data)
	
	
	# type checking static methods
	
	@staticmethod
	def is_valid_book(book):
		correct = True
		for record in book:
			correct = Keybind_book_factory.is_valid_record(record)
			
			if not correct:
				return False
			
		return True
	
	@staticmethod
	def is_valid_record(record):
		#record is valid
		if not type(record) is dict:
			return False
		
		if not "key_combination" in record:
			return False
		if not "event" in record:
			return False
		if not "data" in record:
			return False
		
		#components are valid
		if not Keybind_book_factory.is_valid_keycombination(record["key_combination"]):
			return False
		if not Keybind_book_factory.is_valid_event(record["event"]):
			return False
		if not Keybind_book_factory.is_valid_data(record["data"]):
			return False
		
		# all checks out
		return True
	
	@staticmethod
	def is_valid_event(event):
		if type(event) is str:
			return True
		else:
			return False
	
	@staticmethod	
	def is_valid_data(data):
		if type(data) is list:
			return True
		else:
			return False
	
	@staticmethod
	def is_valid_keycombination(key_combination):
		if not type(key_combination) is set or len(key_combination) < 1:
			return False
		else:
			for element in key_combination:
				#check if key object
				if not(type(element) is keyboard.Key or type(element) is keyboard.KeyCode):
					return False
			return True