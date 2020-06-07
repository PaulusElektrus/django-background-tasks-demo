Little Python & Django Demo of django-background-tasks (https://django-background-tasks.readthedocs.io/en/latest/)

"background_app" provides a view to start 3 different tasks which can then be scheduled by "python manage.py process_tasks" in the command line.

The tasks and completed tasks are stored in the database and are accessible via django admin portal.

To install create a virtual environment (https://www.geeksforgeeks.org/python-virtual-environment/), then "pip install -r requirements.txt".

To run "python manage.py runserver" and if you want to access admin portal "python manage.py createsuperuser".