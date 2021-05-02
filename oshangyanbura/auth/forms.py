from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Regexp, Length

class LoginForm(FlaskForm):
    email = StringField("email", validators=[DataRequired(), Email()])
    password = PasswordField("password", validators=[DataRequired()])
    submit = SubmitField("Log in")


class SignupForm(FlaskForm):
    name = StringField("name", validators=[
        DataRequired(), Length(1, 80),
        Regexp('^[A-Za-z][A-Za-z\s]*$', 0,
               'Names must have only letters')])
    email = StringField("email", validators=[
        DataRequired(), Length(1, 120), Email()])
    password = PasswordField("password", validators=[DataRequired()])
    submit = SubmitField("Submit")

