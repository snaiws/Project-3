import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import config

CSV_FILEPATH = os.path.join(os.getcwd(), __name__, 'users.csv') 
TMP_FILEPATH = os.path.join(os.getcwd(), __name__, 'tmp.csv') 
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    
    from app.pages.main import main_bp
    from app.pages.secondpage import second_bp
    from app.pages.thirdpage import third_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(user_bp, url_prefix='/api')    
    app.register_blueprint(user_bp, url_prefix='/api')

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
