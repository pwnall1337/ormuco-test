#!/usr/bin/env python

import sqlite3 as sql
import sys

con=sql.connect('ormuco.db')
cur=con.cursor()

table_data=("CREATE TABLE data(NAME varchar(255) NOT NULL UNIQUE,"
            "COLOR varchar(255),ANIMAL varchar(255))")
try:
    cur.execute(table_data)
except:
    print "Does table data already exist?"
    pass
