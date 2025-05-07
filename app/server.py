from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def echo_get():
    return 'Hello, send me something in a POST request!'

@app.route('/', methods=['POST'])
def echo_post():
    # Получаем данные из тела POST запроса
    data = request.data
    # Возвращаем полученные данные обратно в теле ответа
    return data

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)