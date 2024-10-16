from flask import Flask, render_template, request

def fibonacci(n):
    if n <= 1:
        return 0 if n == 0 else 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def create_app():
    app = Flask(__name__)
    @app.route('/', methods=['GET'])
    def return_fibonacci_number():
        req_body = request.get_data().decode('utf-8')
        # We get the request body from the user and decode it from a byte string to a normal string

        if req_body.isdigit():
            req_body = int(req_body)
        # if an int is parsable from the request body we get it
        else:
            return "Request Body must be an integer", 400
        # If not then we return that the request body must be a number

        # If everything went correctly we run the fibonacci function and return the result
        return str(fibonacci(req_body)), 200

    return app