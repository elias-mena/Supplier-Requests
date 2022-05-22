from flask_wtf import FlaskForm

from wtforms.fields import (
    StringField,
    SubmitField,
    IntegerField,
    TextAreaField
)

from wtforms.validators import (
    DataRequired,
    Length,
    NumberRange
)


# Form for create a new request
class RequestForm(FlaskForm):
    product = StringField('Producto', validators=[DataRequired(), Length(max=50)])
    description = TextAreaField('Descripción', validators=[DataRequired()])
    amount = IntegerField('Monto', validators=[DataRequired(), NumberRange(min=1, max=10000000)])
    submit = SubmitField('Enviar Solicitud')