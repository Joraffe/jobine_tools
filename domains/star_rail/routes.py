from flask import Blueprint

from domains.shared.resources import (
  create_shared_blueprint,
  index_factory,
)


DOMAIN_NAME = 'star_rail'


def create_star_rail_router():
  star_rail_bp = Blueprint(DOMAIN_NAME, __name__, url_prefix='/star_rail')
  star_rail_bp.register_blueprint(create_shared_blueprint())

  index = index_factory(domain=DOMAIN_NAME)
  star_rail_bp.route('/')(index)
  
  return star_rail_bp
