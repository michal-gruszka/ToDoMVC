from task import Task


class Model:

    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        if isinstance(task, Task):
            self.tasks.append(task)
        else:
            raise TypeError("'task' must be an instance of Task class.")

    def delete_task(self, index):
        if index in range(0, len(self.tasks)):
            del self.tasks[index]
        else:
            raise ValueError('Invalid index value.')

    def mark_task_as_done(self, index):
        if not self.tasks[index].is_done:
            self.tasks[index].is_done = True

    def __str__(self):
        if len(self.tasks) == 0:
            return '-- The list is empty --'
        string = ''
        i = 0
        for task in self.tasks:
            string += '({}) {}: {}\n'.format(i, task.get_name(), task.get_description())
        return string