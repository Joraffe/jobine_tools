import os

from flask import Blueprint, render_template

from star_rail.domains.shared.resources import (
  INDEX_TEMPLATE_PATH,
  create_shared_blueprint
)


def home():
  return render_template(INDEX_TEMPLATE_PATH, domain='home')


def create_home_router():
  home_bp = Blueprint('home', __name__)
  home_bp.register_blueprint(create_shared_blueprint())

  home_bp.route('/')(home)

  return home_bp
