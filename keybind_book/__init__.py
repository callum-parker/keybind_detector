from .keybind_book_factory import Keybind_book_factory
from .keybind_file_handler import Keybind_file_handler

class Keybind_book:
	def __init__(self, save_path):
		self.save_path = save_path
		self.keybindings = Keybind_book_factory.create_keybind_book([])
	
	# internal data management methods
	
	def has(self, key_combination):
		if len(self.lookup(key_combination)) > 0:
			return True
		else:
			return False
	
	def lookup(self, key_combination):
		# input sanity check
		assert(Keybind_book_factory.is_valid_keycombination(key_combination))
		
		matching_records = self.get_matching_records(key_combination)
		return matching_records
	
	def get_matching_records(self, key_combination):
		return [x for x in self.keybindings if x["key_combination"] == key_combination]
	
	def create_keybind(self, new_record_data):
		new_record = Keybind_book_factory.record(new_record_data)
		self.add(new_record)
	
	def add(self, keybind):
		assert(self.is_keybinding(keybind))
		self.keybindings.append(keybind)
		
	def add_and_save(self, keybind):
		self.add(keybind)
		self.save()
	
	def delete(self, record):
		# confirm the keybind record is valid
		assert(self.is_keybinding(record))
		
		# confirm the data structure contains the record
		matches = self.lookup(record["key_combination"])
		assert(len(matches) > 0)
		assert(record in matches)
		
		# delete the record
		self.keybindings.remove(record)
	
	# persistent object state management methods
	
	def load(self):
		Keybind_file_handler.load_keybind_data(self.save_path)
	
	def save(self):
		Keybind_file_handler.save_keybind_data(self.save_path, self.keybindings)
	
	@classmethod
	def is_keybinding(cls, keybinding_record):
		return Keybind_book_factory.is_valid_record(keybinding_record)
