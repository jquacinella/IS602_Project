# -*- coding: utf-8 -*-

#########################################################################
## This scaffolding model makes your app work on Google App Engine too
## File is released under public domain and you can use without limitations
#########################################################################

## if SSL/HTTPS is properly configured and you want all HTTP requests to
## be redirected to HTTPS, uncomment the line below:
# request.requires_https()

DB_HOST      = "localhost"
DB_USERNAME  = "is602"
DB_PASSWORD  = "test1234"
DB_NAME      = "is602"
DB_TABLENAME = "cancer_data_by_area"

db = DAL("mysql://%s:%s@%s/%s" % (DB_USERNAME, DB_PASSWORD, DB_HOST, DB_NAME))

states       = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'Atlanta', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Detroit', 'District of Columbia', 'East North Central', 'East South Central', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Los Angeles', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Middle Atlantic', 'Midwest', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Mountain', 'Nebraska', 'Nevada', 'New England', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Northeast', 'Ohio', 'Oklahoma', 'Oregon', 'Pacific', 'Pennsylvania', 'Rhode Island', 'San Francisco-Oakland', 'San Jose-Monterey', 'Seattle-Puget Sound', 'South', 'South Atlantic', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'United States (comparable to ICD-O-2)', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West', 'West North Central', 'West South Central', 'West Virginia', 'Wisconsin', 'Wyoming']
event_types  = ['Incidence', 'Mortality']
races        = ['American Indian/Alaska Native', 'Asian/Pacific Islander', 'All Races', 'Hispanic', 'Black', 'White']
sex          = ['Male', 'Female', 'Male and Female']
cancer_sites = ['All Cancer Sites Combined','Brain and Other Nervous System','Cervix','Colon and Rectum','Corpus and Uterus, NOS','Esophagus','Female Breast','Female Breast, <i>in situ</i>','Hodgkin Lymphoma','Kaposi Sarcoma','Kidney and Renal Pelvis','Larynx','Leukemias','Liver and Intrahepatic Bile Duct','Lung and Bronchus','Melanomas of the Skin','Mesothelioma','Myeloma','Non-Hodgkin Lymphoma','Oral Cavity and Pharynx','Ovary','Pancreas','Prostate','Stomach','Testis','Thyroid','Urinary Bladder']
years        = range(1999, 2011)

db.define_table(DB_TABLENAME,
    Field('AREA', 'string', length=100, default=states[0]), 
    Field('AGE_ADJUSTED_CI_LOWER', 'float', default=0),
    Field('AGE_ADJUSTED_CI_UPPER', 'float', default=0),
    Field('AGE_ADJUSTED_RATE', 'float', default=0),
    Field('COUNT', 'integer', default=0),
    Field('EVENT_TYPE', 'string', length=100, default=event_types[0]),
    Field('POPULATION', 'integer', default=0),
    Field('RACE', 'string', length=100, default=races[0]),
    Field('SEX', 'string', length=100, default=sex[0]), 
    Field('SITE', 'string', length=500, default=cancer_sites[0]),
    Field('YEAR', 'integer', default=years[0]),
    Field('CRUDE_CI_LOWER', 'float', default=0),
    Field('CRUDE_CI_UPPER', 'float', default=0),
    Field('CRUDE_RATE', 'float', default=0),
    format='%(email)s (%(id)s)', migrate=False)