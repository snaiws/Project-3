from flask import Blueprint, render_template

result2_bp = Blueprint('result2', __name__)

@result2_bp.route('/result2')
def index():
    



    
    return render_template('result2.html', cType_list=list)