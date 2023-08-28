from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, SelectField
from wtforms.validators import DataRequired, Email, Length, EqualTo


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()],
                           render_kw={'class': 'form-control',
                                      'placeholder': 'Enter username'})
    email = StringField('Email', validators=[DataRequired(), Email()],
                        render_kw={'class': 'form-control',
                                   'placeholder': 'Enter email'})
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)],
                             render_kw={'class': 'form-control',
                                        'placeholder': 'Enter password'})
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')],
                                     render_kw={'class': 'form-control',
                                                'placeholder': 'Confirm password'})