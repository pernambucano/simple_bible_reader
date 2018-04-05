from flask import Flask

mapp = Flask(__name__)

@mapp.route('/')
def main_page():
    return "Salmos"
