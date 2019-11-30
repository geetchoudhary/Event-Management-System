from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length, NumberRange
from app.models import Host


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Submit')


class VisitorForm(FlaskForm):
    name = StringField('Your Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone', validators=[DataRequired(), Length(10)])
    submit = SubmitField('Submit')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Password2', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Submit')

    def validate_username(self, username):
        host = Host.query.filter_by(username=username.data).first()
        if host is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        host = Host.query.filter_by(email=email.data).first()
        if host is not None:
            raise ValidationError('Please use a different email address.')


class CheckoutForm(FlaskForm):
    name = StringField('Your name', validators=[DataRequired()])
    phone = StringField('Phone No', validators=[DataRequired(), Length(10)])
    submit = SubmitField('Submit')


class VerifyUserForm(FlaskForm):
    name = StringField('Vistior you are expecting?', validators=[DataRequired()])
    email = StringField('Visitors email?', validators=[DataRequired(), Email()])
    submit = SubmitField('Submit')
