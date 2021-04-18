from flask import Blueprint

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/hello')
def hello_pybo():
    return 'Hello 다시'


@bp.route('/')
def index():
    return 'Hello, Pybo 좋아 지금부터 !!!'
