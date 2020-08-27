# django_project

django_project is an initial Django boilerplate project.

## Getting started with this boilerplate:
##### (eg. in any Linux distribution, you can follow a similar process in another os also.)

1. Create a project root directory in your local machine
```bash
mkdir <project_name> 
```
2. Clone the project in this <project_name> directory (you can use ssh also)
```bash
cd <project_name>
git clone https://github.com/depeshpo/django_project.git
```
3. Create your virtual environment, activate that environment and install all the requirements
```bash
pip install -r requirements.txt
``` 
4. collect all static files (if run for the first time it creates the assests folder in <project_name> directory)
```bash
django-admin collectstatic
```
5. create `env.py` inside `<project_name/django_project/config/settings/`. Copy from `env.example.py` for the first time and update settings as your requirements.
6. Remember `<project_name>/django_project` is the directory name from where you will run the server.

### optional:
1. Rename the `django_project` by running following command (from inside of your Django environment):
```bash
django-admin rename_project <new_name_for_django_project>
```

2. rune migrations
```bash
django-admin migrate
```

3. create superuser
```bash
django-admin create_superuser
```
```python
# initial credential for super-admin is
# username: admin
# email: admin@example.com
# password: admin
```
## Folder Structure
```
<project_name>
|
|---assets (folder created once static files are collected)
|
|---django_project
|   |---apps
|   |   |---core (custom app)
|   |   |---...<other apps>...
|   |   |---urls.py
|   |
|   |---config
|   |   |---settings
|   |   |   |---base.py
|   |   |   |---env.py (ignored by git)
|   |   |   |---env.example.py
|   |   |
|   |   |---asgi.py
|   |   |---urls.py
|   |   |---wsgi.py
|   |   |
|   |   |static_files (all static files we use in development)
|   |   |---base (project as a whole specific static files)
|   |   |   |---css
|   |   |   |---img
|   |   |   |---js
|   |   |---core (my custom app specific)
|   |   |   |---css
|   |   |   |---img
|   |   |   |---js
|   |   |
|   |---templates
|   |   |---core (custom app specific)
|   |   |---<other app specific templates>
|   |   |---base.html (included basics of jquery and bootstrap)
|   |
|   |---.gitignore
|   |---manage.py
|   |---requirements.txt
|
|---media (folder created once items were uploaded)
|---db.sqlite3
```

You can read more on this [medium] article.

[medium]:https://medium.com/@pdipesh/creating-a-boilerplate-for-new-django-project-bf695a26461c
