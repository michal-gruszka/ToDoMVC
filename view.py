import os
import time


class View:

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
              '(0) Exit\n\n')
        return option = input('Choose option: ')

    def add_task_screen(self):
        os.system('clear')
        print('========== Task Manager ==========\n\n')
        name = input('Enter task name: ')
        description = input('Enter task description: ')
        return (name, description)

    def message_screen(self, msg):
        print('========== Task Manager ==========\n\n',
              '            ' + msg)
        time.sleep(2)

    def error_screen(self, error_msg='Invalid input'):
        print('========== Task Manager ==========\n\n',
              '            Error: ' + error_msg)
        time.sleep(2)

    def modify_task_screen(self, task_name, description):
        print('========== Task Manager ==========\n\n',
              'Task name: ' + task_name + '\n',
              'Description: ' + description + '\n\n',
              'Choose the action: \n',
              '(1) Change name \n',
              '(2) Change description \n',
              '(3) Change name and description \n',
              '(0) Cancel \n')
        return option = input('Choose option: ')

    def change_name_screen(self, task_name):
        print('========== Task Manager ==========\n\n',
              'Task name: ' + task_name + '\n\n')
        return new_name = 'Enter new task name: '

    def change_description_screen(self, description):
        print('========== Task Manager ==========\n\n',
              'Task description: ' + description + '\n\n')
        return new_description = 'Enter new task description: '

    def change_name_and_description_screen(self, task_name, description):
        print('========== Task Manager ==========\n\n',
              'Task name: ' + task_name + '\n\n')
        new_name = 'Enter new task name: '
        print('Task description: ' + description + '\n\n')
        new_description = 'Enter new task description: '
        return (new_name, new_description)

    def delete_task_screen(self, tasks_str):
        print('========== Task Manager ==========\n\n' +
              tasks_str + '\n')
        task_id = input('Choose task to be deleted: ')
        return task_id

    def mark_task_screen(self, tasks_str):
        print('========== Task Manager ==========\n\n' +
              tasks_str + '\n')
        task_id = input('Choose task to be marked: ')
        return task_id

    def display_tasks_screen(self, tasks_str):
        print('========== Task Manager ==========\n\n' +
              tasks_str + '\n')
        input('   -- Press any key to return -- ')

    def display_specific_task_screen(self, id, task_name, description):
        print('========== Task Manager ==========\n\n' +
              'Task id: ' + id + '\n' +
              'Name: ' + task_name + '\n' +
              'Description: ' + description + '\n\n')
        input('   -- Press any key to return -- ')
