import pymysql
from flask import Flask, request, jsonify

from config import (
    HOST,
    DB_USER,
    DB_NAME,
    DB_HOST,
    DB_PASSWORD,
    REQUEST_METHODS,
)
from queries import INSERT_QUERY

# создаем приложение Flask
app = Flask(__name__)

# настраиваем соединение с БД MySQL
db = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME)


@app.route('/', methods=[*REQUEST_METHODS.values()])
def index():
    if request.method == REQUEST_METHODS['post']:
        # handle the POST request
        first_name = request.form.get('name')
        last_name = request.form.get('last_name')

        # сохраняем данные в БД
        cursor = db.cursor()
        cursor.execute(INSERT_QUERY, (first_name, last_name))
        db.commit()
        cursor.close()

        # возвращаем ответ клиенту
        response = {'status': 'success', 'message': 'User added to database'}

        return jsonify(response)

    return '''<h1>Hello world!</h1>'''


if __name__ == '__main__':
    app.run(host=HOST, port=443)
