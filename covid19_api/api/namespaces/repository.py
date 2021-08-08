from flask_restx import Namespace, Resource, fields, abort
from covid19_api.db_model.sqlalchemy_models import RepositoryUpdateStatus
from covid19_api.api import db

api = Namespace('repository', 'Repository details')

repository = api.model('repository', {
    'repository_id': fields.String(title='Repository UUID', description='UUID for the repository name'),
    'repository_name': fields.String(title='Repository name'),
    'repository_category': fields.String(title='Repository category'),
    'last_update': fields.DateTime(title='Last update time'),
    'repository_hash': fields.String(title='SHA256 hash of the repository CSV file')
})

error = api.model('error_message', {
    'error': fields.String(title='Error message', example="Repository name 'nonexistant_repository' doesn't exist")
})


@api.route('/')
class RepositoryFullDetails(Resource):

    @api.marshal_with(repository, as_list=True)
    def get(self):
        return db.session.query(RepositoryUpdateStatus).all()


@api.route('/<string:repository_name>')
class RepositoryDetailByRepositoryName(Resource):

    @api.marshal_with(repository)
    def get(self, repository_name):
        query = db.session.query(RepositoryUpdateStatus).filter(RepositoryUpdateStatus.repository_name == repository_name)
        if db.session.query(query.exists()).scalar():
            return query.first()
        abort(404, error=f"Repository name '{repository_name}' doesn't exist")