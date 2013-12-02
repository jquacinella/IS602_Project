#!/usr/bin/python
''' load_data.py - Reads in SQL data to fill in the MySQL schema. 

IS602 - Final Project - James Quacinella
'''

import re
import MySQLdb
import pandas

### Config options for DB

DB_HOST      = "localhost"
DB_USERNAME  = "is602"
DB_PASSWORD  = "-------"
DB_NAME      = "is602"
DB_TABLENAME = "cancer_data_by_area"

# Name of the table columns
DB_COLUMNS = ['AREA',
            'AGE_ADJUSTED_CI_LOWER', 
            'AGE_ADJUSTED_CI_UPPER', 
            'AGE_ADJUSTED_RATE',
            'COUNT',
            'EVENT_TYPE',
            'POPULATION',
            'RACE',
            'SEX',
            'SITE',
            'YEAR',
            'CRUDE_CI_LOWER',
            'CRUDE_CI_UPPER',
            'CRUDE_RATE']


### Main Process

def main():
    # Connect to local database
    print "Connecting to DB ..."
    db = MySQLdb.connect(host=DB_HOST, 
                        user=DB_USERNAME, 
                        passwd=DB_PASSWORD,  
                        db=DB_NAME)
    cur = db.cursor() 
    print "Connected!"
    
    # Read data from file
    print "Reading data ..."
    df = pandas.io.parsers.read_csv('data/cancer/BYAREA.TXT', sep='|')
    print "Done reading data from file!"

    # Loop through data frame and create one big insert command
    print "Executing queries ..."
    query_prefix = "INSERT INTO %s.%s (%s) VALUES " % (DB_NAME, DB_TABLENAME, ",".join(DB_COLUMNS))
    query_values = '''\
('%(AREA)s', \
%(AGE_ADJUSTED_CI_LOWER)s, \
%(AGE_ADJUSTED_CI_UPPER)s, \
%(AGE_ADJUSTED_RATE)s, \
%(COUNT)s, \
'%(EVENT_TYPE)s', \
%(POPULATION)s, \
'%(RACE)s', \
'%(SEX)s', \
'%(SITE)s', \
%(YEAR)s, \
%(CRUDE_CI_LOWER)s, \
%(CRUDE_CI_UPPER)s, \
%(CRUDE_RATE)s)'''

    # Loop through every row of the data set
    count = 0
    for index, row in df.iterrows():
        # Create the VALUES portion of the query
        values = query_values % row

        # Convert NULL values from data file into SQL NULL values
        values = values.replace("~", "NULL")
        values = values.replace(" .,", " NULL,")
        values = values.replace(" -,", " NULL,")
        values = values.replace(" -)", " NULL)")
        
        # Create INSERT query
        query = query_prefix + values
        
        # Execute the query, and log any errors
        try:
            cur.execute(query)
        except Exception, e:
            print "ERROR: %s" % query
        
        # Print current row counr
        count = count + 1
        print "Query count: %d\r" % count,

    print "Done loading data!"

    # Commit the DB transaction
    print "Commiting ..."
    db.commit()
    print "Done commiting data!"

    # Cleanup
    db.close()

if __name__ == "__main__":
    main()