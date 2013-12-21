import types

def index():

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

    cancer_form = SQLFORM.factory(db.cancer_data_by_area, 
                            Field('YEARS',
                                requires=IS_IN_SET(years, multiple = True),
                                widget = SQLFORM.widgets.multiple.widget),
                            _formname='cancer_form')

    # from gluon.debug import dbg
    # dbg.set_trace() # stop here!

    output = None
    query = None

    def validate_cancer_form(form):
        if not form.vars.YEARS:
            form.errors.YEARS = 'Must provide a year!'

    if cancer_form.process(_formname='cancer_form', onvalidation=validate_cancer_form).accepted:

        area_query = db.cancer_data_by_area['AREA'] == request.vars['AREA']
        event_query = db.cancer_data_by_area['EVENT_TYPE'] == request.vars['EVENT_TYPE']
        race_query = db.cancer_data_by_area['RACE'] == request.vars['RACE']
        sex_query  = db.cancer_data_by_area['SEX']  == request.vars['SEX']
        site_query = db.cancer_data_by_area['SITE'] == request.vars['SITE']
        
        if type(request.vars['YEARS']) is types.ListType:
            request.vars['YEARS'] = map(int, request.vars['YEARS'])
            year_query = reduce(lambda a,b: a|b, [db.cancer_data_by_area.YEAR==year for year in request.vars['YEARS']])
        elif type(request.vars['YEARS']) is types.StringType:
            year_query = db.cancer_data_by_area.YEAR==int(request.vars['YEARS'])

        query = area_query & race_query  & sex_query & event_query & site_query & year_query
        output = db(query).select()

    elif cancer_form.errors:
        session.flash = cancer_form.errors

    return locals()