from flask import Blueprint, redirect


Login = Blueprint('login', __name__)
Logout = Blueprint('logout', __name__)


@Login.route('/')
def index():
    return 'login'


@Login.route('/', methods=['POST'])
def login():
    return redirect('/')


@Logout.route('/')
def logout():
    return redirect('/')
