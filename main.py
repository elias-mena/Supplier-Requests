from flask import Flask, request, make_response, redirect, render_template
from apps import create_app

app = create_app()

if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
