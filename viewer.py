import os
import time


class Viewer:

    def welcome_screen(self):
        os.system('clear')
        print('\n      Welcome!      \n')
        time.sleep(2)
    
    def menu_screen(self):
        os.system('clear')
        print('========== Task Manager ==========\n\n',
              '(1) Add task\n',
              '(2) Modify task\n',
              '(3) Delete task\n',
              '(4) Mark task as done\n',
              '(5) Display all tasks\n',
              '(6) Display task details\n',
              '(0) Exit\n')

    def add_task_screen(self):
        os.system('clear')
        print('========== Task Manager ==========\n\n')
        name = input('Enter task name: ')
        description = input('Enter task description: ')
        return (name, description)

    def add_task_success_screen(self):
        print('========== Task Manager ==========\n\n',
              '            Task added!               ')
        time.sleep(2)

    def add_task_fail_screen(self, error_msg='Invalid inputs'):
        print('========== Task Manager ==========\n\n',
              '            Error: ' + error_msg)
        time.sleep(2)

    def modify_task_screen(self, task):
        print('========== Task Manager ==========\n\n',
              'Task name: ' + task.name + '\n',
              'Description: ' + task.description + '\n\n',
              'Choose the action: \n',
              '(1) Change name \n',
              '(2) Change description \n',
              '(3) Change name and description \n',
              '(0) Cancel \n')

    def change_name_screen(self, task):
        print('========== Task Manager ==========\n\n',
              'Task name: ' + task.name + '\n\n')
        name = 'Enter new task name: '
        return name

    def change_description_screen(self, task):
        print('========== Task Manager ==========\n\n',
              'Task description: ' + task.description + '\n\n')
        description = 'Enter new task description: '
        return description

    def change_name_and_description_screen(self, task):
        print('========== Task Manager ==========\n\n',
              'Task name: ' + task.name + '\n\n')
        name = 'Enter new task name: '
        print('Task description: ' + task.description + '\n\n')
        description = 'Enter new task description: '
        return (name, description)