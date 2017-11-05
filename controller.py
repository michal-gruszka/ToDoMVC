from model import Model
from view import View
from task import Task


class Controller:

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def start_program(self):
        self.view.welcome_screen()
        while True:
            option = self.view.menu_screen()
            if option == '1':  # Add task
                self.handle_add_task()
            elif option == '2':  # Modify task
                self.handle_modify_task()
            elif option == '3':  # Delete task
                pass
            elif option == '4':  # Mark task as done
                pass
            elif option == '5':  # Display all tasks
                self.handle_display_tasks()
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
        except (TypeError, ValueError) as e:
            self.view.error_screen(str(e))
        else:
            self.view.message_screen('Task added!')

    def handle_modify_task(self):
        if len(self.model.tasks) == 0:
            self.view.message_screen('There are no tasks!')
            return
        tasks_str = self.model.__str__()
        task_index = self.view.modify_task_screen(tasks_str)
        try:
            task_index = int(task_index)
            task = self.model.tasks[task_index]
        except (TypeError, ValueError, IndexError):
            self.view.error_screen('Invalid index number!')
            return

        while True:
            option = self.view.modify_task_choice_screen(task.get_name(), task.get_description())

            if option == '1':  # Change name
                new_name = self.view.change_name_screen(task.get_name())
                try:
                    task.set_name(new_name)
                except (TypeError, ValueError) as e:
                    self.view.error_screen(str(e))
                else:
                    self.view.message_screen('Task name changed!')
            
            elif option == '2':  # Change description
                new_desc = self.view.change_description_screen(task.get_description())
                try:
                    task.set_description(new_desc)
                except (TypeError, ValueError) as e:
                    self.view.error_screen(str(e))
                else:
                    self.view.message_screen('Task description changed!')
            
            elif option == '3':  # Change name and description
                new_name = self.view.change_name_and_description_screen(task.get_name(), task.get_description())
                try:
                    task.set_name(new_name)
                    task.set_description(new_desc)
                except (TypeError, ValueError) as e:
                    self.view.error_screen(str(e))
                else:
                    self.view.message_screen('Task name and description changed!')

            elif option == '0':
                break

    def handle_delete_task(self):
        pass

    def handle_mark_as_done(self):
        pass

    def handle_display_tasks(self):
        tasks_str = self.model.__str__()
        self.view.display_tasks_screen(tasks_str)

    def handle_display_task_details(self):
        pass