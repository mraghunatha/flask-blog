
from flask import render_template,current_app,url_for
from flask_babel import _
from app.email import send_email
# from app.models import User
# from app import mail


from threading import Thread
# from flask import render_template,current_app
from flask_mail import Message
from app import mail



def send_password_reset_email(user):

    token = user.get_reset_password_token()
    # send_email('new Reset message from Hello','mraghunatha81@gmail.com',['mraghunatha81@gmail.com'],'this is body','this is html body')
    send_email('new Reset message from Hello',
                sender=current_app.config['ADMINS'][0],
                recipients=[user.email],
                text_body=render_template('email/reset_password.txt',
                                         user=user, token=token),
                html_body=render_template('email/reset_password.html',
                                                     user=user, token=token))
                # html_body=render_template('email/reset_password.html', user=user, token=token))

                #render_template('email/reset_password.html',
                                #                     user=user, token=token))


# 'this is html body ' +
    # send_email('[Microblog] Reset Your Password',
    #            sender=current_app.config['ADMINS'][0],
    #            recipients=[user.email],
    #            text_body=render_template('email/reset_password.txt',
    #                                      user=user, token=token),
    #            html_body=render_template('email/reset_password.html',
    #                                      user=user, token=token))
