from flask import Blueprint

from domains.shared.resources import create_index_blueprint


DOMAIN_NAME = 'star-rail-character'


def create_character_router(parent_domain=''):
  bp = create_index_blueprint(
    domain=DOMAIN_NAME,
    parent_domain=parent_domain,
    url_prefix='/character',
  )

  return bp
