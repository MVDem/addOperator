from django.apps import AppConfig


class TodoConfig(AppConfig):
    name = 'todo'

    def ready(self):
        print('app ready')
        from .todo_checker import start_task_check_loop

        start_task_check_loop()

        

  

