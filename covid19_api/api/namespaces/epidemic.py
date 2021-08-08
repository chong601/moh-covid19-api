from flask_restx import Namespace, Resource, fields, abort
from flask_sqlalchemy import Pagination
from sqlalchemy import func
from covid19_api.db_model.sqlalchemy_models import CasesMalaysia
from covid19_api.api import db

api = Namespace('epidemic', 'Epidemic data')

cases_malaysia = api.model('cases_malaysia', {
    'row_id': fields.Integer(title='Row ID', description='ID of the row', example='1'),
    'row_version': fields.Integer(title='Row version', description='The version of the row.', example='1'),
    'date': fields.Date(title='Date', example='2021-01-01'),
    'cases_new': fields.Integer(title='New cases'),
    'cluster_import': fields.Integer(title='Import new cases (not available with row_version=1)'),
    'cluster_religious': fields.Integer(title='Religious new cases (not available with row_version=1)'),
    'cluster_community': fields.Integer(title='Community new cases (not available with row_version=1)'),
    'cluster_highRisk': fields.Integer(title='High-risk new cases (not available with row_version=1)'),
    'cluster_education': fields.Integer(title='Education new cases (not available with row_version=1)'),
    'cluster_detentionCentre': fields.Integer(title='Detention centre new cases (not available with row_version=1)'),
    'cluster_workplace': fields.Integer(title='Workplace new cases (not available with row_version=1)')
})

pagination_parser = api.parser()
pagination_parser.add_argument('page', location='args', help='Page number', type=int)
pagination_parser.add_argument('size', location='args', help='Items per page', type=int)


@api.route('/cases_malaysia')
class CasesMalaysiaWithPagination(Resource):

    @api.expect(pagination_parser)
    @api.marshal_with(cases_malaysia, as_list=True, skip_none=True)
    def get(self):
        args: dict = pagination_parser.parse_args()
        page = args.get('page') or 1
        size = args.get('size') or 7

        date_subquery = db.session.query(CasesMalaysia.date)
        query = db.session.query(CasesMalaysia)

        if not (args['page'] or args['size']):
            date_subquery = date_subquery.order_by(CasesMalaysia.date.desc()).limit(7)
            query = query.filter(CasesMalaysia.date.in_(date_subquery)).order_by(CasesMalaysia.date)

        result:Pagination = query.paginate(page, size, error_out=False)
        print(result.query)
        if result.items:
            return result.items
        abort(404, f'Invalid page number {page}. Valid page numbers are between 1 to {result.pages}')


@api.route('/cases_malaysia/<string:date>')
class CasesMalaysiaByDate(Resource):

    @api.marshal_with(cases_malaysia, skip_none=True)
    def get(self, date):
        query = db.session.query(CasesMalaysia).filter(CasesMalaysia.date == date)
        if db.session.query(query.exists()).scalar():
            result = query.first()
            return result
        abort(404, error=f"Date '{date}' is not found in database.")
