from task import Task
import os.path


class Model:
    """ Class representing tasks database. """
    
    def __init__(self):
        self._tasks = []

    def get_task(self, index):
        if index in range(0, len(self._tasks)):
            return self._tasks[index]
        else:
            raise IndexError('Invalid index value.')

    def has_no_tasks(self):
        if len(self._tasks):
            return False
        return True

    def add_task(self, task):
        if isinstance(task, Task):
            self._tasks.append(task)
        else:
            raise TypeError("'task' must be an instance of Task class.")

    def delete_task(self, index):
        if index in range(0, len(self._tasks)):
            del self._tasks[index]
        else:
            raise IndexError('Invalid index value.')

    def mark_unmark_task(self, index):
        task = self.get_task(index)
        task.toggle_is_done()

    def archive_tasks(self):
        self._tasks = [t for t in self._tasks if not t.get_is_done()]

    def save_to_file(self, filename='tasks.csv'):
        with open(filename, 'w') as f:
            for task in self._tasks:
                line = '{},{},{}\n'.format(task.get_is_done(), task.get_name(), task.get_description())
                f.write(line)
    
    def load_from_file(self, filename='tasks.csv'):
        if os.path.isfile(filename):
            tasks = []
            with open(filename, 'r') as f:
                for line in f:
                    is_done, name, description = line.rstrip('\n').split(',')
                    task = Task(name)
                    task.set_description(description)
                    if is_done == 'True':
                        task.toggle_is_done()
                    tasks.append(task)
                self._tasks = tasks
            
    def __str__(self):
        if len(self._tasks) == 0:
            return '-- The list is empty --'
        string = ''
        i = 0
        for task in self._tasks:
            string += '({}) [{}] {}\n'.format(i, 'X' if task.get_is_done() else ' ', task.get_name())
            i += 1
        return string