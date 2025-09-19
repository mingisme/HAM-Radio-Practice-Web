from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return "Hello, World" 

@main.route('/about')
def about():
    return render_template('about.html')  # Assuming an about.html template will be created later.