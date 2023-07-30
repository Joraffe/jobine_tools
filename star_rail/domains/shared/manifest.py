import json
import os


RESOURCE_MANIFEST_PATH = os.path.join(os.path.dirname(__file__), 'static/manifest.json')


def static_rp(name):
  with open(RESOURCE_MANIFEST_PATH, 'r') as f:
    resource_manifest = json.loads(f.read())

  return resource_manifest[name]['file']
