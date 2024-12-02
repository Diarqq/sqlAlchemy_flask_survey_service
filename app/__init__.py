from flask import Flask

def create_app():
    app = Flask(__name__)

    app.secret_key = 'sup'
    app.config['SESSION_TYPE'] = 'filesystem'

    from .views import init_app
    init_app(app)


    from .db import pg as pg_db
    pg_db.init_app(app)

    return app
