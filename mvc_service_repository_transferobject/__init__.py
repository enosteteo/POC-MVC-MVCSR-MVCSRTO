from flask import Flask
from flask_login import LoginManager

from config import Config
from mvc_service_repository_transferobject.extensions import db


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_mapping(config_class.config)

    # flask extensions
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from mvc_service_repository_transferobject.users.model import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # blueprints
    from mvc_service_repository_transferobject.main import bp as main_bp

    app.register_blueprint(main_bp)

    from mvc_service_repository_transferobject.users import bp as users_bp

    app.register_blueprint(users_bp, url_prefix='/users')

    from mvc_service_repository_transferobject.tasks import bp as tasks_bp

    app.register_blueprint(tasks_bp, url_prefix='/tasks')

    from mvc_service_repository_transferobject.auth import bp as auth_bp

    app.register_blueprint(auth_bp, url_prefix='/auth')

    @app.route('/test/')
    def test():
        return '<h1>Test Page</h1>'

    with app.app_context():
        db.create_all()

    return app
