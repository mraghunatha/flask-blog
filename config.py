import smtplib
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')  or\
            'sqlite:///' + os.path.join(basedir,'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False




    MAIL_SERVER='smtp.gmail.com'
    MAIL_PORT='465'
    MAIL_USE_TLS=1
    # MAIL_USE_SSL=True
    MAIL_USERNAME=['raghutest786@gmail.com']
    MAIL_PASSWORD=['$987654321']
    ADMINS = ['raghutest786@gmail.com']
    LANGUAGES = ['en','es']
    POSTS_PER_PAGE = 5
