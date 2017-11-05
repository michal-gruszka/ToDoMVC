class Task:
    """ An object representing a task/to-do item. """
    def __init__(self, name):
        self.set_name(name)
        self._description = '---'
        self._is_done = False

    def set_name(self, name):
        if type(name) != str:
            raise TypeError("'name' must be a string.")
        if len(name) < 1 or len(name) > 20:
            raise ValueError("'name' must be 1-20 characters long.")
        self._name = name
    
    def get_name(self):
        return self._name

    def set_description(self, description):
        if type(description) != str:
            raise TypeError("'description' must be a string.")
        if len(description) < 1 or len(description) > 150:
            raise ValueError("'description' must be 1-150 characters long.")
        self._description = description

    def get_description(self):
        return self._description

    def toggle_is_done(self):
        if self._is_done:
            self._is_done = False
        else:
            self._is_done = True

    def get_is_done(self):
        return self._is_done

    def __str__(self):
        return '[{}] {}: {}'.format('X' if self._is_done else ' ', self._name, self._description)