from flask import (
  Blueprint,
  render_template,
  send_from_directory
)

from domains.shared.manifest import static_rp


def index_factory(domain=None):
  def index():
    return render_template('shared/index.html', domain=domain)

  return index


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


def create_index_blueprint(domain=None, parent_domain=None, url_prefix=None):
  bp = Blueprint(domain, __name__, url_prefix=url_prefix)
  bp.register_blueprint(create_shared_blueprint())

  index = index_factory(domain=f'{parent_domain}.{domain}')
  bp.route('/')(index)

  return bp
