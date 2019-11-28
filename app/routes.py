from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.forms import LoginForm, RegistrationForm, VisitorForm, CheckoutForm, VerifyUserForm
from flask_login import current_user, login_user, logout_user
from app.models import Host, Visitor
from datetime import datetime
from flask_mail import Mail, Message


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = VisitorForm()
    if form.validate_on_submit():
        vist = Visitor(name=form.name.data, email=form.email.data, phone=form.phone.data)
        host = Host.query.filter_by(vis_name=form.email.data).first()
        if host is not None:
            db.session.add(vist)
            db.session.commit()
            flash('Enjoy your visit')
            return redirect(url_for('index'))
        else:
            flash('No hosts available')
            return redirect(url_for('index'))
    return render_template('index.html', title='Home', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        host = Host.query.filter_by(username=form.username.data).first()
        if host is None or not host.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(host, remember=form.remember_me.data)
        return redirect(url_for('host'))
    return render_template('login.html', title='Sign In', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        host = Host(username=form.username.data, email=form.email.data)
        host.set_password(form.password.data)
        db.session.add(host)
        db.session.commit()
        flash('Congratulations, you are now a registered Host!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/host', methods=['GET', 'POST'])
def host():
    if current_user.is_authenticated:
        id = current_user.get_id()
    form = VerifyUserForm()
    if form.validate_on_submit():
        host = Host.query.filter_by(id=id).first()
        host.vis_name = form.email.data
        db.session.add(host)
        db.session.commit()
        flash('You are now expecting a user')
        return redirect(url_for('host'))
    return render_template('host.html', title='Host', form=form)


@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    form = CheckoutForm()
    if form.validate_on_submit():
        vist = Visitor.query.filter_by(phone=form.phone.data).first()
        if vist is None:
            flash('Check in First')
            return redirect(url_for('checkout'))
        vist.checkOutTime = datetime.utcnow()
        db.session.add(vist)
        db.session.commit()
        flash('Congratulations, you have checked out')
        return redirect(url_for('index'))
    return render_template('checkout.html', title='Checkout', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))