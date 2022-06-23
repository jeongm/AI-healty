from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired

# FlaskForm  폼 생성
class RegisterForm(FlaskForm):
    userid = StringField('id', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    username = StringField('username', validators=[DataRequired()])
    re_password = PasswordField('password2', validators=[DataRequired()])
    phone = PasswordField('phone_num', validators=[DataRequired()])
    age = PasswordField('age', validators=[DataRequired()])
    sex = PasswordField('SEX1', validators=[DataRequired()])
    height = PasswordField('height', validators=[DataRequired()])
    weight = PasswordField('weight', validators=[DataRequired()])