from google.cloud import ndb


COMBAT_TYPES = [
  'Physical',
  'Fire',
  'Ice',
  'Lightning',
  'Wind',
  'Quantum',
  'Imaginary',
]
PATHS = [
  'Abundance',
  'Destruction',
  'Erudition',
  'Harmony',
  'Hunt',
  'Nihility',
  'Preservation',
]

class Character(ndb.Model):
  uid = ndb.ComputedProperty(lambda self: self.key.id(), indexed=False)

  name = ndb.StringProperty()
  combat_type = ndb.StringProperty(choices=COMBAT_TYPES)
  path = ndb.StringProperty(choices=PATHS)
  rarity = ndb.IntegerProperty(choices=[4, 5])


  @classmethod
  def all(cls):
    query = cls.query()
    return [character for character in query]
