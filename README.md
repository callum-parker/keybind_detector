# keybind_detector
a tool for registering keybinds that activate on key input regardless of the application having focus or not

a few notes on using this, should anyone actually want to:

Keybind_detector is a threading.Thread object, and will run as a daemon. to create it, either supply it with just your callback method, or a callback method and a name for the saved keybinding records. once start()ed it will run in the background, listening to key input and testing all currently pressed keys against its keybind_list object on release, to see if the set of those keys matches any keybindings registered with it. keybind_list is a Keybind_book object, which manages the keybindings. the Keybind_book_factory class can be used to construct keybindings manually, though this will eventually be revised into a better interface for the user. the input required to create a given record in the factory is a list containing a set of pynput.Key or pynput.KeyCode objects, a string containing any event information you would like to store about the keybind for your own use, and a list of any data you want to store for your own use.

better documentation coming soon.