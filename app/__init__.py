from flask import Flask, g
#

def app_register_blueprints(app):
    """
    Register all blueprints from here
    :param app: Flask App
    :return: None
    """
    from app.api import dominion

    # Register routes
    _blue_prints = [
        (dominion.blueprint.BP, True),
    ]
    for _bp, include, in _blue_prints:
        if include:
            app.register_blueprint(_bp)


def create_app():
    """
    create and configure the app
    """
    app = Flask(__name__)

    # app.config.from_pyfile('../config.py')
    from app.api.db.db import connect_db

    global db
    db = connect_db(app)

    app_register_blueprints(app)

    return app
