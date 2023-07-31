from flask import Blueprint

from domains.shared.resources import (
  create_shared_blueprint,
  index_factory,
)


DOMAIN_NAME = 'home'


def create_home_router():
  home_bp = Blueprint(DOMAIN_NAME, __name__)
  home_bp.register_blueprint(create_shared_blueprint())

  index = index_factory(domain=DOMAIN_NAME)
  home_bp.route('/')(index)
  home_bp.route('/about')(index)

  return home_bp
