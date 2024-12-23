from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Налаштування бази даних
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://<username>:<password>@<host>:<port>/<database>'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    
    with app.app_context():
        from .routes import api_bp
        app.register_blueprint(api_bp)
        
        # Ініціалізація бази даних
        db.create_all()
    
    return app
