from flask_wtf.file import FileAllowed, FileField, FileRequired, FileStorage
from wtforms import Form, IntegerField, DecimalField, StringField, BooleanField, TextAreaField, validators, ValidationError


class Addproducts(Form):
    name = StringField('Name', [validators.DataRequired()])
    price = DecimalField('Price', [validators.DataRequired()])
    discount = IntegerField('Discount', default=0)
    stock = IntegerField('Stock', [validators.DataRequired()])
    description = TextAreaField('Description',[validators.DataRequired()])
    colors = TextAreaField('Colors', [validators.DataRequired()])

    image_1 = FileField('Image 1', validators=[FileAllowed(['jpg', 'png', 'gif', 'jpeg', 'jfif'], 'Images only Please!')])

    image_2 = FileField('Image 2',  validators=[FileAllowed(['jpg', 'png', 'gif', 'jpeg', 'jfif'], 'Images only Please!')])

    image_3 = FileField('Image 3',  validators=[FileAllowed(['jpg', 'png', 'gif', 'jpeg', 'jfif'], 'Images only Please!')])
    