import os
import time


class View:

    def welcome_screen(self):
        os.system('clear')
        print('========== Task Manager ==========\n\n',
              '             Welcome!\n')
        time.sleep(1.5)
    
    def menu_screen(self):
        os.system('clear')
        print('========== Task Manager ==========\n\n',
              '(1) Add task\n',
              '(2) Modify task\n',
              '(3) Delete task\n',
              '(4) Mark/unmark task as done\n',
              '(5) Display all tasks\n',
              '(6) Display task details\n',
              '(7) Archive done tasks\n',
              '(0) Exit\n\n')
        option = input('Choose option: ')
        return option

    def add_task_screen(self):
        os.system('clear')
        print('========== Task Manager ==========\n\n')
        name = input('Enter task name: ')
        description = input('Enter task description: ')
        return (name, description)

    def message_screen(self, msg):
        os.system('clear')
        print('========== Task Manager ==========\n\n',
              msg)
        time.sleep(1.5)

    def error_screen(self, error_msg='Invalid input'):
        os.system('clear')
        print('========== Task Manager ==========\n\n',
              'Error: ' + error_msg)
        input('\n    -- Press Enter to continue --   \n')

    def modify_task_choice_screen(self, task_name, description):
        os.system('clear')
        print('========== Task Manager ==========\n\n',
              'Task name: ' + task_name + '\n',
              'Description: ' + description + '\n\n',
              'Choose the action: \n',
              '(1) Change name \n',
              '(2) Change description \n',
              '(3) Change name and description \n',
              '(0) Return \n')
        option = input('Choose option: ')
        return option

    def modify_task_screen(self, tasks_str):
        self._print_tasks_choice(tasks_str)
        task_id = input('Choose task to be modified: ')
        return task_id

    def change_name_screen(self, task_name):
        os.system('clear')
        print('========== Task Manager ==========\n\n',
              'Task name: ' + task_name + '\n\n')
        new_name = input('Enter new task name: ')
        return new_name

    def change_description_screen(self, description):
        os.system('clear')
        print('========== Task Manager ==========\n\n',
              'Task description: ' + description + '\n\n')
        new_description = input('Enter new task description: ')
        return new_description

    def change_name_and_description_screen(self, task_name, description):
        os.system('clear')
        print('========== Task Manager ==========\n\n',
              'Task name: ' + task_name + '\n\n')
        new_name = 'Enter new task name: '
        print('Task description: ' + description + '\n\n')
        new_description = input('Enter new task description: ')
        return (new_name, new_description)

    def delete_task_screen(self, tasks_str):
        self._print_tasks_choice(tasks_str)
        task_id = input('Choose task to be deleted: ')
        return task_id

    def mark_task_screen(self, tasks_str):
        self._print_tasks_choice(tasks_str)
        task_id = input('Choose task to mark/unmark: ')
        return task_id

    def display_tasks_screen(self, tasks_str):
        self._print_tasks_choice(tasks_str)
        input('   -- Press Enter to return -- \n')

    def choose_task_for_details_screen(self, tasks_str):
        self._print_tasks_choice(tasks_str)
        task_id = input('Choose task to see details: ')
        return task_id

    def display_task_details_screen(self, id, is_done, task_name, description):
        os.system('clear')
        print('========== Task Manager ==========\n\n' +
              'Task id: ' + str(id) + '\n' +
              'Done: ' + str(is_done) + '\n' +
              'Name: ' + task_name + '\n' +
              'Description: ' + description + '\n\n')
        input('   -- Press Enter to return -- \n')

    def _print_tasks_choice(self, tasks_str):
        os.system('clear')
        print('========== Task Manager ==========\n\n' +
              tasks_str + '\n')