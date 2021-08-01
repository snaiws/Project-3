import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from flask_migrate import Migrate

CSV_FILEPATH = os.path.join(os.getcwd(), __name__, 'users.csv') 
TMP_FILEPATH = os.path.join(os.getcwd(), __name__, 'tmp.csv') 
db = SQLAlchemy()
#migrate = Migrate()

def create_app():
    app = Flask(__name__)
    
    from p3_app.routes.main import main_bp
    from p3_app.routes.result1 import result1_bp
    from p3_app.routes.result2 import result2_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(result1_bp)    
    app.register_blueprint(result2_bp)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
