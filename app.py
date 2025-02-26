from flask import Flask

app = Flask(__name__)


def add(a, b):
    return a + b


def sub(a, b):
    beta = b
    return a - b


def multiply(a, b):
    result = a * b
    return result


if __name__ == '__main__':
    app.run(debug=True)
