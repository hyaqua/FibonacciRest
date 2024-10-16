from flask import Flask, render_template, request

def fibonacci(n):
    if n <= 1:
        return 0 if n == 0 else 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def create_app():
    app = Flask(__name__)
    @app.route('/<num>', methods=['GET'])
    def return_fibonacci_number(num):
        # We check if the passed number is a number, if it is we convert it to an integer
        if str.isdigit(num):
            num = int(num)
        # If not then we return that the request body must be a number
        else:
            return "Request Body must be an integer", 400

        return str(fibonacci(num)), 200

    return app