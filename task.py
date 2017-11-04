class Task:
    """ An object representing a task/to-do item. """
    def __init__(self, name):
        self.name = name
        self.description = '---'
        self.is_done = False

    def __str__(self):
        return '{} {}: {}'.format('[X] ' if self.is_done else '[ ] ', self.name, self.description)