#!/usr/bin/python
''' load_schema.py - Reads in SQL query to create the MySQL schema. 

IS602 - Final Project - James Quacinella
'''

import MySQLdb

### Config options for DB

DB_HOST      = "localhost"
DB_USERNAME  = "is602"
DB_PASSWORD  = "-------"
DB_NAME      = "is602"
DB_TABLENAME = "cancer_data_by_area"

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
    
    # Read schema loading query from file
    print "Reading query ..."
    f = open("data/MySQL/schema.sql")
    query = "".join([line.strip() for line in f.readlines()])
    print "Done reading query from file: %s" % query

    # Execute and commit the table creation query
    print "Executing query ..."
    cur.execute(query % (DB_NAME, DB_TABLENAME))
    db.commit()
    print "Done!"


if __name__ == "__main__":
    main()