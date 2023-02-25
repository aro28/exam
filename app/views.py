from flask import render_template, request, redirect, url_for, flash
from app import db
from .models import UserMixin, Employee, Position, User
from .forms import PositionForm, EmployeeForm, UserForm
from flask_login import login_user, logout_user, login_required


def index():
    employees = Employee.query.all()
    return render_template('index.html', employees=employees)

def position_create():
    title = 'Добавление позиции'
    form = PositionForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            position = Position()
            form.populate_obj(position)
            db.session.add(position)
            db.session.commit()
            # return redirect(url_for('index'))
            flash(f"Клиент {position.department} успешно зарегистрирован.")
    return render_template('standard_form.html', form=form, title=title)


def employee_create():
    title = 'Добавление клиента'
    form = EmployeeForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            employee = Employee()
            form.populate_obj(employee)
            db.session.add(employee)
            db.session.commit()
            # return redirect(url_for('index'))
            flash(f"Клиент {employee.name} успешно зарегистрирован.")
    return render_template('standard_form.html', form=form, title=title)


def employee_update(id):
    employee = Employee.query.get(id)
    form = EmployeeForm(obj=employee)

    if request.method == 'POST':
        if form.validate_on_submit():
            form.populate_obj(employee)  # тоже самое что тут   ->    category.code = form.code.data
            db.session.commit()
            flash(f"Клиент {employee.name} успешно зарегистрирован.")
            return redirect(url_for('index'))
        else:
            print(form.errors)  # словарь всех ошибок
    return render_template('standard_form.html', form=form)  # **locals()


def employee_delete(id):
    employee = Employee.query.get(id)
    if request.method == 'POST':
        db.session.delete(employee)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('confirm_delete.html', employee=employee)


def register():
    form = UserForm()
    if request.method == 'POST':
        if form.validate_on_submit():  # правильно ли введены данные, тогда отрабатывает
            user = User()
            form.populate_obj(user)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('login'))
        else:
            print(form.errors)
    return render_template('user_form.html', form=form)
#
#
def login():
    form = UserForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first() # Метод first() возвр первый элемент из списка
            if user and user.password_check(form.password.data):
                login_user(user)
                return redirect(url_for('index'))

        else:
            print(form.errors)
    return render_template('user_form.html', form=form)



# def logout():
#     pass
