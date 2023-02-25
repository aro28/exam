from flask_wtf import FlaskForm
import wtforms as wf


class PositionForm(FlaskForm):
    department = wf.StringField(label='Student Name')
    wage = wf.IntegerField(label='Age', validators=[
        wf.validators.DataRequired(),
        wf.validators.NumberRange(min=0, max=100)
    ])



class EmployeeForm(FlaskForm):
    name = wf.StringField(label='ФИО клиента')
    inn = wf.StringField(label='ИНН паспорт', validators=[
        wf.validators.DataRequired(),
        wf.validators.Length(min=14, max=14)
    ])
    position_id = wf.StringField(label='Позиция клиента')

    def validate_inn(self, field):
        inn = str(field.data)
        if not inn[0].startswith('1', len(inn) != 14):
            raise wf.ValidationError('Начинать с 1 и 2')
        if not inn[0].startswith('2', len(inn) != 14):
            raise wf.ValidationError('Начинать с 1 и 2')
class UserForm(FlaskForm):
    username = wf.StringField(label='Login name', validators=[
        wf.validators.Length(min=6, max=15),
        wf.validators.DataRequired()]
                              )
    password = wf.PasswordField(label='New Password', validators=[wf.validators.DataRequired()])

    # def validate_password(form, field):
    #     if not any(chr.isdigit() for chr in field.data):
    #         raise wf.ValidationError('Password must contain digits and letters')
    #     if len(field.data) < 8:
    #         raise wf.ValidationError('Password must contain a minimum of 8 characters')
    #
    # def validate_username(form, field):
    #     excluded_chars = " *?!'^+%&/()=}][{$#"
    #     for char in field.data:
    #         if char in excluded_chars:
    #             raise wf.ValidationError(
    #                 f"Character {char} is not allowed in username.")
    #     if not any(chr.isdigit() for chr in field.data):
    #         raise wf.ValidationError('Password must contain digits and letters')
