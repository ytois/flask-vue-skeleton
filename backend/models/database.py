from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def init_db(app):
    SQLALCHEMY_DATABASE_URI = \
        'postgresql://{user}:{passwd}@{host}:{port}/{db}'.format(
            user=app.config['DB_USER'],
            passwd=app.config['DB_PASSWORD'],
            host=app.config['DB_HOST'],
            port=app.config['DB_PORT'],
            db=app.config['DB_NAME'],
        )
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    db.init_app(app)
