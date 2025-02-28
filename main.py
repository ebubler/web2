from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    id_astr = StringField('id астронавта', validators=[DataRequired()])
    password_astr = PasswordField('Пароль астронавта', validators=[DataRequired()])
    id_cap = StringField('id капитана', validators=[DataRequired()])
    password_cap = PasswordField('Пароль капитана', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Доступ')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

data = {
    "title": "Автоматический ответ",
    "surname": "Иванов",
    "name": "Иван",
    "education": "Высшее",
    "profession": "инженер-исследователь",
    "sex": "Мужик",
    "motivation": "Хочу помочь колонизации Марса!",
    "ready": "Да"
}

professions = [
    "инженер-исследователь",
    "пилот",
    "строитель",
    "экзобиолог",
    "врач",
    "инженер по терраформированию",
    "климатолог",
    "специалист по радиационной защите",
    "астрогеолог",
    "гляциолог"
]

@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)

@app.route('/training/<prof>')
def training(prof):
    if 'инженер' in prof.lower() or 'строитель' in prof.lower():
        header = "Инженерные тренажёры"
        image = "инженер.jpg"
        alt_text = "Схема расположения инженерных тренажёров"
    else:
        header = "Научные симуляторы"
        image = "наука.jpg"
        alt_text = "Схема расположения научных симуляторов"

    return render_template('training.html', header=header, image=image, alt_text=alt_text)

@app.route('/list_prof/<list_type>')
def list_prof(list_type):
    header = "Список профессий для миссии на Марс"

    return render_template(
        'list_prof.html',
        header=header,
        list_type=list_type,
        professions=professions
    )

@app.route('/answer')
@app.route('/auto_answer')
def auto_answer():
    return render_template('auto_answer.html', **data)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for('success'))
    return render_template('login.html', title='Авторизация', form=form)

@app.route('/success')
def success():
    return render_template('success.html', title='Успешный вход')

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')