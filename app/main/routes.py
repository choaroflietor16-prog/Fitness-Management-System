from flask import Blueprint, render_template
from flask_login import login_required, current_user

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    return render_template('main/index.html')


@main_bp.route('/dashboard')
@login_required
def dashboard():
    # Milestone 2+ will branch this into trainer/client dashboards.
    return render_template('main/dashboard.html', user=current_user)
