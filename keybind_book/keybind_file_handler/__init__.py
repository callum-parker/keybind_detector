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


if __name__ == "__main__":
	data = [123,[123,1234]]
	Keybind_file_handler.save_keybind_data("./testdata.pickle", data)
	new_data = Keybind_file_handler.load_keybind_data("./testdata.pickle")
	assert(data == new_data)
	print("no issues")