import json

from flask import (
  Blueprint,
  Response,
)
from google.cloud import ndb

from domains.star_rail.models.character import Character


DOMAIN_NAME = 'star-rail-character-api'


def get_all_characters():
  client = ndb.Client()
  characters = []

  with client.context():
    characters = [c.to_dict() for c in Character.all()]

  return Response(json.dumps(characters), mimetype='application/json')


def create_character_api_router():
  api_bp = Blueprint(DOMAIN_NAME, __name__, url_prefix='/api')

  api_bp.route('/all')(get_all_characters)

  return api_bp
