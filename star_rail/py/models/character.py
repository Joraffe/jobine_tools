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
