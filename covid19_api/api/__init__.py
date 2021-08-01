from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


# Results per page
MAX_RESULTS_PER_PAGE = 100

# Create a new Flask instance
app = Flask(__name__)


# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://chong601:chong601@10.102.7.97/moh_covid19_api'
# Disable JSON key ordering.
# Fuck this took fucking forever to figure out.
# This setting is completely cosmetic, but used because most API put keys on top
app.config['JSON_SORT_KEYS'] = False
# Inform Flask-SQLAlchemy to disable modification tracking
# We do not rely on events so it's probably safe to disable it.
# This shouldn't cause issues, but do raise a bug issue if weird things occur in production!
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# Database
from ..db_model import sqlalchemy_models
