from flask_restx import Namespace, Resource, fields, abort
from flask_sqlalchemy import Pagination
from sqlalchemy.sql.expression import or_
from covid19_api.db_model.sqlalchemy_models import CasesMalaysia, CasesState, Clusters, DeathsMalaysia, DeathsState, HospitalByState, ICUByState, PKRCByState, TestsMalaysia
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

cases_state = api.model('cases_state', {
    'row_id': fields.Integer(title='Row ID', description='ID of the row', example='1'),
    'row_version': fields.Integer(title='Row version', description='The version of the row.'),
    'date': fields.Date(title='Date'),
    'state': fields.String(title='State name'),
    'cases_new': fields.Integer(title='New cases')
})

clusters = api.model('clusters', {
    'row_id': fields.Integer(title='Row ID', description='ID of the row', example='1'),
    'row_version': fields.Integer(title='Row version', description='The version of the row.'),
    'cluster': fields.String(title='Cluster name'),
    'state': fields.String(title='State name'),
    'district': fields.String(title='District name'),
    'date_announced': fields.Date(title='Date cluster is announced'),
    'date_last_onset': fields.Date(title='Most recent date with new cases reported in the cluster'),
    'category': fields.String(title='Cluster category'),
    'status': fields.String(title='Cluster status'),
    'cases_new': fields.Integer(title='New cases reported in the cluster'),
    'cases_total': fields.Integer(title='Total number of cases reported in the cluster'),
    'cases_active': fields.Integer(title='Number of active cases reported in the cluster'),
    'tests': fields.Integer(title='Number of tests performed for the cluster'),
    'icu': fields.Integer(title='Number of individuals under ICU care for the cluster'),
    'deaths': fields.Integer(title='Number of deaths for the cluster'),
    'recovered': fields.Integer(title='Number of recovered individuals for the cluster')
})

deaths_malaysia = api.model('deaths_malaysia', {
    'row_id': fields.Integer(title='Deaths ID'),
    'row_version': fields.Integer(title='Row version'),
    'date': fields.Date(title='Reported date'),
    'deaths_new': fields.Integer(title='New deaths for the reported date')
})

deaths_state = api.model('deaths_state', {
    'row_id': fields.Integer(title='Deaths ID'),
    'row_version': fields.Integer(title='Row version'),
    'date': fields.Date(title='Reported date'),
    'state': fields.String(title='State name'),
    'deaths_new': fields.Integer(title='New deaths for the reported date')
})

hospital = api.model('hospital', {
    'row_id': fields.Integer(title='Deaths ID'),
    'row_version': fields.Integer(title='Row version'),
    'date': fields.Date(title='Reported date'),
    'state': fields.String(title='State name'),
    'beds': fields.Integer(title='Total available hospital beds'),
    'beds_covid': fields.Integer(title='Total available hospital beds dedicated for COVID-19'),
    'beds_noncrit': fields.Integer(title='Total available hospital beds for non-critical care'),
    'admitted_pui': fields.Integer(title='Total admitted persons under investigation'),
    'admitted_covid': fields.Integer(title='Total admitted persons with COVID-19'),
    'admitted_total': fields.Integer(title='Total admissions'),
    'discharged_pui': fields.Integer(title='Total discharged persons under investigation'),
    'discharged_covid': fields.Integer(title='Total discharged persons with COVID-19'),
    'discharged_total': fields.Integer(title='Total discharges'),
    'hosp_pui': fields.Integer(title='Total hospitalised persons under investigation'),
    'hosp_covid': fields.Integer(title='Total hospitalised COVID-19 patients'),
    'hosp_noncovid': fields.Integer(title='Total non-COVID patients')
})

icu = api.model('icu', {
    'row_id': fields.Integer(title='Deaths ID'),
    'row_version': fields.Integer(title='Row version'),
    'date': fields.Date(title='Reported date'),
    'state': fields.String(title='State name'),
    'beds_icu': fields.Integer(title='Gazetted ICU beds'),
    'beds_icu_rep': fields.Integer(title='Total ICU beds for Anaesthesiology & Critical Care departments'),
    'beds_icu_total': fields.Integer(title='Total ICU beds'),
    'beds_icu_covid': fields.Integer(title='Total ICU beds dedicated for COVID-19'),
    'vent': fields.Integer(title='Total available ventilators'),
    'vent_port': fields.Integer(title='Total available portable ventilators'),
    'icu_covid': fields.Integer(title='Total number of COVID individuals under ICU care'),
    'icu_pui': fields.Integer(title='Total number of PUI individuals under ICU care'),
    'icu_noncovid': fields.Integer(title='Total number of non-COVID individuals under ICU care'),
    'vent_covid': fields.Integer(title='Total number of COVID individuals that require ventilator'),
    'vent_pui': fields.Integer(title='Total number of PUI individuals that require ventilator'),
    'vent_noncovid': fields.Integer(title='Total number of non-COVID individuals that require ventilator')
})

pkrc = api.model('pkrc', {
    'row_id': fields.Integer(title='Deaths ID'),
    'row_version': fields.Integer(title='Row version'),
    'date': fields.Date(title='Reported date'),
    'state': fields.String(title='State name'),
    'beds': fields.Integer(title='Total available PKRC beds'),
    'admitted_pui': fields.Integer(title='Total admitted persons under investigation'),
    'admitted_covid': fields.Integer(title='Total admitted persons with COVID-19'),
    'admitted_total': fields.Integer(title='Total admissions'),
    'discharged_pui': fields.Integer(title='Total discharged persons under investigation'),
    'discharged_covid': fields.Integer(title='Total discharged persons with COVID-19'),
    'discharged_total': fields.Integer(title='Total discharges'),
    'pkrc_pui': fields.Integer(title='Total hospitalised persons under investigation'),
    'pkrc_covid': fields.Integer(title='Total hospitalised COVID-19 patients'),
    'pkrc_noncovid': fields.Integer(title='Total non-COVID patients')
})

tests_malaysia = api.model('tests_malaysia', {
    'row_id': fields.Integer(title='Deaths ID'),
    'row_version': fields.Integer(title='Row version'),
    'date': fields.Date(title='Reported date'),
    'rtk_ag': fields.Integer(title='Total RTK-Ag tests performed'),
    'pcr': fields.Integer(title='Total RT-PCR tests performed')
})

pagination_parser = api.parser()
pagination_parser.add_argument('page', location='args', help='Page number', type=int)
pagination_parser.add_argument('size', location='args', help='Items per page', type=int)


@api.route('/cases_malaysia')
class CasesMalaysiaWithPagination(Resource):

    @api.expect(pagination_parser)
    @api.marshal_with(cases_malaysia, as_list=True, skip_none=True)
    @api.doc(responses={404: 'Not Found'})
    def get(self):
        """
        Returns country-wide new cases with pagination support.

        Defaults to get new cases for the last 7 days if page and size are not defined, in ascending date order.

        Size parameter is optional and defaults to 10 items.
        """
        args: dict = pagination_parser.parse_args()
        page = args.get('page') or 1
        size = args.get('size') or 10

        date_subquery = db.session.query(CasesMalaysia.date)
        query = db.session.query(CasesMalaysia)

        if not (args['page'] or args['size']):
            date_subquery = date_subquery.order_by(CasesMalaysia.date.desc()).limit(7)
            query = query.filter(CasesMalaysia.date.in_(date_subquery)).order_by(CasesMalaysia.date)

        result:Pagination = query.paginate(page, size, error_out=False)
        if result.items:
            return result.items
        abort(404, error=f"Invalid page number '{page}'. Valid page numbers are between 1 to {result.pages} for size of {result.per_page} item(s)")


@api.route('/cases_malaysia/<string:date>')
class CasesMalaysiaByDate(Resource):

    @api.marshal_with(cases_malaysia, skip_none=True)
    @api.doc(responses={404: 'Not Found'})
    def get(self, date):
        """
        Returns country-wide new cases based on date provided.

        Date format follows ISO-8601 date format (YYYY-MM-DD eg. 2021-08-03).
        """
        query = db.session.query(CasesMalaysia).filter(CasesMalaysia.date == date)
        if db.session.query(query.exists()).scalar():
            result = query.first()
            return result
        abort(404, error=f"Date '{date}' is not found in database.")


@api.route('/cases_state')
class CasesStateWithPagination(Resource):

    @api.expect(pagination_parser)
    @api.marshal_with(cases_state, skip_none=True)
    @api.doc(responses={404: 'Not Found'})
    def get(self):
        """
        Returns new cases on per-state basis with pagination support.

        Defaults to get new cases for the last 7 days if page and size are not defined, in ascending date order.

        Size parameter is optional and defaults to 10 items.

        Note: Size parameter only applies to number of days, not number of items!
        """
        args: dict = pagination_parser.parse_args()
        page = args.get('page') or 1
        # We don't use size against the final result, instead on the number of dates
        size = args.get('size') or 7

        date_subquery = db.session.query(CasesState.date).group_by(CasesState.date).order_by(CasesState.date)
        query = db.session.query(CasesState)

        if not (args['page'] or args['size']):
            date_subquery = date_subquery.order_by(CasesState.date.desc()).limit(7)
            query = query.filter(CasesState.date.in_(date_subquery)).order_by(CasesState.date, CasesState.state)
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
        query = query.filter(CasesState.date.in_(dates)).order_by(CasesState.date, CasesState.state)
        result = query.all()

        if result:
            return result
        abort(404, error=f"Invalid page number '{page}'. Valid page numbers are between 1 to {date_result.pages} for size of {date_result.per_page} item(s)")


@api.route('/cases_state/<string:state>')
class CasesStateByDate(Resource):

    @api.expect(pagination_parser)
    @api.marshal_with(cases_state, as_list=True, skip_none=True)
    @api.doc(responses={404: 'Not Found'})
    def get(self, state):
        """
        Returns new cases for a state with pagination support.

        State name is case-insensitive.

        Defaults to get new cases for the last 7 days if page and size are not defined, in ascending date order.

        Size parameter is optional and defaults to 10 items.

        Note: Size parameter only applies to number of days, not number of items!
        """
        args: dict = pagination_parser.parse_args()
        page = args.get('page') or 1
        size = args.get('size') or 7

        date_subquery = db.session.query(CasesState.date).group_by(CasesState.date)
        query = db.session.query(CasesState)
        state_count = db.session.query(CasesState.state).distinct(CasesState.state).count()

        if not (args['page'] or args['size']):
            date_subquery = date_subquery.order_by(CasesState.date.desc()).limit(size)

        if state != 'all':
            state_exists = db.session.query(db.session.query(CasesState.state).filter(CasesState.state.ilike(f'%{state}')).exists()).scalar()
            if state_exists:
                query = query.filter(CasesState.state.ilike(f'%{state}'), CasesState.date.in_(date_subquery))
            else:
                abort(404, f"State name '{state}' not found in database")
        else:
            size = size * state_count
            query = query.filter(CasesState.date.in_(date_subquery))

        result:Pagination = query.order_by(CasesState.date).paginate(page, size, error_out=False)
        if result.items:
            return result.items


@api.route('/cases_state/<string:state>/<string:date>')
class CasesStateByStateWithPagination(Resource):

    @api.marshal_with(cases_state, as_list=True, skip_none=True)
    @api.doc(responses={404: 'Not Found'})
    def get(self, state, date):
        """
        Returns new cases for a state on the specified date.

        State name is case-insensitive.
        Date format follows ISO-8601 date format (YYYY-MM-DD eg. 2021-08-03).
        """
        query = db.session.query(CasesState)

        if state != 'all':
            state_exists = db.session.query(db.session.query(CasesState.state).filter(CasesState.state.ilike(f'%{state}')).exists()).scalar()
            if state_exists:
                query = query.filter(CasesState.state.ilike(f'%{state}'), CasesState.date == date)
            else:
                abort(404, f"State name '{state}' not found in database")
        else:
            query = query.filter(CasesState.date == date)

        result = query.all()
        if result:
            return result
        abort(404, error=f"State '{state}' with date '{date}' is not found in database.")


@api.route('/clusters')
class AllClusters(Resource):

    @api.expect(pagination_parser)
    @api.marshal_with(clusters, as_list=True, skip_none=True)
    def get(self):
        """
        Returns country-wide clusters with pagination support.

        Defaults to get top 10 clusters with active case count in descending order.

        Size parameter is optional and defaults to 10 items.
        """
        args: dict = pagination_parser.parse_args()
        page = args.get('page') or 1
        size = args.get('size') or 10

        query = db.session.query(Clusters)

        if not (args['page'] or args['size']):
            query = query.filter(Clusters.status != 'ended').order_by(Clusters.cases_active.desc()).limit(10)
            return query.all()

        result: Pagination = query.paginate(page, size, error_out=False)

        if result.items:
            return result.items
        abort(404, f"Invalid page number '{page}'. Valid page numbers are between 1 to {result.pages} for size of {result.per_page} item(s)")


@api.route('/clusters/state')
class AvailableClustersState(Resource):

    def get(self):
        """
        Get list of states with clusters.

        Returns a list of states available for query.
        """
        return {'available_states': [
            "Johor",
            "Kedah",
            "Kelantan",
            "Melaka",
            "Negeri Sembilan",
            "Pahang",
            "Perak",
            "Perlis",
            "Pulau Pinang",
            "Sabah",
            "Sarawak",
            "Selangor",
            "Terengganu",
            "WP Kuala Lumpur",
            "WP Putrajaya",
            "WP Labuan"
        ]}


@api.route('/clusters/state/<state>')
class GetClusterDataByState(Resource):

    @api.expect(pagination_parser)
    @api.marshal_with(clusters, as_list=True, skip_none=True)
    def get(self, state):
        """
        Get all clusters by state.

        State name is case-insensitive.
        Defaults to get the first 10 available clusters in the state.
        Size parameter is optional and defaults to 10 items.
        """
        args: dict = pagination_parser.parse_args()
        page = args.get('page') or 1
        size = args.get('size') or 10

        # Hack to allow "Semua Negeri" clusters to be always included in the query
        query = db.session.query(Clusters).filter(or_(Clusters.state.ilike(f'%{state}%'), Clusters.state.ilike('Semua Negeri')))

        result: Pagination = query.paginate(page, size, error_out=False)

        if result.items:
            return result.items
        abort(404, f"Invalid page number '{page}'. Valid page numbers are between 1 to {result.pages} for size of {result.per_page} item(s)")


# I would like to enable district search, but there's a few roadblocks with that idea sadly:
# - LIKE constructs are *NOT* fast. It's negligble in the situation where the number of rows are low,
#   but lots of rows = slow-downs.
#   - Good news is that *most* DB servers has their own implementation on having fast lookups with
#     indexes (PostgreSQL has <type>_pattern_ops which allows fast LIKE searches), but I don't know
#     if there's a database-agnostic way to set up the correct index for all database servers (yet).
#     Do make a pull-request if you have any ideas!
# - District names are stored in a single column, comma-separated. 
#   - Which is fine, but the problem is the names are not consistent (from a quick glance)
#     Which makes storing a separate table to store the district names can be complex and prone to
#     duplicates.
#   - There's a good news though: it may be possible to get district names and store it in a separate
#     table, but have to cater for situations where district names are not _always_ consistent.
#     Or just screw it and use the district names as-is.
#
# Nevertheless, I will implement it anyway when time permits, but expect district searching 
# to have weird quirks.


@api.route('/clusters/status')
class GetClusterStatusList(Resource):

    def get(self):
        """Get a list of available cluster status available for query."""
        query = db.session.query(Clusters.status).distinct(Clusters.status)

        return {'available_status': [status for status, in query.all()]}


@api.route('/clusters/status/<status>')
class GetClusterDataByStatus(Resource):

    @api.expect(pagination_parser)
    @api.marshal_with(clusters, as_list=True, skip_none=True)
    def get(self, status):
        """
        Get all clusters with the specified status.

        Status name is case-insensitive.
        Defaults to get the first 10 available clusters of the given status.
        Size parameter is optional and defaults to 10 items.
        """
        args: dict = pagination_parser.parse_args()
        page = args.get('page') or 1
        size = args.get('size') or 10
        
        query = db.session.query(Clusters).filter(Clusters.status.ilike(status))
        if not db.session.query(query.exists()).scalar():
            abort(404, f"Status '{status}' is not a valid cluster status")

        result: Pagination = query.paginate(page, size, error_out=False)

        if result.items:
            return result.items
        abort(404, f"Invalid page number '{page}'. Valid page numbers are between 1 to {result.pages} for size of {result.per_page} item(s)")


@api.route('/clusters/category')
class ClustersListAllCategories(Resource):

    def get(self):
        """Get all available cluster categories available for query."""
        query = db.session.query(Clusters.category).distinct(Clusters.category)

        return {'available_categories': [category for category, in query.all()]}


@api.route('/clusters/category/<category>')
class GetClusterDataByCategory(Resource):

    @api.expect(pagination_parser)
    @api.marshal_with(clusters, as_list=True, skip_none=True)
    def get(self, category: str):
        """
        Get all clusters with the specified category.

        Category name is case-insensitive.
        Defaults to get the first 10 available clusters of the given category.
        Size parameter is optional and defaults to 10 items.
        """
        args: dict = pagination_parser.parse_args()
        page = args.get('page') or 1
        size = args.get('size') or 10

        query = db.session.query(Clusters).filter(Clusters.category.ilike(f'%{category}%'))

        result: Pagination = query.paginate(page, size, error_out=False)

        if result.items:
            return result.items
        abort(404, f"Invalid page number '{page}'. Valid page numbers are between 1 to {result.pages} for size of {result.per_page} item(s)")


@api.route('/clusters/<string:name>')
class ClusterByName(Resource):

    @api.expect(pagination_parser)
    @api.marshal_with(clusters, as_list=True, skip_none=True)
    def get(self, name: str):
        """
        Get cluster data by cluster name

        Cluster name is case-insensitive.
        Defaults to get the first 10 available clusters of the given category.
        Size parameter is optional and defaults to 10 items.
        """
        query = db.session.query(Clusters).filter(Clusters.cluster.ilike(f'%{name}%'))
        result = query.all()
        if result:
            return result
        abort(404, error=f"Cluster name '{name}' not found in database")


@api.route('/deaths_malaysia')
class DeathsMalaysiaWithPagination(Resource):

    @api.expect(pagination_parser)
    @api.marshal_with(deaths_malaysia, as_list=True, skip_none=True)
    def get(self):
        """
        Get country-wide new deaths with pagination support.

        Defaults to get new cases for the last 7 days if page or size is not defined, in ascending date order.

        Size parameter is optional and defaults to 10 items.
        """
        args: dict = pagination_parser.parse_args()
        page = args.get('page') or 1
        size = args.get('size') or 7

        date_subquery = db.session.query(DeathsMalaysia.date)
        query = db.session.query(DeathsMalaysia)

        if not (args['page'] or args['size']):
            date_subquery = date_subquery.order_by(DeathsMalaysia.date.desc()).limit(7)
            query = query.filter(DeathsMalaysia.date.in_(date_subquery)).order_by(DeathsMalaysia.date)
            return query.all()

        result:Pagination = query.paginate(page, size, error_out=False)

        if result.items:
            return result.items
        abort(404, f"Invalid page number '{page}'. Valid page numbers are between 1 to {result.pages} for size of {result.per_page} item(s)")


@api.route('/deaths_malaysia/<string:date>')
class DeathsMalaysiaByDate(Resource):

    @api.marshal_with(deaths_malaysia)
    def get(self, date):
        """
        Get country-wide new deaths based on date provided.

        Date format follows ISO-8601 date format (YYYY-MM-DD eg. 2021-08-03).
        """
        query = db.session.query(DeathsMalaysia).filter(DeathsMalaysia.date == date)
        if db.session.query(query.exists()).scalar():
            result = query.first()
            return result
        abort(404, error=f"Date '{date}' is not found in database.")


@api.route('/deaths_state')
class DeathsStatewithPagination(Resource):

    @api.expect(pagination_parser)
    @api.marshal_with(deaths_state, as_list=True, skip_none=True)
    def get(self):
        """
        Get per-state new deaths on per-state basis with pagination support.

        Defaults to get new cases for the last 7 days if page and size are not defined, in ascending date order.

        Size parameter is optional and defaults to 10 days worth of data.

        Note: Size parameter only applies to number of days, not number of items!
        """
        args: dict = pagination_parser.parse_args()
        page = args.get('page') or 1
        # We don't use size against the final result, instead on the number of dates
        size = args.get('size') or 7

        date_subquery = db.session.query(DeathsState.date).group_by(DeathsState.date)
        query = db.session.query(DeathsState)
        state_count = db.session.query(DeathsState.state).distinct(DeathsState.state).count()

        if not (args['page'] or args['size']):
            date_subquery = date_subquery.order_by(DeathsState.date.desc()).limit(size)
            query = query.filter(DeathsState.date.in_(date_subquery)).order_by(DeathsState.date, DeathsState.state)
            return query.all()

        query = query.filter(DeathsState.date.in_(date_subquery)).order_by(DeathsState.date, DeathsState.state)

        size = size * state_count

        result: Pagination = query.paginate(page, size, error_out=False)
        if result.items:
            return result.items
        abort(404, f"Invalid page number '{page}'. Valid page numbers are between 1 to {result.pages} for size of {result.per_page} item(s)")


@api.route('/deaths_state/<string:state>')
class DeathsStateByStateWithPagination(Resource):

    @api.expect(pagination_parser)
    @api.marshal_with(deaths_state, as_list=True, skip_none=True)
    def get(self, state):
        """
        Returns new deaths for a state with pagination support.

        State name is case-insensitive.

        Defaults to get new cases for the last 7 days if page and size are not defined, in ascending date order.

        Size parameter is optional and defaults to 10 items.

        Note: Size parameter only applies to number of days, not number of items!
        """
        args: dict = pagination_parser.parse_args()
        page = args.get('page') or 1
        size = args.get('size') or 7

        date_subquery = db.session.query(DeathsState.date).group_by(DeathsState.date)
        query = db.session.query(DeathsState)
        state_count = db.session.query(DeathsState.state).distinct(DeathsState.state).count()

        if not (args['page'] or args['size']):
            date_subquery = date_subquery.order_by(DeathsState.date.desc()).limit(size)

        if state != 'all':
            state_exists = db.session.query(db.session.query(DeathsState.state).filter(DeathsState.state.ilike(f'%{state}')).exists()).scalar()
            if state_exists:
                query = query.filter(DeathsState.state.ilike(f'%{state}'), DeathsState.date.in_(date_subquery))
            else:
                abort(404, f"State name '{state}' not found in database")
        else:
            size = size * state_count
            query = query.filter(DeathsState.date.in_(date_subquery))

        result:Pagination = query.order_by(DeathsState.date).paginate(page, size, error_out=False)
        if result.items:
            return result.items


@api.route('/deaths_state/<string:state>/<string:date>')
class DeathsStateByStateByDate(Resource):

    @api.marshal_with(deaths_state, skip_none=True)
    def get(self, state, date):
        """
        Returns new deaths for a state on the specified date.

        State name is case-insensitive.
        Date format follows ISO-8601 date format (YYYY-MM-DD eg. 2021-08-03).
        """
        query = db.session.query(DeathsState).filter(DeathsState.state.ilike(state), DeathsState.date == date)
        if db.session.query(query.exists()).scalar():
            result = query.first()
            return result
        abort(404, error=f"State '{state}' with date '{date}' is not found in database.")


@api.route('/hospital')
class HospitalWithPagination(Resource):

    @api.expect(pagination_parser)
    @api.marshal_with(hospital)
    def get(self):
        """
        Returns hospital data on per-state basis with pagination support.

        Defaults to hospital data from all states for the last 7 days if page and size are not defined, in ascending date order.

        Size parameter is optional and defaults to 10 items.

        Note: Size parameter only applies to number of days, not number of items!
        """
        args: dict = pagination_parser.parse_args()
        page = args.get('page') or 1
        # We don't use size against the final result, instead on the number of dates
        size = args.get('size') or 7

        date_subquery = db.session.query(HospitalByState.date).group_by(HospitalByState.date).order_by(HospitalByState.date)
        query = db.session.query(HospitalByState)

        if not (args['page'] or args['size']):
            date_subquery = date_subquery.order_by(HospitalByState.date.desc()).limit(7)
            query = query.filter(HospitalByState.date.in_(date_subquery)).order_by(HospitalByState.date, HospitalByState.state)
            return query.all()

        # Ugh. Apparently Putrajaya didn't have hospital data till 2021-05-11, so we need to do 
        # some crappy dance around this to make it "work"

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
        # pagination_result = select date from hospital_by_state group by date order by date offset (SELECT (page_number - 1) * size) limit size;
        # query = select * from hospital_by_state where date in (pagination.result);
        query = query.filter(HospitalByState.date.in_(dates)).order_by(HospitalByState.date, HospitalByState.state)
        result = query.all()

        if result:
            return result
        abort(404, error=f"Invalid page number '{page}'. Valid page numbers are between 1 to {date_result.pages} for size of {date_result.per_page} item(s)")


@api.route('/hospital/<string:state>')
class HospitalByStateWithPagination(Resource):

    @api.expect(pagination_parser)
    @api.marshal_with(hospital, as_list=True, skip_none=True)
    def get(self, state=None):
        """
        Returns hospital data on specific state with pagination support.

        Defaults to hospital data for the last 7 days if page and size are not defined, in ascending date order.

        Size parameter is optional and defaults to 10 items.

        Note: Size parameter only applies to number of days, not number of items!
        """
        args: dict = pagination_parser.parse_args()
        page = args.get('page') or 1
        size = args.get('size') or 7

        date_subquery = db.session.query(HospitalByState.date).group_by(HospitalByState.date)
        query = db.session.query(HospitalByState)

        if state != 'all':
            state_exists = db.session.query(db.session.query(HospitalByState.state).filter(HospitalByState.state.ilike(f'%{state}')).exists()).scalar()
            if state_exists:
                query = query.filter(HospitalByState.state.ilike(f'%{state}'))
            else:
                abort(404, f"State name '{state}' not found in database")

        if not (args['page'] or args['size']):
            date_subquery = date_subquery.order_by(HospitalByState.date.desc()).limit(7)
            query = query.filter(HospitalByState.date.in_(date_subquery)).order_by(HospitalByState.date, HospitalByState.state)
            return query.all()

        # Ugh. Apparently Putrajaya didn't have hospital data till 2021-05-11, so we need to do 
        # some crappy dance around this to make it "work"
        # Get dates based on the pagination values

        date_subquery = date_subquery.order_by(HospitalByState.date)
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
        query = query.filter(HospitalByState.date.in_(dates)).order_by(HospitalByState.date, HospitalByState.state)
        result = query.all()

        if result:
            return result
        abort(404, error=f"Invalid page number '{page}'. Valid page numbers are between 1 to {date_result.pages} for size of {date_result.per_page} item(s)")


@api.route('/hospital/<string:state>/<string:date>')
class HospitalByStateByDateWithPagination(Resource):

    @api.marshal_with(hospital, skip_none=True)
    def get(self, state=None, date=None):
        """
        Returns hospital data for a state on the specified date.

        State name is case-insensitive.
        Date format follows ISO-8601 date format (YYYY-MM-DD eg. 2021-08-03).
        """
        query = db.session.query(HospitalByState)
        if state == 'all':
            query = query.filter(HospitalByState.date == date)
            return query.all()
        else:
            query = query.filter(HospitalByState.state.ilike(state), HospitalByState.date == date)
            if db.session.query(query.exists()).scalar():
                result = query.first()
                return result
        abort(404, error=f"State '{state} with date '{date}' is not found in database.")


@api.route('/icu')
class ICUWithPagination(Resource):

    @api.expect(pagination_parser)
    @api.marshal_with(icu, as_list=True, skip_none=True)
    def get(self):
        """
        Returns ICU data on per-state basis with pagination support.

        Defaults to ICU data from all states for the last 7 days if page and size are not defined, in ascending date order.

        Size parameter is optional and defaults to 10 items.

        Note: Size parameter only applies to number of days, not number of items!
        """
        args: dict = pagination_parser.parse_args()
        page = args.get('page') or 1
        # We don't use size against the final result, instead on the number of dates
        size = args.get('size') or 7

        date_subquery = db.session.query(ICUByState.date).group_by(ICUByState.date).order_by(ICUByState.date)
        query = db.session.query(ICUByState)

        if not (args['page'] or args['size']):
            date_subquery = date_subquery.order_by(ICUByState.date.desc()).limit(7)
            query = query.filter(ICUByState.date.in_(date_subquery)).order_by(ICUByState.date, ICUByState.state)
            return query.all()

        # Ugh. Apparently Putrajaya didn't have hospital data till 2021-05-11, so we need to do 
        # some crappy dance around this to make it "work"

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
        # pagination_result = select date from hospital_by_state group by date order by date offset (SELECT (page_number - 1) * size) limit size;
        # query = select * from hospital_by_state where date in (pagination.result);
        query = query.filter(ICUByState.date.in_(dates)).order_by(ICUByState.date, ICUByState.state)
        result = query.all()

        if result:
            return result
        abort(404, error=f"Invalid page number '{page}'. Valid page numbers are between 1 to {date_result.pages} for size of {date_result.per_page} item(s)")


@api.route('/icu/<string:state>')
class ICUByStateWithPagination(Resource):

    @api.expect(pagination_parser)
    @api.marshal_with(icu, as_list=True, skip_none=True)
    def get(self, state=None):
        """
        Returns ICU data on specific state with pagination support.

        Defaults to ICU data for the last 7 days if page and size are not defined, in ascending date order.

        Size parameter is optional and defaults to 10 items.

        Note: Size parameter only applies to number of days, not number of items!
        """
        args: dict = pagination_parser.parse_args()
        page = args.get('page') or 1
        size = args.get('size') or 7

        date_subquery = db.session.query(ICUByState.date).group_by(ICUByState.date)
        query = db.session.query(ICUByState)

        if state != 'all':
            state_exists = db.session.query(db.session.query(ICUByState.state).filter(ICUByState.state.ilike(f'%{state}')).exists()).scalar()
            if state_exists:
                query = query.filter(ICUByState.state.ilike(f'%{state}'))
            else:
                abort(404, f"State name '{state}' not found in database")

        if not (args['page'] or args['size']):
            date_subquery = date_subquery.order_by(ICUByState.date.desc()).limit(7)
            query = query.filter(ICUByState.date.in_(date_subquery)).order_by(ICUByState.date, ICUByState.state)
            return query.all()

        # Ugh. Apparently Putrajaya didn't have hospital data till 2021-05-11, so we need to do 
        # some crappy dance around this to make it "work"
        # Get dates based on the pagination values

        date_subquery = date_subquery.order_by(ICUByState.date)
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
        # pagination_result = select date from icu_by_state group by date order by date offset (SELECT (page_number - 1) * size) limit size;
        # query = select * from icu_by_state where date in (pagination.result);
        query = query.filter(ICUByState.date.in_(dates)).order_by(ICUByState.date, ICUByState.state)
        result = query.all()

        if result:
            return result
        abort(404, error=f"Invalid page number '{page}'. Valid page numbers are between 1 to {date_result.pages} for size of {date_result.per_page} item(s)")


@api.route('/icu/<string:state>/<string:date>')
class ICUByStateByDateWithPagination(Resource):

    @api.marshal_with(icu, as_list=True, skip_none=True)
    def get(self, state=None, date=None):
        """
        Returns ICU data for a state on the specified date.

        State name is case-insensitive.
        Date format follows ISO-8601 date format (YYYY-MM-DD eg. 2021-08-03).
        """
        query = db.session.query(ICUByState)
        if state == 'all':
            query = query.filter(ICUByState.date == date)
            return query.all()
        else:
            query = query.filter(ICUByState.state.ilike(state), ICUByState.date == date)
            if db.session.query(query.exists()).scalar():
                result = query.first()
                return result
        abort(404, error=f"State '{state}' with date '{date}' is not found in database.")


@api.route('/pkrc')
class PKRCWithPagination(Resource):

    @api.expect(pagination_parser)
    @api.marshal_with(pkrc, as_list=True, skip_none=True)
    def get(self):
        """
        Returns PKRC data on per-state basis with pagination support.

        Defaults to PKRC data from all states for the last 7 days if page and size are not defined, in ascending date order.

        Size parameter is optional and defaults to 10 items.

        Note: Size parameter only applies to number of days, not number of items!
        """
        args: dict = pagination_parser.parse_args()
        page = args.get('page') or 1
        # We don't use size against the final result, instead on the number of dates
        size = args.get('size') or 7

        date_subquery = db.session.query(PKRCByState.date).group_by(PKRCByState.date).order_by(PKRCByState.date)
        query = db.session.query(PKRCByState)

        if not (args['page'] or args['size']):
            date_subquery = date_subquery.order_by(PKRCByState.date.desc()).limit(7)
            query = query.filter(PKRCByState.date.in_(date_subquery)).order_by(PKRCByState.date, PKRCByState.state)
            return query.all()

        # Ugh. Apparently Putrajaya didn't have hospital data till 2021-05-11, so we need to do 
        # some crappy dance around this to make it "work"

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
        # pagination_result = select date from hospital_by_state group by date order by date offset (SELECT (page_number - 1) * size) limit size;
        # query = select * from hospital_by_state where date in (pagination.result);
        query = query.filter(PKRCByState.date.in_(dates)).order_by(PKRCByState.date, PKRCByState.state)
        result: Pagination = query.all()

        if result:
            return result
        abort(404, error=f"Invalid page number '{page}'. Valid page numbers are between 1 to {date_result.pages} for size of {date_result.per_page} item(s)")


@api.route('/pkrc/<string:state>')
class PKRCByStateWithPagination(Resource):

    @api.expect(pagination_parser)
    @api.marshal_with(pkrc, as_list=True, skip_none=True)
    def get(self, state=None):
        """
        Returns PKRC data on specific state with pagination support.

        Defaults to PKRC data for the last 7 days if page and size are not defined, in ascending date order.

        Size parameter is optional and defaults to 10 items.

        Note: Size parameter only applies to number of days, not number of items!
        """
        args: dict = pagination_parser.parse_args()
        page = args.get('page') or 1
        size = args.get('size') or 7

        date_subquery = db.session.query(PKRCByState.date).group_by(PKRCByState.date)
        query = db.session.query(PKRCByState)

        if state != 'all':
            state_exists = db.session.query(db.session.query(PKRCByState.state).filter(PKRCByState.state.ilike(f'%{state}')).exists()).scalar()
            if state_exists:
                query = query.filter(PKRCByState.state.ilike(f'%{state}'))
            else:
                abort(404, f"State name '{state}' not found in database")

        if not (args['page'] or args['size']):
            date_subquery = date_subquery.order_by(PKRCByState.date.desc()).limit(7)
            query = query.filter(PKRCByState.date.in_(date_subquery)).order_by(PKRCByState.date, PKRCByState.state)
            return query.all()

        # Ugh. Apparently Putrajaya didn't have hospital data till 2021-05-11, so we need to do 
        # some crappy dance around this to make it "work"
        # Get dates based on the pagination values

        date_subquery = date_subquery.order_by(PKRCByState.date)
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
        query = query.filter(PKRCByState.date.in_(dates)).order_by(PKRCByState.date, PKRCByState.state)
        result = query.all()

        if result:
            return result
        abort(404, error=f"Invalid page number '{page}'. Valid page numbers are between 1 to {date_result.pages} for size of {date_result.per_page} item(s)")


@api.route('/pkrc/<string:state>/<string:date>')
class PKRCByStateByDateWithPagination(Resource):

    @api.marshal_with(icu, as_list=True, skip_none=True)
    def get(self, state=None, date=None):
        """
        Returns hospital data for a state on the specified date.

        State name is case-insensitive.
        Date format follows ISO-8601 date format (YYYY-MM-DD eg. 2021-08-03).
        """
        query = db.session.query(PKRCByState)
        if state == 'all':
            query = query.filter(PKRCByState.date == date)
            return query.all()
        else:
            query = query.filter(PKRCByState.state.ilike(state), PKRCByState.date == date)
            if db.session.query(query.exists()).scalar():
                result = query.first()
                return result
        abort(404, error=f"State '{state}' with date '{date}' is not found in database.")


@api.route('/tests_malaysia')
class TestsMalaysiaWithPagination(Resource):

    @api.expect(pagination_parser)
    @api.marshal_with(tests_malaysia, as_list=True, skip_none=True)
    def get(self):
        """
        Returns country-wide testing data with pagination support.

        Defaults to get testing data for the last 7 days if page and size are not defined, in ascending date order.

        Size parameter is optional and defaults to 10 items.
        """
        args: dict = pagination_parser.parse_args()
        page = args.get('page') or 1
        size = args.get('size') or 7

        date_subquery = db.session.query(TestsMalaysia.date)
        query = db.session.query(TestsMalaysia)

        if not (args['page'] or args['size']):
            date_subquery = date_subquery.order_by(TestsMalaysia.date.desc()).limit(7)
            query = query.filter(TestsMalaysia.date.in_(date_subquery)).order_by(TestsMalaysia.date)
            return query.all()

        result:Pagination = query.paginate(page, size, error_out=False)
        if result.items:
            return result.items
        abort(404, f"Invalid page number '{page}'. Valid page numbers are between 1 to {result.pages} for size of {result.per_page} item(s)")


@api.route('/tests_malaysia/<string:date>')
class TestsMalaysiaByDate(Resource):

    @api.marshal_with(tests_malaysia, skip_none=True)
    def get(self, date):
        """
        Returns country-wide testing data based on date provided.

        Date format follows ISO-8601 date format (YYYY-MM-DD eg. 2021-08-03).
        """
        query = db.session.query(TestsMalaysia).filter(TestsMalaysia.date == date)
        if db.session.query(query.exists()).scalar():
            result = query.first()
            return result
        abort(404, error=f"Date '{date}' is not found in database.")
