import pickle

class Keybind_file_handler:
	@staticmethod
	def load_keybind_data(path):
		keybind_data = []
		with open(path, 'rb') as file:
			keybind_data = pickle.load(file)
		return keybind_data
		
	@staticmethod
	def save_keybind_data(path, data):
		with open(path, 'wb') as file:
			pickle.dump(data, file)