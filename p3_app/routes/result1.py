from flask import Blueprint, render_template

result1_bp = Blueprint('result1', __name__)

@result1_bp.route('/result1')
def index():
    



    
    return render_template('result1.html', cType_list=list)