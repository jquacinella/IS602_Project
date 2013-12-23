import types
import gluon.contenttype
from gluon.serializers import json
import json

@request.restful()
def index():
    ''' REST interface for CDC Cancer (JSON response on POST).'''

    def GET():
        cancer_form = _cancer_data_form()
        return locals()

    def POST(*args, **vars):
        cancer_form = _cancer_data_form()

        #from gluon.debug import dbg
        #dbg.set_trace() # stop here!

        output = None
        query = None

        #if cancer_form.process().accepted:
        if cancer_form.accepts(request, formname=None):
            # Build up portions of the query 
            area_query = db.cancer_data_by_area['AREA'] == request.vars['AREA']
            event_query = db.cancer_data_by_area['EVENT_TYPE'] == request.vars['EVENT_TYPE']
            race_query = db.cancer_data_by_area['RACE'] == request.vars['RACE']
            sex_query  = db.cancer_data_by_area['SEX']  == request.vars['SEX']
            site_query = db.cancer_data_by_area['SITE'] == request.vars['SITE']
            
            # # Build up the portion of the query for year, which can be a list
            # if type(request.vars['YEARS']) is types.ListType:
            #     request.vars['YEARS'] = map(int, request.vars['YEARS'])
            #     year_query = reduce(lambda a,b: a|b, [db.cancer_data_by_area.YEAR==year for year in request.vars['YEARS']])
            # elif type(request.vars['YEARS']) is types.StringType:
            #     year_query = db.cancer_data_by_area.YEAR==int(request.vars['YEARS'])

            # Combine all subqueries into one
            #query = area_query & race_query  & sex_query & event_query & site_query & year_query
            query = area_query & race_query  & sex_query & event_query & site_query

            # Get the output from MySQL
            output = db(query).select(orderby=db.cancer_data_by_area.YEAR)

            # Generate JSON object
            data = []
            for row in output:
                year = row['YEAR']
                data.append({"date": str(year), "count": row[request.vars['TARGET']]})

            response.headers['Content-Type'] = gluon.contenttype.contenttype('.json')
            response.status = 200
            return json.dumps(data)

        elif cancer_form.errors:
            response.headers['Content-Type'] = gluon.contenttype.contenttype('.json')
            response.status = 500
            return json.dumps({'error': cancer_form.errors, 'vars': request.vars})

        response.headers['Content-Type'] = gluon.contenttype.contenttype('.json')
        response.status = 200
        return json.dumps({'vars': request.vars})

    return locals()


def _cancer_data_form():
    db['cancer_data_by_area'].AREA.requires = IS_IN_SET(states, multiple=False)
    db['cancer_data_by_area'].AREA.widget = SQLFORM.widgets.options.widget
    
    db['cancer_data_by_area'].EVENT_TYPE.requires = IS_IN_SET(event_types, multiple=False)
    db['cancer_data_by_area'].EVENT_TYPE.widget = SQLFORM.widgets.options.widget

    db['cancer_data_by_area'].RACE.requires = IS_IN_SET(races, multiple=False)
    db['cancer_data_by_area'].RACE.widget = SQLFORM.widgets.options.widget

    db['cancer_data_by_area'].SEX.requires = IS_IN_SET(sex, multiple=False)
    db['cancer_data_by_area'].SEX.widget = SQLFORM.widgets.options.widget

    db['cancer_data_by_area'].SITE.requires = IS_IN_SET(cancer_sites, multiple=False)
    db['cancer_data_by_area'].SITE.widget = SQLFORM.widgets.options.widget
  
    db['cancer_data_by_area'].AGE_ADJUSTED_CI_LOWER.writable = False
    db['cancer_data_by_area'].AGE_ADJUSTED_CI_LOWER.readable = False
    db['cancer_data_by_area'].AGE_ADJUSTED_CI_UPPER.writable = False
    db['cancer_data_by_area'].AGE_ADJUSTED_CI_UPPER.readable = False
    db['cancer_data_by_area'].AGE_ADJUSTED_RATE.writable = False
    db['cancer_data_by_area'].AGE_ADJUSTED_RATE.readable = False
    db['cancer_data_by_area'].CRUDE_CI_LOWER.writable = False
    db['cancer_data_by_area'].CRUDE_CI_LOWER.readable = False
    db['cancer_data_by_area'].CRUDE_CI_UPPER.writable = False
    db['cancer_data_by_area'].CRUDE_CI_UPPER.readable = False
    db['cancer_data_by_area'].CRUDE_RATE.writable = False
    db['cancer_data_by_area'].CRUDE_RATE.readable = False
    db['cancer_data_by_area'].COUNT.writable = False
    db['cancer_data_by_area'].COUNT.readable = False
    db['cancer_data_by_area'].POPULATION.writable = False
    db['cancer_data_by_area'].POPULATION.readable = False
    db['cancer_data_by_area'].YEAR.writable = False
    db['cancer_data_by_area'].YEAR.readable = False

    return SQLFORM.factory(db.cancer_data_by_area, 
                            Field('TARGET', default=target_variable[0], requires=IS_IN_SET(target_variable, multiple = False)), 
                            _formname='cancer_form')

