from flask import Flask, render_template

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')