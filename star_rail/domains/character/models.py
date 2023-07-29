from google.cloud import ndb

COMBAT_TYPES = [
  'Quantum',
  'Physical',
  'Fire',
  'Ice',
  'Lightning',
  'Wind',
  'Imaginary',
]

PATHS = [
  'Hunt',
  'Destruction',
  'Erudition',
  'Harmony',
  'Nihility',
  'Preservation',
  'Abundance',
]


class Character(ndb.Model):
  name = ndb.StringProperty(indexed=True)
  combat_type = ndb.StringProperty(indexed=True, choices=COMBAT_TYPES)
  path = ndb.StringProperty(indexed=True, choices=PATHS)

  @classmethod
  def query_by_name(cls, name):
    return cls.query().filter(cls.name == name)
  
  @classmethod
  def query_by_combat_type(cls, combat_type):
    return cls.query().filter(cls.combat_type == combat_type)

  @classmethod
  def query_by_path(cls, path):
    return cls.query().filter(cls.path == path)
