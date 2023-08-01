from flask import Blueprint

from domains.home.routers.index import create_index_router


DOMAIN_NAME = 'home'


def create_home_router():
  home_bp = Blueprint(DOMAIN_NAME, __name__)

  home_bp.register_blueprint(create_index_router(parent_domain=DOMAIN_NAME))

  return home_bp
