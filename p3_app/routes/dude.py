from flask import Blueprint, render_template

dude_bp = Blueprint('dude', __name__)

@dude_bp.route('/dude')
def index():
    



    
    return render_template('dude.html')