import functools

from flask import (
    Blueprint, g, request
)

from thesisweb.db import get_db


bp = Blueprint('api', __name__, url_prefix='/api')


@bp.route('/record')
def record():
    person = request.args.get('person', 'none')
    if person == 'none':
        return 'Skip'

    db = get_db()
    status = db.execute('SELECT on_off FROM record_status').fetchone()
    if status is None or not status['on_off']:
        return 'Off'

    db.execute('REPLACE INTO persons (person) VALUES (?)', (person,))
    db.commit()
    return 'Recorded'


@bp.route('/query')
def query():
    db = get_db()

    db.execute('UPDATE record_status SET on_off = 1')
    db.commit()

    person = db.execute('SELECT person FROM persons ORDER BY id DESC LIMIT 1').fetchone()
    if person is None:
        return 'none'

    name = person['person']
    db.execute('DELETE FROM persons')
    db.commit()

    db.execute('UPDATE record_status SET on_off = 0')
    db.commit()

    return name
