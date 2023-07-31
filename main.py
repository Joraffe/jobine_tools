from flask import Flask

from domains.home.routes import create_home_router
from domains.star_rail.routes import create_star_rail_router


app = Flask(__name__)
app.register_blueprint(create_home_router())
app.register_blueprint(create_star_rail_router())


if __name__ == "__main__":
  # This is used when running locally only. When deploying to Google App
  # Engine, a webserver process such as Gunicorn will serve the app. This
  # can be configured by adding an `entrypoint` to app.yaml.
  # Flask's development server will automatically serve static files in
  # the "static" directory. See:
  # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
  # App Engine itself will serve those files as configured in app.yaml.
  app.run(host="127.0.0.1", port=8080, debug=True)
