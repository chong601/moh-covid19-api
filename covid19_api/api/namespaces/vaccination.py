from flask_restx import Namespace, Resource, fields, abort
from flask_sqlalchemy import Pagination
from covid19_api.db_model.sqlalchemy_models import VaxMalaysia, VaxState
from covid19_api.api import db

api = Namespace('vaccination', 'COVID-19 vaccination data')

vax_malaysia = api.model('vax_malaysia', {
    'row_id': fields.Integer(title='Row ID'),
    'row_version': fields.Integer(title='Row version'),
    'date': fields.Date(title='Date'),
    'daily_partial': fields.Integer(title='1st doses (for double-dose vaccines) delivered between 0000 and 2359 on date'),
    'daily_full': fields.Integer(title='2nd doses (for single-dose vaccines) and 1-dose vaccines (e.g. Cansino) delivered between 0000 and 2359 on date.'),
    'daily': fields.Integer(title='Total daily delivered between 0000 and 2359 on date'),
    'cumul_partial': fields.Integer(title='Sum of cumulative partial doses delivered until row date'),
    'cumul_full': fields.Integer(title='Sum of cumulative full doses delivered until row date'),
    'cumul': fields.Integer(title='Total cumulative doses delivered until row date'),
    'pfizer1': fields.Integer(title='1st dose of PFizer vaccine delivered between 0000 and 2359 on date'),
    'pfizer2': fields.Integer(title='2nd dose of PFizer vaccine delivered between 0000 and 2359 on date'),
    'sinovac1': fields.Integer(title='1st dose of SinoVac vaccine delivered between 0000 and 2359 on date'),
    'sinovac2': fields.Integer(title='2nd dose of SinoVac vaccine delivered between 0000 and 2359 on date'),
    'astra1': fields.Integer(title='1st dose of AstraZeneca vaccine delivered between 0000 and 2359 on date'),
    'astra2': fields.Integer(title='2nd dose of AstraZeneca vaccine delivered between 0000 and 2359 on date'),
    'pending': fields.Integer(title='Doses delivered that are quarantined in VMS (Vaccine Management System)'),
})

vax_state = api.model('vax_state', {
    'row_id': fields.Integer(title='Row ID'),
    'row_version': fields.Integer(title='Row version'),
    'date': fields.Date(title='Date'),
    'state': fields.String(title='State name'),
    'daily_partial': fields.Integer(title='1st doses (for double-dose vaccines) delivered between 0000 and 2359 on date'),
    'daily_full': fields.Integer(title='2nd doses (for single-dose vaccines) and 1-dose vaccines (e.g. Cansino) delivered between 0000 and 2359 on date.'),
    'daily': fields.Integer(title='Total daily delivered between 0000 and 2359 on date'),
    'cumul_partial': fields.Integer(title='Sum of cumulative partial doses delivered until row date'),
    'cumul_full': fields.Integer(title='Sum of cumulative full doses delivered until row date'),
    'cumul': fields.Integer(title='Total cumulative doses delivered until row date'),
    'pfizer1': fields.Integer(title='1st dose of PFizer vaccine delivered between 0000 and 2359 on date'),
    'pfizer2': fields.Integer(title='2nd dose of PFizer vaccine delivered between 0000 and 2359 on date'),
    'sinovac1': fields.Integer(title='1st dose of SinoVac vaccine delivered between 0000 and 2359 on date'),
    'sinovac2': fields.Integer(title='2nd dose of SinoVac vaccine delivered between 0000 and 2359 on date'),
    'astra1': fields.Integer(title='1st dose of AstraZeneca vaccine delivered between 0000 and 2359 on date'),
    'astra2': fields.Integer(title='2nd dose of AstraZeneca vaccine delivered between 0000 and 2359 on date'),
    'pending': fields.Integer(title='Doses delivered that are quarantined in VMS (Vaccine Management System)'),
})

pagination_parser = api.parser()
pagination_parser.add_argument('page', location='args', help='Page number', type=int)
pagination_parser.add_argument('size', location='args', help='Items per page', type=int)


@api.route('/vax_malaysia')
class VaxMalaysiaWithPagination(Resource):

    @api.expect(pagination_parser)
    @api.marshal_with(vax_malaysia, as_list=True, skip_none=True)
    def get(self):
        """
        Get country-wide vaccination data with pagination support

        Defaults to vaccination data for the last 7 days sorted by date in ascending order.

        Size parameter is optional and defaults to 10.
        """
        args: dict = pagination_parser.parse_args()
        page = args.get('page') or 1
        size = args.get('size') or 7

        date_subquery = db.session.query(VaxMalaysia.date)
        query = db.session.query(VaxMalaysia)

        if not (args['page'] or args['size']):
            date_subquery = date_subquery.order_by(VaxMalaysia.date.desc()).limit(7)
            query = query.filter(VaxMalaysia.date.in_(date_subquery)).order_by(VaxMalaysia.date)

        result:Pagination = query.paginate(page, size, error_out=False)
        if result.items:
            return result.items
        abort(404, f"Invalid page number '{page}'. Valid page numbers are between 1 to {result.pages} for size of {result.per_page} item(s)")


@api.route('/vax_malaysia/<string:date>')
class VaxMalaysiaByDate(Resource):

    @api.marshal_with(vax_malaysia, skip_none=True)
    def get(self, date):
        """
        Get vaccination data by date

        Defaults to vaccination data for the last 7 days sorted by date in ascending order.
        Size parameter is optional and defaults to 10.
        """
        query = db.session.query(VaxMalaysia).filter(VaxMalaysia.date == date)
        if db.session.query(query.exists()).scalar():
            result = query.first()
            return result
        abort(404, error=f"Date '{date}' is not found in database.")


@api.route('/vax_state')
class VaxStateWithPagination(Resource):

    @api.expect(pagination_parser)
    @api.marshal_with(vax_state, as_list=True, skip_none=True)
    def get(self):
        """
        Get country-wide vaccination data with pagination support

        Defaults to vaccination data for the last 7 days sorted by date in ascending order.
        Size parameter is optional and defaults to 10.
        """
        args: dict = pagination_parser.parse_args()
        page = args.get('page') or 1
        # We don't use size against the final result, instead on the number of dates
        size = args.get('size') or 7

        date_subquery = db.session.query(VaxState.date).group_by(VaxState.date).order_by(VaxState.date)
        query = db.session.query(VaxState)

        if not (args['page'] or args['size']):
            date_subquery = date_subquery.order_by(VaxState.date.desc()).limit(7)
            query = query.filter(VaxState.date.in_(date_subquery)).order_by(VaxState.date, VaxState.state)
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
        # pagination_result = select date from vax_state group by date order by date offset (SELECT (page_number - 1) * size) limit size;
        # query = select * from vax_state where date in (pagination.result);
        query = query.filter(VaxState.date.in_(dates)).order_by(VaxState.date, VaxState.state)
        result = query.all()

        if result:
            return result
        abort(404, f"Invalid page number '{page}'. Valid page numbers are between 1 to {date_result.pages} for size of {date_result.per_page} item(s)")


@api.route('/vax_state/<string:state>')
class VaxStateByStateWithPagination(Resource):

    @api.expect(pagination_parser)
    @api.marshal_with(vax_state, as_list=True, skip_none=True)
    def get(self, state=None):
        """
        Get vaccination data by date

        Defaults to vaccination data for the last 7 days sorted by date in ascending order.
        Size parameter is optional and defaults to 10.
        """
        
        args: dict = pagination_parser.parse_args()
        page = args.get('page') or 1
        size = args.get('size') or 7

        date_subquery = db.session.query(VaxState.date).group_by(VaxState.date)
        query = db.session.query(VaxState)

        if state != 'all':
            state_exists = db.session.query(db.session.query(VaxState.state).filter(VaxState.state.ilike(f'%{state}')).exists()).scalar()
            if state_exists:
                query = query.filter(VaxState.state.ilike(f'%{state}'))
            else:
                abort(404, f"State name '{state}' not found in database")

        if not (args['page'] or args['size']):
            date_subquery = date_subquery.order_by(VaxState.date.desc()).limit(7)
            query = query.filter(VaxState.date.in_(date_subquery)).order_by(VaxState.date, VaxState.state)
            return query.all()

        # Handle date bullshit first, then deal with actual data
        # Get dates based on the pagination values

        date_subquery = date_subquery.order_by(VaxState.date)
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
        query = query.filter(VaxState.date.in_(dates)).order_by(VaxState.date, VaxState.state)
        result = query.all()

        if result:
            return result
        abort(404, f"Invalid page number '{page}'. Valid page numbers are between 1 to {date_result.pages} for size of {date_result.per_page} item(s)")


@api.route('/vax_state/<string:state>/<string:date>')
class VaxStateByStateByDateWithPagination(Resource):

    @api.marshal_with(vax_state, skip_none=True)
    def get(self, state=None, date=None):
        query = db.session.query(VaxState)
        if state == 'all':
            query = query.filter(VaxState.date == date)
            return query.all()
        else:
            query = query.filter(VaxState.state.ilike(state), VaxState.date == date)
            if db.session.query(query.exists()).scalar():
                result = query.first()
                return result
        abort(404, error=f"State '{state}' with date '{date}' is not found in database.")
