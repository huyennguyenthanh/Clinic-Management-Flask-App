# ClinicManagement_FlaskApp
A web-app project for Database subject in university.


This app using : PostgreSQL + Flask

1. About database

First, you need to have a database PostgreSQL (pdAdmin4)

Read about databse design in file report.pdf

Note : in the report, we have a column in table histories called "note"

But in the source code, it is calles "disease_name". I'll update soon.



You can find create-table-sql in file database.sql, and a simple data to test app.

The trigger code is in file trigger.sql


2. How to run web-app in localhost ?

About me, I using Pycharm. So you can open Terminal in Pycharm :
+ install flask, flask-login, flask-wtf,vv... in venv
+ create a endpoint : $ export endpoint=main.py
+ $ flask run

3. All info about project is in file report. A simple data is in file database.sql

Thanks !
