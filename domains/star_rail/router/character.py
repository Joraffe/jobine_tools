from flask import Blueprint

from domains.shared.resources import (
  create_shared_blueprint,
  index_factory,
)
from domains.star_rail.router.character_api import (
  create_character_api_router
)


DOMAIN_NAME = 'star-rail-character'


def create_character_router(parent_domain=None):
  character_bp = Blueprint(DOMAIN_NAME, __name__, url_prefix='/character')
  character_bp.register_blueprint(create_shared_blueprint())

  character_bp.route('/')(index_factory(domain=DOMAIN_NAME, parent_domain=parent_domain))

  # Routes under /character/api
  character_bp.register_blueprint(create_character_api_router())

  return character_bp
