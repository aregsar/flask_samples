from flask import Flask
app = Flask(__name__)

from app.configs.settings import Settings
app.config.from_object(Settings)

from app.configs.blueprints import register_blueprints
register_blueprints(app)

print app.url_map
