# Detailed Project Description

Using the data that was just released this year by the CDC on yearly incidents of cancer, this project will investigate which states have shown an increase or decrease in cancer incidents from 1999 - 2010. This analysis can be broken down by many factors, including age group, race and cancer site. The end product will be a simple web interface, giving the end user the ability to choose how to slice and dice the data, resulting in a graph output.

My plan is to extract the data in Python and store the data in pandas. This will allow me to graph the data in various ways. This is to get a feel of the data. Once this is done, the data will be loaded into a MySQL database. A simple HTML frontend will point to a small HTTP backend (using a Python Web Framework like flask, web2py, etc), which will query the MySQL database and result in a graphical output using the D3.js library (or possibly Bokeh). This interface can then be used to investigate changes in cancer incidences or mortality rates broken down by many variables, including race, age range, sex and state. 

The CDC provides a similar web interface, that is much more detailed than what I had in mind, located here: http://apps.nccd.cdc.gov/DCPC_INCA/DCPC_INCA.aspx. However, the interface here will focus on showing changes over time. The CDC interface can only show one year at a time.



## Technologies Used

### Data

- United States Cancer Statistics (USCS) - http://www.cdc.gov/cancer/npcr/uscs/download_data.htm

### Language

- Python - http://www.python.org/
- Pandas - http://pandas.pydata.org/

### Database

- MySQL - http://mysql.org

### Web Layer (not chosen yet)

- Web2py - http://web2py.com/
- Flask - http://flask.pocoo.org/

### Visualization

- Pylab - http://wiki.scipy.org/PyLab
- D3.js - http://d3js.org/
- Bokeh - https://github.com/ContinuumIO/bokeh


## Proposed Layout

<pre>
cancer/
|-- data/
|    |-- cancer/                # Raw data from CDC
|    |-- data.pandas            # Pickled version of pandas data frame of loaded data
|    |-- cancer_data.sql        # MySQL data SQL files
|    |-- cancer_schema.sql      # MySQL schema
|-- web/                        # Web frontend and backend files (including JS, CSS, etc) (Layput TBD)
|    |-- static/
|    |   |-- html/
|    |   |-- css/
|    |   |-- js/
|    |-- ...
</pre>

## Schema

<pre>
AREA - String - Name of the state (50 possible values)
AGE_ADJUSTED_CI_LOWER - Float - Lower bound of 95% confidence interval of the crude rate
AGE_ADJUSTED_CI_UPPER - Float - Upper bound of 95% confidence interval of the crude rate
AGE_ADJUSTED_RATE - Float - Rate of incidence per 100,000 persons, 
COUNT - Integer - Number of 'event types' in a given population
EVENT_TYPE - String - Cancer incidence or mortality event (2 values, incidence or mortality)
POPULATION - Integer - Total people in a given population
RACE - String - Race of Sample (6 possible values)
SEX - String - Sex of Sample (3 possible values: M, F, Both)
SITE - String - Site of the cancer (27 possible values)
YEAR - Integer - Year of data collection for this given population
CRUDE_CI_LOWER - Float - Lower bound of 95% confidence interval of the crude rate
CRUDE_CI_UPPER - Float - Upper bound of 95% confidence interval of the crude rate
CRUDE_RATE - Float - Rate of incidence per 100,000 persons
</pre>

## General Steps

- [x] Load data from .TXT file into pandas
- [ ] Use pylab to graph the data in various ways, get familiar with data
- [ ] Load data into MySQL
- [ ] Create code to generate a query to the database based on various parameters
- [ ] Create simple backend that returns JSON of data to plot based on given HTTP parameters
- [ ] Create simple frontend using a JS visualization library, which used backend via jQuery
- [ ] Use frontend to look if certain rates are increasing more quickly in certain areas over time


## Ideas to Expand in the Future

- Can use the other data files to include different ways to break the data down. I am currently using the BYAREA.txt file; BYAGE.txt and BYSITE.txt can provide further insight as that data is broken down by census age groups and cancer sites, respectively. 
