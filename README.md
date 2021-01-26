# ClinicManagement_FlaskApp
A web-app project for Database subject in university.


This app using : PostgreSQL + Flask

## 1. About database

First, you need to have a database PostgreSQL (pdAdmin4)

Read about databse design in file report.pdf. You can find create-table-sql in file database.sql, and a simple data to test app.

Note : in the report, we have a column in table histories called "note". But in the source code, it is called "disease_name". I'll update soon. 





The trigger code is in file trigger.sql


2. How to run web-app in localhost ?

About me, I using Pycharm. So you can open Terminal in Pycharm :
+ install flask, flask-login, flask-wtf,vv... in venv
+ create a endpoint : $ export flask_app=main.py (in Ubuntu, in Windows, alter "export" by "set")
+ $ flask run

3. All info about project is in file report. A simple data is in file database.sql

## 4. Sign up before sign in this app.

Thanks !
