from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Налаштування бази даних
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://avnadmin:AVNS_O3z9kbbw2LFc1tKyV82@pg-35e910ad-istu-00f2.b.aivencloud.com:17636/defaultdb?sslmode=require'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    
    with app.app_context():
        from .routes import api_bp
        app.register_blueprint(api_bp)
        
        # Ініціалізація бази даних
        db.create_all()
    
    return app
