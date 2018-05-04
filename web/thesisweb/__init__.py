import os
from flask import Flask
from datetime import timedelta


def create_app(*args, **kwargs):
    app = Flask(__name__, instance_relative_config=True, static_url_path='/static')
    app.debug=True
    
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'thesis.sqlite'),
    )

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.config.from_pyfile('config.py', silent=True)
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(seconds=1)
    
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    from thesisweb import db
    db.init_app(app)

    from thesisweb import page
    from thesisweb import api
    app.register_blueprint(page.bp)
    app.register_blueprint(api.bp)

    return app
