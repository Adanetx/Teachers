## Application: React and Djano

This Application is used to list the teachers in collage, this app is very nice to
manage the workers(teachers) in a collage it conatains the detatil information of  the teachers name, age, favorite courese, level of education etc ..
this is

## important links
[client side repository](https://github.com/Adanetx/clientTeachers)
[Deployed app]()
[Api Repo](https://github.com/Adanetx/Teachers)

## user stories

- 'As an unregistered user, I would like to sign up with email and password.
- As a registered user, I would like to sign in with email and password.
- As a signed in user, I would like to change password.
- As a signed in user, I would like to sign out.
-  As a signed in user, I would like to add a teacher to  database (app).
- As a signed in user, I would like to update the teacher that .
- As a signed in user, I would like to delete my  teacher on from the data base(app).
- As a signed in user, I would like to see all my all teachers on Application

## Techinologies use ..

- Django Bd
- python
- rest_framework',
'- rest_framework.authtoken',
 - command line
 - envronmental shell
 - git
 - github

## Instalation and setup process

- download template from [](https://git.generalassemb.ly/Adanetx/django-auth-template)
- move .zip file and unzip it
- replace read me by your own
- git init (means create  git folder)
- Create a `.env` file
-    Add a key `ENV` with the value `development`
- Run `pipenv shell` to start up your virtual environment.
-   Run `pipenv install` to install dependencies.
- Create a psql database for your project_db_name
- Edit `settings.sql` then run `psql -U postgres -f settings.sql`
    OR:
    1. Type `psql` to get into interactive shell.
    2. Run `CREATE DATABASE "project_db_name";` where `project_db_name` is the name you want for your database.
- Add the database name to the `.env` file using the key `DB_NAME_DEV`.
- Replace all instances of `django_auth_template` with your application name. **This includes the folder included in this repository.**


## Commands

Commands are run with the syntax `python3 manage.py <command>`:

| command | action |
|---------|--------|
| `runserver`  |  Run the server |
| `makemigrations`  | Generate migration files based on changes to models  |
| `migrate`  | Run migration files to migrate changes to db  |
| `startapp`  | Create a new app  |



## catalog of Rutes  of the teachers


Verb   | URI Pattern            |
|--------|------------------------|
|   |   |
| GET      | `/teachers/`        |
| GET      | `/teachers/<int:pk>/`|
| POST     | `/teachers`|
| PATCH    | `/teachers/<int:pk>/`|
| DELETE  | `/teachers/<int: pk/`|

## unsolve problems

- still it need add resource
- add more paths...

## Images


RED  IMAGE ..for a time bing it is one to one relationship
I have the user and resource.
  ![ERD](https://i.imgur.com/U6NNbhd.png)
