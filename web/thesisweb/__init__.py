import os
from flask import Flask


def create_app(*args, **kwargs):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'thesis.sqlite'),
    )

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.config.from_pyfile('config.py', silent=True)

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
