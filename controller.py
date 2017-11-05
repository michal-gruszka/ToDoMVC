from model import Model
from view import View


class Controller:

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def start_program(self):
        self.view.welcome_screen()
        option = self.view.menu_screen()
        while True:
            if option == '1':  # Add task
                self.handle_add_task()
            elif option == '2':  # Modify task
                pass
            elif option == '3':  # Delete task
                pass
            elif option == '4':  # Mark task as done
                pass
            elif option == '5':  # Display all tasks
                pass
            elif option == '6':  # Display task details
                pass
            elif option == '0':
                self.view.message_screen('Goodbye!')
                exit()

    def handle_add_task(self):
        name, description = self.view.add_task_screen()
        try:
            new_task = Task(name)
            new_task.set_description(description)
            self.model.add_task(new_task)
        except TypeError, ValueError as e:
            self.view.error_screen(str(e))
        
        self.view.message_screen('Task added!')