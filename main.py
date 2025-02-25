from flask import Flask, render_template

app = Flask(__name__)

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

@app.route('/')
@app.route('/index')
def index():
    title = "Главная страница"
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

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')