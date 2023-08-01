from flask import Blueprint

from domains.star_rail.routers.index import create_index_router
from domains.star_rail.routers.character import create_character_router


DOMAIN_NAME = 'star-rail'


def create_star_rail_router():
  star_rail_bp = Blueprint(DOMAIN_NAME, __name__, url_prefix='/star-rail')

  star_rail_bp.register_blueprint(create_index_router(parent_domain=DOMAIN_NAME))
  star_rail_bp.register_blueprint(create_character_router(parent_domain=DOMAIN_NAME))
  
  return star_rail_bp
