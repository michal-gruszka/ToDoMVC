from task import Task


class Model:

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

    def __str__(self):
        if len(self._tasks) == 0:
            return '-- The list is empty --'
        string = ''
        i = 0
        for task in self._tasks:
            string += '({}) [{}] {}\n'.format(i, 'X' if task.get_is_done() else ' ', task.get_name())
            i += 1
        return string