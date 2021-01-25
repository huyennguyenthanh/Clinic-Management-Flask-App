import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql:///' + os.path.join(basedir, 'app.db')
    # SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:17071608@localhost:5433/a'
    # # follow and annouce for app when data update
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    # conn = psycopg2.connect(
    #     host="localhost",
    #     database="a",
    #     user="postgres",
    #     password="17071608")
