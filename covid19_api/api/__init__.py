from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restx import Api


# Results per page
MAX_RESULTS_PER_PAGE = 100

# Create a new Flask instance
app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://chong601:chong601@localhost/moh_covid19_api'
# Disable JSON key ordering.
# Fuck this took fucking forever to figure out.
# This setting is completely cosmetic, but used because most API put keys on top
app.config['JSON_SORT_KEYS'] = False
# Inform Flask-SQLAlchemy to disable modification tracking
# We do not rely on events so it's probably safe to disable it.
# This shouldn't cause issues, but do raise a bug issue if weird things occur in production!
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Flask-RESTX: Disable X-Fields entry on Swagger
app.config['RESTX_MASK_SWAGGER'] = False
# Remove default message
app.config['ERROR_INCLUDE_MESSAGE'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import database models
from covid19_api.db_model import sqlalchemy_models

# Import namespaces
from .namespaces.epidemic import api as epidemic_api
from .namespaces.repository import api as repository_api
from .namespaces.mysejahtera import api as mysejahtera_api
from .namespaces.static import api as static_api
from .namespaces.registration import api as vaxreg_api
from .namespaces.vaccination import api as vax_api

# Create alpha blueprint
alpha_blueprint = Blueprint('api', __name__, url_prefix='/api/alpha')

# Create Flask-RestX Api
api = Api(alpha_blueprint, title='MOH COVID-19 REST API', version='0.2-alpha', description='Swagger interface for MOH COVID-19 REST API', doc='/ui/', ordered=True)

# Add namespaces
api.add_namespace(epidemic_api)
api.add_namespace(repository_api)
api.add_namespace(mysejahtera_api)
api.add_namespace(static_api)
api.add_namespace(vaxreg_api)
api.add_namespace(vax_api)

# Register blueprint
app.register_blueprint(alpha_blueprint)
