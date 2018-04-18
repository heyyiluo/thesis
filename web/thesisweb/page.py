import functools

from flask import (
    Blueprint, g, render_template, request
)

from thesisweb.db import get_db


bp = Blueprint('page', __name__)


@bp.route('/page1')
def page1():
    return render_template('page1.html')


@bp.route('/page2')
def page2():
    person = request.args.get('person', 'none')
    return render_template('page2.html', person=person)
