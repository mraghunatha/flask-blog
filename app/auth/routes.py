from datetime import datetime
from app import db #mail,Message
from flask_login import login_user,current_user,logout_user,login_required
from flask import render_template,url_for,redirect,flash,request,g
from werkzeug.urls import url_parse
from flask_babel import _, get_locale
from app.auth import bp
from app.auth.forms import LoginForm,RegistrationForm
from app.models import User
from app.auth.forms import ResetPasswordRequestForm

from app.auth.email import send_password_reset_email,send_email
# from app.auth.email import send_email
from app.auth.forms import ResetPasswordForm









@bp.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username= form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid user name or password")
            return redirect(url_for('auth.login'))
        login_user(user,remember=form.remember_me.data)




        send_email('new message from Hello','raghutest786@gmail.com',['raghutest786@gmail.com'],'this is body','this is html body')


        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc!='':
            next_page = url_for("main.index")
        return redirect(next_page)
    return render_template('auth/login.html',form = form,title="Sign In")

@bp.route('/logout')
def logout():


    logout_user()
    return redirect(url_for('main.index'))


@bp.route('/register', methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('auth.login'))
        # return redirect(url_for('main.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations you are now a registered user')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html',title='Register',form=form)




@bp.route('/reset_password_request', methods=['GET', 'POST'])
def reset_password_request():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = ResetPasswordRequestForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            # flash('xCheck your email for the instructions to reset your password')
            send_password_reset_email(user)
        flash('Check your email for the instructions to reset your password')
        return redirect(url_for('auth.login'))
    return render_template('auth/reset_password_request.html',
                           title='Reset Password', form=form)



#when user clicks the link for reset password it connects to following link of reset password
@bp.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    user = User.verify_reset_password_token(token)
    if not user:
        return redirect(url_for('main.index'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()
        flash('Your password has been reset.')
        return redirect(url_for('auth.login'))
    return render_template('auth/reset_password.html', form=form)
