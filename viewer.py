import os
import time


class Viewer:

    def welcome_screen(self):
        print('\n      Welcome!      \n')
    
    def menu_screen(self):
        print('========== Task Manager ==========\n',
              '(1) Add task\n',
              '(2) Modify task\n',
              '(3) Delete task\n',
              '(4) Mark task as done\n',
              '(5) Display all tasks\n',
              '(0) Exit\n')
