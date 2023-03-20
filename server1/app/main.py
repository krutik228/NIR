from flask import Flask, request, jsonify
import pymysql

# создаем приложение Flask
app = Flask(__name__)

# настраиваем соединение с БД MySQL
db = pymysql.connect(host="localhost", user="admin", password="P@ssw0rd", database="names")


# обработчик POST-запросов
@app.route('/post', methods=['POST'])
def add_user():
    # получаем данные из тела запроса
    data = request.json
    first_name = data['first_name']
    last_name = data['last_name']

    # сохраняем данные в БД
    cursor = db.cursor()
    query = "INSERT INTO users (first_name, last_name) VALUES (%s, %s)"
    cursor.execute(query, (first_name, last_name))
    db.commit()
    cursor.close()

    # возвращаем ответ клиенту
    response = {'status': 'success', 'message': 'User added to database'}
    return jsonify(response)


if __name__ == '__main__':
    print('main py')
    app.run(host='0.0.0.0', port=443)
