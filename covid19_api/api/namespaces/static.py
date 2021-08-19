from flask_restx import Namespace, Resource, fields, abort
from flask_sqlalchemy import Pagination
from covid19_api.db_model.sqlalchemy_models import Population
from covid19_api.api import db

api = Namespace('static', 'Static data')

population = api.model('population', {
    'row_id': fields.Integer(title='Row ID', description='ID of the row'),
    'row_version': fields.Integer(title='Row version'),
    'state': fields.String(title='State name'),
    'idxs': fields.Integer(title='Index number'),
    'pop': fields.Integer(title='Total state population'),
    'pop_18': fields.Integer(title='Total state population ages >= 18'),
    'pop_60': fields.Integer(title='Total state population ages >= 60')
})

pagination_parser = api.parser()
pagination_parser.add_argument('page', location='args', help='Page number', type=int)
pagination_parser.add_argument('size', location='args', help='Items per page', type=int)


@api.route('/population')
class PopulationData(Resource):

    @api.marshal_with(population, as_list=True, skip_none=True)
    def get(self):
        """Get all state population data"""
        result = db.session.query(Population).all()
        if result:
            return result
        abort(404, error='No population data found')


@api.route('/population/<string:state>')
class PopulationDataByStateName(Resource):

    @api.marshal_with(population, skip_none=True)
    def get(self, state):
        """Get state population data by state name"""
        query = db.session.query(Population).filter(Population.state.ilike(f'%{state}'))
        if db.session.query(query.exists()).scalar():
            result = query.first()
            return result
        abort(404, error=f"State '{state}' is not found in database.")