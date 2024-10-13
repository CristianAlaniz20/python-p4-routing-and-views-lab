#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route('/print/<string>')
def print_string(string):
    print(string)
    return(string)

@app.route('/count/<number>')
def count(number):
    string_list = [str(num) for num in range(int(number))]
    numbers_string = ""
    for text in string_list:
        numbers_string += f"{text}\n"
    return numbers_string

@app.route('/math/<num1>/<operation>/<num2>')
def math(num1, operation, num2):
    operation_result = None 
    number1 = int(num1)
    number2 = int(num2)
    if operation == "+":
        operation_result = number1 + number2
    elif operation == "-":
        operation_result = number1 - number2
    elif operation == "*":
        operation_result = number1 * number2
    elif operation == "div":
        operation_result = number1 / number2
    elif operation == "%":
        operation_result = number1 % number2
    else:
        operation_result = "Could not perform operation"
    return str(operation_result)