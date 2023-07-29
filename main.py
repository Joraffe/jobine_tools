import datetime

from flask import Flask, render_template
from google.cloud import datastore


datastore_client = datastore.Client()
app = Flask(__name__)


def store_time(email, dt):
  entity = datastore.Entity(key=datastore_client.key("User", email, "visit"))
  entity.update({"timestamp": dt})

  datastore_client.put(entity)


def fetch_times(email, limit):
  ancestor = datastore_client.key("User", email)
  query = datastore_client.query(kind="visit", ancestor=ancestor)
  query.order = ["-timestamp"]

  times = query.fetch(limit=limit)

  return times


@app.route("/")
def root():
  return render_template("index.html")


if __name__ == "__main__":
  # This is used when running locally only. When deploying to Google App
  # Engine, a webserver process such as Gunicorn will serve the app. This
  # can be configured by adding an `entrypoint` to app.yaml.
  # Flask's development server will automatically serve static files in
  # the "static" directory. See:
  # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
  # App Engine itself will serve those files as configured in app.yaml.
  app.run(host="127.0.0.1", port=8080, debug=True)
