from website.models import User
from flask import Blueprint, render_template


views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def home():
    
    return render_template('home.html', user={'is_authenticated': False})