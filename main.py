from flask import Flask, render_template, request

def fibonacci(n):
    if n <= 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def create_app():
    app = Flask(__name__)