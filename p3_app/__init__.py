import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from flask_migrate import Migrate

load_dotenv()
CSV_FILEPATH = os.path.join(os.getcwd(), __name__, './static/industrytable.csv')
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    #os.getenv('DATABASE_URL')

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app_db.db'
    db.init_app(app)
    migrate.init_app(app, db)
    
    from p3_app.routes.main import main_bp
    from p3_app.routes.result1 import result1_bp
    from p3_app.routes.result2 import result2_bp
    from p3_app.routes.dude import dude_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(result1_bp)    
    app.register_blueprint(result2_bp)
    app.register_blueprint(dude_bp)


    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
