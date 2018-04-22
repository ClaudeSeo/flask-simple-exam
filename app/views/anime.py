from flask import Blueprint, render_template

bp = Blueprint('anime', __name__, url_prefix='/anime')


@bp.route('', methods=('GET',))
def index():
    return render_template('anime/index.html')
