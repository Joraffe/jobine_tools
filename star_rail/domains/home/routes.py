import os

from flask import Blueprint, render_template


def home():
  return render_template('home/index.html')


def create_home_router():
  home_bp = Blueprint(
    'home',
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/public'
  )

  home_bp.route('/')(home)

  return home_bp
