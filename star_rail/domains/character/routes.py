import json

from flask import Blueprint
from werkzeug.exceptions import abort

from star_rail.py.models.character import Character


###########################
# Helper functions
###########################
def get_dict_results_from_query(query):
  return [entity.to_dict() for entity in query]


###########################
# Handler functions
###########################
def get_all_characters():
  return get_dict_results_from_query(Character.query())
  

def get_character_by_name(name):
  return get_dict_results_from_query(Character.query_by_name(name))


def get_character_by_combat_type(combat_type):
  return get_dict_results_from_query(Character.query_by_combat_type(combat_type))

def get_character_by_path(path):
  return get_dict_results_from_query(Character.query_by_path(path))


# Factory to create the router w/ populated routes
def create_charcter_router():
  bp = Blueprint('character', __name__)

  bp.route('/all')(get_all_characters)
  bp.route('/name/<string:name>')(get_character_by_name)
  bp.route('/combat_type/<string:combat_type>')(get_character_by_combat_type)
  bp.route('/path/<string:path>')(get_character_by_path)

  return bp
