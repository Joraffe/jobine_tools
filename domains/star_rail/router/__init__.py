from flask import Blueprint

from domains.shared.resources import (
  create_shared_blueprint,
  index_factory,
)
from domains.star_rail.router.character import create_character_router


DOMAIN_NAME = 'star-rail'


def create():
  star_rail_bp = Blueprint(DOMAIN_NAME, __name__, url_prefix='/star-rail')

  star_rail_bp.register_blueprint(create_shared_blueprint())
  star_rail_bp.route('/')(index_factory(domain=DOMAIN_NAME))

  star_rail_bp.register_blueprint(create_character_router(parent_domain=DOMAIN_NAME))
  
  return star_rail_bp
