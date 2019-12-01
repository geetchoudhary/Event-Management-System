from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.forms import LoginForm, RegistrationForm, VisitorForm, CheckoutForm, VerifyUserForm
from flask_login import current_user, login_user, logout_user
from app.models import Host, Visitor, Visname
from datetime import datetime
from flask_mail import Mail, Message

# flask_mail config
app.config.update(dict(
    DEBUG=True,
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=587,
    MAIL_USE_TLS=True,
    MAIL_USE_SSL=False,
    MAIL_USERNAME='innovaccereventexpo@gmail.com',
    MAIL_PASSWORD='querty$123',
))


def send_email(subject, to, message):
    msg = Message(subject,  # subject
                  sender=("Admin", "innovaccereventexpo@gmail.com "),
                  recipients=[to],
                  body=message)
    mymail.send(msg)


mymail = Mail(app)


def index():
    form = VisitorForm()
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

    if form.validate_on_submit():
        vist = Visitor(name=form.name.data, email=form.email.data, phone=form.phone.data)
        visexp = Visname.query.filter_by(visExpect=form.email.data).first()
        if visexp is not None:
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
    if request.method == 'POST':
        try:
            username = request.form['username']
            password = request.form['password']
            remember_me = request.form['remember_me']
        except KeyError:
            username = request.form['username']
            password = request.form['password']

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
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        password2 = request.form['password2']

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
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
    if form.validate_on_submit():
        host = Host.query.filter_by(id=id).first()
        visexp = Visname(host_id=host.id, visExpect=form.email.data)
        db.session.add(visexp)
        db.session.commit()
        flash('You are now expecting a user')
        return redirect(url_for('host'))
    return render_template('host.html', title='Host', form=form)


@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    form = CheckoutForm()
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
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
