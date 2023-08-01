from flask import (
  Blueprint,
  render_template,
  send_from_directory
)

from domains.shared.manifest import static_rp


def index_factory(domain=None, parent_domain=None):
  if parent_domain:
    domain_prefix = f'{parent_domain}.{domain}'
  else:
    domain_prefix = f'{domain}'

  def index():
    return render_template('shared/index.html', domain_prefix=domain_prefix)

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
