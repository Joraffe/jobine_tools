from flask import Blueprint, send_from_directory

from star_rail.domains.shared.manifest import static_rp


INDEX_TEMPLATE_PATH = 'shared/index.html'


def create_shared_blueprint():
  shared_bp = Blueprint(
    'shared',
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/',
  )

  shared_bp.add_app_template_global(static_rp)

  return shared_bp
