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

### Visualization

- Pylab - http://wiki.scipy.org/PyLab
- D3.js - http://d3js.org/


## Project Layout

<pre>
cancer/
|-- data/
|    |-- MySQL/                  # MySQL schema and data
|    |-- cancer/                 # Raw data from CDC
|-- scripts/
|    |-- load_data.py            # Script that loads the MySQL data
|    |-- load_schema.py          # Script that loads the MySQL schema
|-- web/                         # Web2py installation
|    |-- applications/is602      # The main is602_final application
|              |-- controller    # Location of Python code behind the REST request
|              |-- model         # Location of DB model
|              |-- static        # Location of JS and CSS (Bootstrap) files

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
- [x] Use pylab to graph the data in various ways, get familiar with data
- [x] Load data into MySQL
- [x] Create code to generate a query to the database based on various parameters
- [x] Create simple backend that returns JSON of data to plot based on given HTTP parameters
- [x] Create simple frontend using a JS visualization library, which used backend via jQuery
- [ ] Use frontend to look if certain rates are increasing more quickly in certain areas over time

## Instructions

If you want to see the end result, which is a basic web interface to the CDC data, you can visit https://jquacinella.pythonanywhere.com/is602_project/. The web2py architecture is being hosted there for the time being.

If you want to do this yourself, here are the steps

1. Clone this repo
  * ``git clone https://github.com/jquacinella/IS602_Project.git``
2. Change directory to the data/cancer
  * ``cd IS602_Project/data/cancer``
3. Unzip the USCS_1999_2010_ASCII.zip file, which should extract a file called BYAREA.txt 
  * Github has a file size limit, hence this is needed
4. Navigate to the top-level directory
  * ``cd ../../``
5. Setup a local MySQL instance
  * Either use:
    
    ```python
    DB_HOST      = "localhost"
    DB_USERNAME  = "is602"
    DB_PASSWORD  = "test1234"
    DB_NAME      = "is602"
    DB_TABLENAME = "cancer_data_by_area"
    ```
  * Or record the username, password, database, and table name and edit the following scripts
      * ``vi scripts/load_schema.py``
      * ``vi scripts/load_data.py``
      * ``vi applications/is602_final/models/db.py``
6. Run the schema and data importer (this may take a while)
  * ``python scripts/load_schema.py``
  * ``python scripts/load_data.py`` 
7. Change to the web2py-based web/ directpry
  * ``cd web/``
8. Start the web-server (Change the port number if needed)
  * ``python web2py.py --nogui -p 8080 -a test1234``
9. Open the web interface, which should be located here: http://127.0.0.1:8080/is602_project/

## Ideas to Expand in the Future

- Can use the other data files to include different ways to break the data down. I am currently using the BYAREA.txt file; BYAGE.txt and BYSITE.txt can provide further insight as that data is broken down by census age groups and cancer sites, respectively. 
