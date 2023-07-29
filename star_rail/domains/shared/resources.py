from flask import Blueprint

INDEX_TEMPLATE_PATH = 'shared/index.html'


def create_shared_blueprint():
  return Blueprint(
    'shared',
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/public',
  )
