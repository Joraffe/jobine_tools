from flask import Blueprint

from domains.shared.resources import (
  create_shared_blueprint,
  index_factory,
)


DOMAIN_NAME = 'home'


def create():
  star_rail_bp = Blueprint(DOMAIN_NAME, __name__)

  star_rail_bp.register_blueprint(create_shared_blueprint())
  star_rail_bp.route('/')(index_factory(domain=DOMAIN_NAME))
  
  return star_rail_bp
