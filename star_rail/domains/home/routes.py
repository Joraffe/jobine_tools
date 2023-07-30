import os

from flask import Blueprint

from star_rail.domains.shared.resources import (
  create_shared_blueprint,
  index_factory,
)


def create_home_router():
  home_bp = Blueprint('home', __name__)
  home_bp.register_blueprint(create_shared_blueprint())

  index = index_factory(domain='home')
  home_bp.route('/')(index)
  home_bp.route('/about')(index)

  return home_bp
