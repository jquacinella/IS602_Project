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

    db['cancer_data_by_area'].YEAR.requires = IS_IN_SET(years, multiple=False)
    db['cancer_data_by_area'].YEAR.widget = SQLFORM.widgets.options.widget

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

    cancer_form = SQLFORM.factory(db.cancer_data_by_area, _formname='cancer_form')

    # from gluon.debug import dbg
    # dbg.set_trace() # stop here!

    output = "lame"
    if cancer_form.process(_formname='cancer_form').accepted:
        area_query = db.cancer_data_by_area['AREA'] == request.vars['AREA']
        race_query = db.cancer_data_by_area['RACE'] == request.vars['RACE']
        sex_query  = db.cancer_data_by_area['SEX']  == request.vars['SEX']
        site_query = db.cancer_data_by_area['SITE'] == request.vars['SITE']
        year_query = db.cancer_data_by_area['YEAR'] == request.vars['YEAR']
        
        output = db.cancer_data_by_area(area_query & race_query & sex_query & site_query & year_query)

    elif cancer_form.errors:
        output = cancer_form.errors

    return locals()