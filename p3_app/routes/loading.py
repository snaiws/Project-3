from flask import Blueprint, render_template

loading_bp = Blueprint('loading', __name__)

@loading_bp.route('/loading')
def index():
    



    
    return render_template('loading.html')