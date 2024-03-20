from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['SECRET_KEY'] = 'diflenchahfldjfenbuhsfadsfdnhacpfasdyvyitybanxcnxmzfdas h va'

    from .views import views
    from .actions import actions
    from .rakitra import rakitra
    from .pret import pret
    # Les prefix a utiliser pour acceder au url dans ces fichier
    app.register_blueprint(views,url_prefix="/")
    app.register_blueprint(actions,url_prefix="/actions")
    app.register_blueprint(rakitra,url_prefix="/rakitra")
    app.register_blueprint(pret,url_prefix="/pret")
    return app