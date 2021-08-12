from flask_restx import Namespace, Resource, fields, abort
from flask_sqlalchemy import Pagination
from covid19_api.db_model.sqlalchemy_models import CheckinMalaysiaTime, CheckinMalaysia, CheckinState, TraceMalaysia
from covid19_api.api import db

api = Namespace('mysejahtera', 'MySejahtera check-in and tracing data')

checkin_malaysia_time = api.model('checkin_malaysia_time', {
    'row_id': fields.Integer(title='Row ID', description='ID of the row'),
    'row_version': fields.Integer(title='Row version'),
    'date': fields.Date(title='Date'),
    'timeslot0': fields.Integer(title='Number of check-ins for time 00:00 to 00:29'),
    'timeslot1': fields.Integer(title='Number of check-ins for time 00:30 to 00:59'),
    'timeslot2': fields.Integer(title='Number of check-ins for time 01:00 to 01:29'),
    'timeslot3': fields.Integer(title='Number of check-ins for time 01:30 to 01:59'),
    'timeslot4': fields.Integer(title='Number of check-ins for time 02:00 to 02:29'),
    'timeslot5': fields.Integer(title='Number of check-ins for time 02:30 to 02:59'),
    'timeslot6': fields.Integer(title='Number of check-ins for time 03:00 to 03:29'),
    'timeslot7': fields.Integer(title='Number of check-ins for time 03:30 to 03:59'),
    'timeslot8': fields.Integer(title='Number of check-ins for time 04:00 to 04:29'),
    'timeslot9': fields.Integer(title='Number of check-ins for time 04:30 to 04:59'),
    'timeslot10': fields.Integer(title='Number of check-ins for time 05:00 to 05:29'),
    'timeslot11': fields.Integer(title='Number of check-ins for time 05:30 to 05:59'),
    'timeslot12': fields.Integer(title='Number of check-ins for time 06:00 to 06:29'),
    'timeslot13': fields.Integer(title='Number of check-ins for time 06:30 to 06:59'),
    'timeslot14': fields.Integer(title='Number of check-ins for time 07:00 to 07:29'),
    'timeslot15': fields.Integer(title='Number of check-ins for time 07:30 to 07:59'),
    'timeslot16': fields.Integer(title='Number of check-ins for time 08:00 to 08:29'),
    'timeslot17': fields.Integer(title='Number of check-ins for time 08:30 to 08:59'),
    'timeslot18': fields.Integer(title='Number of check-ins for time 09:00 to 09:29'),
    'timeslot19': fields.Integer(title='Number of check-ins for time 09:30 to 09:59'),
    'timeslot20': fields.Integer(title='Number of check-ins for time 10:00 to 10:29'),
    'timeslot21': fields.Integer(title='Number of check-ins for time 10:30 to 10:59'),
    'timeslot22': fields.Integer(title='Number of check-ins for time 11:00 to 11:29'),
    'timeslot23': fields.Integer(title='Number of check-ins for time 11:30 to 11:59'),
    'timeslot24': fields.Integer(title='Number of check-ins for time 12:00 to 12:29'),
    'timeslot25': fields.Integer(title='Number of check-ins for time 12:30 to 12:59'),
    'timeslot26': fields.Integer(title='Number of check-ins for time 13:00 to 13:29'),
    'timeslot27': fields.Integer(title='Number of check-ins for time 13:30 to 13:59'),
    'timeslot28': fields.Integer(title='Number of check-ins for time 14:00 to 14:29'),
    'timeslot29': fields.Integer(title='Number of check-ins for time 14:30 to 14:59'),
    'timeslot30': fields.Integer(title='Number of check-ins for time 15:00 to 15:29'),
    'timeslot31': fields.Integer(title='Number of check-ins for time 15:30 to 15:59'),
    'timeslot32': fields.Integer(title='Number of check-ins for time 16:00 to 16:29'),
    'timeslot33': fields.Integer(title='Number of check-ins for time 16:30 to 16:59'),
    'timeslot34': fields.Integer(title='Number of check-ins for time 17:00 to 17:29'),
    'timeslot35': fields.Integer(title='Number of check-ins for time 17:30 to 17:59'),
    'timeslot36': fields.Integer(title='Number of check-ins for time 18:00 to 18:29'),
    'timeslot37': fields.Integer(title='Number of check-ins for time 18:30 to 18:59'),
    'timeslot38': fields.Integer(title='Number of check-ins for time 19:00 to 19:29'),
    'timeslot39': fields.Integer(title='Number of check-ins for time 19:30 to 19:59'),
    'timeslot40': fields.Integer(title='Number of check-ins for time 20:00 to 20:29'),
    'timeslot41': fields.Integer(title='Number of check-ins for time 20:30 to 20:59'),
    'timeslot42': fields.Integer(title='Number of check-ins for time 21:00 to 21:29'),
    'timeslot43': fields.Integer(title='Number of check-ins for time 21:30 to 21:59'),
    'timeslot44': fields.Integer(title='Number of check-ins for time 22:00 to 22:29'),
    'timeslot45': fields.Integer(title='Number of check-ins for time 22:30 to 22:59'),
    'timeslot46': fields.Integer(title='Number of check-ins for time 23:00 to 23:29'),
    'timeslot47': fields.Integer(title='Number of check-ins for time 23:30 to 23:59')
})

checkin_malaysia = api.model('checkin_malaysia', {
    'row_id': fields.Integer(title='Row ID', description='ID of the row'),
    'row_version': fields.Integer(title='Row version'),
    'date': fields.Date(title='Date'),
    'checkins': fields.Integer(title='Number of checkins'),
    'unique_ind': fields.Integer(title='Number of unique individuals checked in'),
    'unique_loc': fields.Integer(title='Number of unique premises checked in')
})

checkin_state = api.model('checkin_malaysia', {
    'row_id': fields.Integer(title='Row ID', description='ID of the row'),
    'row_version': fields.Integer(title='Row version'),
    'date': fields.Date(title='Date'),
    'state': fields.String(title='State name'),
    'checkins': fields.Integer(title='Number of checkins'),
    'unique_ind': fields.Integer(title='Number of unique individuals checked in'),
    'unique_loc': fields.Integer(title='Number of unique premises checked in')
})

trace_malaysia = api.model('trace_malaysia', {
    'row_id': fields.Integer(title='Row ID', description='ID of the row'),
    'row_version': fields.Integer(title='Row version'),
    'date': fields.Date(title='Date'),
    'casual_contacts': fields.Integer(title='Casual contact count'),
    'hide_large': fields.Integer(title='Large hotspot count identified by CPRC HIDE system'),
    'hide_small': fields.Integer(title='Small hotspot count identified by CPRC HIDE system'),
})

pagination_parser = api.parser()
pagination_parser.add_argument('page', location='args', help='Page number', type=int)
pagination_parser.add_argument('size', location='args', help='Items per page', type=int)

@api.route('/checkin_malaysia_time')
class CheckinMalaysiaTimeWithPagination(Resource):

    @api.expect(pagination_parser)
    @api.marshal_with(checkin_malaysia_time, as_list=True, skip_none=True)
    def get(self):
        args: dict = pagination_parser.parse_args()
        page = args.get('page') or 1
        size = args.get('size') or 7

        date_subquery = db.session.query(CheckinMalaysiaTime.date)
        query = db.session.query(CheckinMalaysiaTime)

        if not (args['page'] or args['size']):
            date_subquery = date_subquery.order_by(CheckinMalaysiaTime.date.desc()).limit(7)
            query = query.filter(CheckinMalaysiaTime.date.in_(date_subquery)).order_by(CheckinMalaysiaTime.date)
            return query.all()

        result:Pagination = query.paginate(page, size, error_out=False)
        if result.items:
            return result.items
        abort(404, f'Invalid page number {page}. Valid page numbers are between 1 to {result.pages}')


@api.route('/checkin_malaysia_time/<string:date>')
class CheckinMalaysiaTimeByDate(Resource):

    @api.marshal_with(checkin_malaysia_time, skip_none=True)
    def get(self, date):
        query = db.session.query(CheckinMalaysiaTime).filter(CheckinMalaysiaTime.date == date)
        if db.session.query(query.exists()).scalar():
            result = query.first()
            return result
        abort(404, error=f"Date '{date}' is not found in database.")


@api.route('/checkin_malaysia')
class CheckinMalaysiaWithPagination(Resource):

    @api.expect(pagination_parser)
    @api.marshal_with(checkin_malaysia, as_list=True, skip_none=True)
    def get(self):
        args: dict = pagination_parser.parse_args()
        page = args.get('page') or 1
        size = args.get('size') or 7

        date_subquery = db.session.query(CheckinMalaysia.date)
        query = db.session.query(CheckinMalaysia)

        if not (args['page'] or args['size']):
            date_subquery = date_subquery.order_by(CheckinMalaysia.date.desc()).limit(7)
            query = query.filter(CheckinMalaysia.date.in_(date_subquery)).order_by(CheckinMalaysia.date)
            return query.all()

        result:Pagination = query.paginate(page, size, error_out=False)
        if result.items:
            return result.items
        abort(404, f'Invalid page number {page}. Valid page numbers are between 1 to {result.pages}')


@api.route('/checkin_malaysia/<string:date>')
class CheckinMalaysiaByDate(Resource):

    @api.marshal_with(checkin_malaysia, skip_none=True)
    def get(self, date):
        query = db.session.query(CheckinMalaysia).filter(CheckinMalaysia.date == date)
        if db.session.query(query.exists()).scalar():
            result = query.first()
            return result
        abort(404, error=f"Date '{date}' is not found in database.")


@api.route('/checkin_state')
class CheckinStateWithPagination(Resource):

    @api.expect(pagination_parser)
    @api.marshal_with(checkin_state, as_list=True, skip_none=True)
    def get(self):
        args: dict = pagination_parser.parse_args()
        page = args.get('page') or 1
        # We don't use size against the final result, instead on the number of dates
        size = args.get('size') or 7

        date_subquery = db.session.query(CheckinState.date).group_by(CheckinState.date).order_by(CheckinState.date)
        query = db.session.query(CheckinState)

        if not (args['page'] or args['size']):
            date_subquery = date_subquery.order_by(CheckinState.date.desc()).limit(7)
            query = query.filter(CheckinState.date.in_(date_subquery)).order_by(CheckinState.date, CheckinState.state)
            return query.all()

        # Handle date bullshit first, then deal with actual data

        # Get dates based on the pagination values
        date_subquery: Pagination = date_subquery.paginate(page, size, error_out=False)
        # Get all dates returned by the pagination
        dates = [date[0] for date in date_subquery.items]

        # Future project: implement pagination logic and expose it to end user
        attr = {a: getattr(date_subquery, a) for a in dir(date_subquery) if not a.startswith('__') and not callable(getattr(date_subquery, a))}

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
        query = query.filter(CheckinState.date.in_(dates)).order_by(CheckinState.date, CheckinState.state)
        result = query.all()

        if result:
            return result
        abort(404, f'Invalid page number {page}. Valid page numbers are between 1 to {date_subquery.pages}')


@api.route('/checkin_state/<string:state>')
class CheckinStateByStateWithPagination(Resource):

    @api.expect(pagination_parser)
    @api.marshal_with(checkin_state, as_list=True, skip_none=True)
    def get(self, state=None):
        args: dict = pagination_parser.parse_args()
        page = args.get('page') or 1
        size = args.get('size') or 7

        date_subquery = db.session.query(CheckinState.date).group_by(CheckinState.date)
        query = db.session.query(CheckinState)

        if state != 'all':
            state_exists = db.session.query(db.session.query(CheckinState.state).filter(CheckinState.state.ilike(f'%{state}')).exists()).scalar()
            if state_exists:
                query = query.filter(CheckinState.state.ilike(f'%{state}'))
            else:
                abort(404, f"State name '{state}' not found in database")

        if not (args['page'] or args['size']):
            date_subquery = date_subquery.order_by(CheckinState.date.desc()).limit(7)
            query = query.filter(CheckinState.date.in_(date_subquery)).order_by(CheckinState.date, CheckinState.state)
            return query.all()

        # Handle date bullshit first, then deal with actual data
        # Get dates based on the pagination values

        date_subquery = date_subquery.order_by(CheckinState.date)
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
        query = query.filter(CheckinState.date.in_(dates)).order_by(CheckinState.date, CheckinState.state)
        result = query.all()

        if result:
            return result
        abort(404, f'Invalid page number {page}. Valid page numbers are between 1 to {date_result.pages}')


@api.route('/checkin_state/<string:state>/<string:date>')
class CheckinStateByStateByDateWithPagination(Resource):

    @api.marshal_with(checkin_state, skip_none=True)
    def get(self, state=None, date=None):
        query = db.session.query(CheckinState)
        if state == 'all':
            query = query.filter(CheckinState.date == date)
            return query.all()
        else:
            query = query.filter(CheckinState.state.ilike(state), CheckinState.date == date)
            if db.session.query(query.exists()).scalar():
                result = query.first()
                return result
        abort(404, error=f"State '{state} with date '{date}' is not found in database.")
