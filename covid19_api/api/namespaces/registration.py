from flask_restx import Namespace, Resource, fields, abort
from flask_sqlalchemy import Pagination
from covid19_api.db_model.sqlalchemy_models import VaxRegMalaysia, VaxRegState
from covid19_api.api import db

api = Namespace('registration', 'COVID-19 vaccine registration data')

vaxreg_malaysia = api.model('vaxreg_malaysia', {
    'row_id': fields.Integer(title='Row ID'),
    'row_version': fields.Integer(title='Row version'),
    'date': fields.Date(title='Date'),
    'state': fields.String(title='State name', description='Defaults to Malaysia'),
    'total': fields.Integer(title='Number of unique registrants'),
    'phase2': fields.Integer(title='Number of unique individuals eligible for Phase 2'),
    'mysj': fields.Integer(title='Number of individuals registered via MySejahtera'),
    'call': fields.Integer(title='Number of individuals registered via the call centre'),
    'web': fields.Integer(title='Number of individuals registered via the website'),
    'children': fields.Integer(title='Number of individuals below 18'),
    'elderly': fields.Integer(title='Number of individuals aged 60 and above'),
    'comorb': fields.Integer(title='Number of individuals self-declaring at least 1 comorbidity'),
    'oku': fields.Integer(title='Number of individuals self-declaring as OKU')
})

vaxreg_state = api.model('vaxreg_state', {
    'row_id': fields.Integer(title='Row ID'),
    'row_version': fields.Integer(title='Row version'),
    'date': fields.Date(title='Date'),
    'state': fields.String(title='State name'),
    'total': fields.Integer(title='Number of unique registrants'),
    'phase2': fields.Integer(title='Number of unique individuals eligible for Phase 2'),
    'mysj': fields.Integer(title='Number of individuals registered via MySejahtera'),
    'call': fields.Integer(title='Number of individuals registered via the call centre'),
    'web': fields.Integer(title='Number of individuals registered via the website'),
    'children': fields.Integer(title='Number of individuals below 18'),
    'elderly': fields.Integer(title='Number of individuals aged 60 and above'),
    'comorb': fields.Integer(title='Number of individuals self-declaring at least 1 comorbidity'),
    'oku': fields.Integer(title='Number of individuals self-declaring as OKU')
})

pagination_parser = api.parser()
pagination_parser.add_argument('page', location='args', help='Page number', type=int)
pagination_parser.add_argument('size', location='args', help='Items per page', type=int)


@api.route('/vaxreg_malaysia')
class VaxRegMalaysiaWithPagination(Resource):

    @api.expect(pagination_parser)
    @api.marshal_with(vaxreg_malaysia, as_list=True, skip_none=True)
    def get(self):
        args: dict = pagination_parser.parse_args()
        page = args.get('page') or 1
        size = args.get('size') or 7

        date_subquery = db.session.query(VaxRegMalaysia.date)
        query = db.session.query(VaxRegMalaysia)

        if not (args['page'] or args['size']):
            date_subquery = date_subquery.order_by(VaxRegMalaysia.date.desc()).limit(7)
            query = query.filter(VaxRegMalaysia.date.in_(date_subquery)).order_by(VaxRegMalaysia.date)

        result:Pagination = query.paginate(page, size, error_out=False)
        if result.items:
            return result.items
        abort(404, f"Invalid page number '{page}'. Valid page numbers are between 1 to {result.pages} for size of {result.per_page} item(s)")


@api.route('/vaxreg_malaysia/<string:date>')
class VaxRegMalaysiaByDate(Resource):

    @api.marshal_with(vaxreg_malaysia, skip_none=True)
    def get(self, date):
        query = db.session.query(VaxRegMalaysia).filter(VaxRegMalaysia.date == date)
        if db.session.query(query.exists()).scalar():
            result = query.first()
            return result
        abort(404, error=f"Date '{date}' is not found in database.")


@api.route('/vaxreg_state')
class VaxRegStateWithPagination(Resource):

    @api.expect(pagination_parser)
    @api.marshal_with(vaxreg_state, as_list=True, skip_none=True)
    def get(self):
        args: dict = pagination_parser.parse_args()
        page = args.get('page') or 1
        # We don't use size against the final result, instead on the number of dates
        size = args.get('size') or 7

        date_subquery = db.session.query(VaxRegState.date).group_by(VaxRegState.date).order_by(VaxRegState.date)
        query = db.session.query(VaxRegState)

        if not (args['page'] or args['size']):
            date_subquery = date_subquery.order_by(VaxRegState.date.desc()).limit(7)
            query = query.filter(VaxRegState.date.in_(date_subquery)).order_by(VaxRegState.date, VaxRegState.state)
            return query.all()

        # Handle date bullshit first, then deal with actual data

        # Get dates based on the pagination values
        date_result: Pagination = date_subquery.paginate(page, size, error_out=False)
        # Get all dates returned by the pagination
        dates = [date[0] for date in date_result.items]

        # Future project: implement pagination logic and expose it to end user
        attr = {a: getattr(date_result, a) for a in dir(date_result) if not a.startswith('__') and not callable(getattr(date_result, a))}

        if 'query' in attr:
            compile = attr['query'].statement.compile()
            attr.update({'query_string': compile.string})
            attr.update({'query_param': compile.params})
            del attr['query']

        # Query the database with the rows selected from pagination
        # Think of this as a subquery-ish method, except that the query is done separately like:
        # 
        # pagination_result = select date from vaxreg_state group by date order by date offset (SELECT (page_number - 1) * size) limit size;
        # query = select * from vaxreg_state where date in (pagination.result);
        query = query.filter(VaxRegState.date.in_(dates)).order_by(VaxRegState.date, VaxRegState.state)
        result = query.all()

        if result:
            return result
        abort(404, f"Invalid page number '{page}'. Valid page numbers are between 1 to {date_result.pages} for size of {date_result.per_page} item(s)")


@api.route('/vaxreg_state/<string:state>')
class VaxRegStateByStateWithPagination(Resource):

    @api.expect(pagination_parser)
    @api.marshal_with(vaxreg_state, as_list=True, skip_none=True)
    def get(self, state=None):
        args: dict = pagination_parser.parse_args()
        page = args.get('page') or 1
        size = args.get('size') or 7

        date_subquery = db.session.query(VaxRegState.date).group_by(VaxRegState.date)
        query = db.session.query(VaxRegState)

        if state != 'all':
            state_exists = db.session.query(db.session.query(VaxRegState.state).filter(VaxRegState.state.ilike(f'%{state}')).exists()).scalar()
            if state_exists:
                query = query.filter(VaxRegState.state.ilike(f'%{state}'))
            else:
                abort(404, f"State name '{state}' not found in database")

        if not (args['page'] or args['size']):
            date_subquery = date_subquery.order_by(VaxRegState.date.desc()).limit(7)
            query = query.filter(VaxRegState.date.in_(date_subquery)).order_by(VaxRegState.date, VaxRegState.state)
            return query.all()

        # Handle date bullshit first, then deal with actual data
        # Get dates based on the pagination values

        date_subquery = date_subquery.order_by(VaxRegState.date)
        date_result: Pagination = date_subquery.paginate(page, size, error_out=False)
        # Get all dates returned by the pagination
        dates = [date[0] for date in date_result.items]

        # Future project: implement pagination logic and expose it to end user
        attr = {a: getattr(date_result, a) for a in dir(date_result) if not a.startswith('__') and not callable(getattr(date_result, a))}

        if 'query' in attr:
            compile = attr['query'].statement.compile()
            attr.update({'query_string': compile.string})
            attr.update({'query_param': compile.params})
            del attr['query']

        # Query the database with the rows selected from pagination
        # Think of this as a subquery-ish method, except that the query is done separately like:
        #
        # pagination_result = select date from hospital_by_state group by date order by date offset (SELECT (page_number - 1) * size) limit size;
        # query = select * from hospital_by_state where date in (pagination.result);
        query = query.filter(VaxRegState.date.in_(dates)).order_by(VaxRegState.date, VaxRegState.state)
        result = query.all()

        if result:
            return result
        abort(404, f"Invalid page number '{page}'. Valid page numbers are between 1 to {date_result.pages} for size of {date_result.per_page} item(s)")


@api.route('/vaxreg_state/<string:state>/<string:date>')
class VaxRegStateByStateByDateWithPagination(Resource):

    @api.marshal_with(vaxreg_state, skip_none=True)
    def get(self, state=None, date=None):
        query = db.session.query(VaxRegState)
        if state == 'all':
            query = query.filter(VaxRegState.date == date)
            return query.all()
        else:
            query = query.filter(VaxRegState.state.ilike(state), VaxRegState.date == date)
            if db.session.query(query.exists()).scalar():
                result = query.first()
                return result
        abort(404, error=f"State '{state}' with date '{date}' is not found in database.")
