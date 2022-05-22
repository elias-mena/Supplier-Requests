from flask_wtf import FlaskForm

from wtforms.fields import (
    PasswordField,
    SubmitField,
    StringField,
    EmailField,
    DateField
)

from wtforms.validators import (
    DataRequired,
    EqualTo,
    Length
)


# Form for log in a user
class LoginForm(FlaskForm):
    username = StringField('Nombre de Usuario', validators=[DataRequired(), Length(max=15)])
    password = PasswordField('Contraseña', validators=[DataRequired(), Length(min=8, max=50)])
    submit = SubmitField('Ingresar')


# Form for register a user
class RegistrationForm(FlaskForm):
    username = StringField('Nombre de Usuario', validators=[DataRequired(), Length(min=5, max=9)])
    first_name = StringField('Nombre', validators=[DataRequired(), Length(min=1, max=30)])
    last_name = StringField('Apellidos', validators=[DataRequired(), Length(min=1, max=30)])
    birth_date = DateField('Fecha de nacimiento', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Length(max=40)])
    password = PasswordField('Contraseña', validators=[DataRequired(), Length(min=8, max=50)])
    confirm_password = PasswordField('Confirmar Contraseña', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Registrarse!')
