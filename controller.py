from model import Model
from view import View
from task import Task
import os


class Controller:

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def start_program(self):
        self.model.load_from_file()
        self.view.welcome_screen()
        while True:
            option = self.view.menu_screen()
            if option == '1':  # Add task
                self.handle_add_task()
            elif option == '2':  # Modify task
                self.handle_modify_task()
            elif option == '3':  # Delete task
                self.handle_delete_task()
            elif option == '4':  # Mark task as done
                self.handle_mark_unmark()
            elif option == '5':  # Display all tasks
                self.handle_display_tasks()
            elif option == '6':  # Display task details
                self.handle_display_task_details()
            elif option == '7':  # Archive done tasks
                self.handle_archive_tasks()
            elif option == '0':  # Exit
                self.handle_exit()

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
        if self.model.has_no_tasks():
            self.view.message_screen('There are no tasks!')
            return
        tasks_str = self.model.__str__()
        task_index = self.view.modify_task_screen(tasks_str)
        try:
            task_index = int(task_index)
            task = self.model.get_task(task_index)
        except (TypeError, ValueError, IndexError):
            self.view.error_screen('Invalid index number!')
            return

        while True:
            option = self.view.modify_task_choice_screen(task.get_name(), task.get_description())

            if option == '1':  # Change name
                self.handle_change_name(task)
            
            elif option == '2':  # Change description
                self.handle_change_description(task)
            
            elif option == '3':  # Change name and description
                self.handle_change_name_and_description(task)

            elif option == '0':
                break

    def handle_change_name(self, task):
        new_name = self.view.change_name_screen(task.get_name())
        try:
            task.set_name(new_name)
        except (TypeError, ValueError) as e:
            self.view.error_screen(str(e))
        else:
            self.view.message_screen('Task name changed!')
    
    def handle_change_description(self, task):
        new_desc = self.view.change_description_screen(task.get_description())
        try:
            task.set_description(new_desc)
        except (TypeError, ValueError) as e:
            self.view.error_screen(str(e))
        else:
            self.view.message_screen('Task description changed!')

    def handle_change_name_and_description(self, task):
        new_name = self.view.change_name_and_description_screen(task.get_name(), task.get_description())
        try:
            task.set_name(new_name)
            task.set_description(new_desc)
        except (TypeError, ValueError) as e:
            self.view.error_screen(str(e))
        else:
            self.view.message_screen('Task name and description changed!')

    def handle_delete_task(self):
        if self.model.has_no_tasks():
            self.view.message_screen('There are no tasks!')
            return
        tasks_str = self.model.__str__()
        task_index = self.view.delete_task_screen(tasks_str)
        try:
            task_index = int(task_index)
            self.model.delete_task(task_index)
        except (TypeError, ValueError, IndexError):
            self.view.error_screen('Invalid index value!')
        else:
            self.view.message_screen('Task deleted!')

    def handle_mark_unmark(self):
        if self.model.has_no_tasks():
            self.view.message_screen('There are no tasks!')
            return
        tasks_str = self.model.__str__()
        task_index = self.view.mark_task_screen(tasks_str)
        try:
            task_index = int(task_index)
            self.model.mark_unmark_task(task_index)
        except (TypeError, ValueError, IndexError):
            self.view.error_screen('Invalid index value!')
        else:
            self.view.message_screen('Task marking updated!')

    def handle_display_tasks(self):
        if self.model.has_no_tasks():
            self.view.message_screen('There are no tasks!')
            return
        tasks_str = self.model.__str__()
        self.view.display_tasks_screen(tasks_str)

    def handle_display_task_details(self):
        if self.model.has_no_tasks():
            self.view.message_screen('There are no tasks!')
            return
        tasks_str = self.model.__str__()
        task_index = self.view.choose_task_for_details_screen(tasks_str)
        try:
            task_index = int(task_index)
            chosen_task = self.model.get_task(task_index)
        except (TypeError, ValueError, IndexError):
            self.view.error_screen('Invalid index value!')
        else:
            self.view.display_task_details_screen(task_index, chosen_task.get_is_done(),
                                                  chosen_task.get_name(), chosen_task.get_description())

    def handle_archive_tasks(self):
        self.model.archive_tasks()
        self.view.message_screen('Tasks archived!')

    def handle_exit(self):
        self.model.save_to_file()
        self.view.message_screen('            Goodbye!')
        os.system('clear')
        exit()