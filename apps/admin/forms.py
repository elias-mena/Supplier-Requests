from flask_wtf import FlaskForm

from wtforms.fields import (
    PasswordField,
    SubmitField,
    StringField,
    EmailField,
    DateField,
    SelectField
)

from wtforms.validators import (
    DataRequired,
    EqualTo,
    Length
)


# Form for register a user
class NewUserForm(FlaskForm):
    username = StringField('Nombre de Usuario', validators=[DataRequired(), Length(min=5, max=15)])
    first_name = StringField('Nombre', validators=[DataRequired(), Length(min=1, max=30)])
    last_name = StringField('Apellidos', validators=[DataRequired(), Length(min=1, max=30)])
    birth_date = DateField('Fecha de nacimiento', validators=[DataRequired()])
    rol = SelectField('Rol', coerce=int,
                       choices=[(1, 'Administrador'), (2, 'Cliente'), (3, 'Aprovador Jefe'),
                                (4, 'Aprovador Financiero 1'), (5, 'Aprovador Financiero 2'),
                                (6, 'Aprovador Financiero 3')],
                       validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Length(max=40)])
    password = PasswordField('Contraseña', validators=[DataRequired(), Length(min=8, max=50)])
    confirm_password = PasswordField('Confirmar Contraseña', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Insertar Usuario!')


