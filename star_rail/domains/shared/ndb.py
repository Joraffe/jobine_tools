from google.cloud import ndb


def create_client():
  client = ndb.Client()
  return client
