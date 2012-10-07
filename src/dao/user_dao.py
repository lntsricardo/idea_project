#!/usr/bin/python
# -*- coding: utf-8 -*-

import psycopg2
import sys

def select_user(id_user):
    '''
    select_user(number)
    Selects only one result from the table user according to the id_user passed.

    >>> select_user(1)
    user
    '''
    con = None

    try:
     
        con = psycopg2.connect(database='idea_database', user='idea', password='idea') 
        cur = con.cursor()
        cur.execute('SELECT * FROM USER WHERE ID_USER = ' + id_user)          
        user = cur.fetchone()
   	print '## INFO: User selected succesfully!!!'
    

    except psycopg2.DatabaseError, e:
        print '## ERROR: %s' % e    
        ##sys.exit(1)
    
    
    finally:
    
        if con:
            con.close()
	return user


def insert_user(id_user, name, id_type):
    '''
	Write description here!!!!!!
    '''
    con = None

    try:

        con = psycopg2.connect(database='idea_database', user='idea', password='idea')
        cur = con.cursor()
        cur.execute('INSERT INTO PERSON VALUES ('+ id_user + ', ' + name + ', ' + name + ', ' + name + ', ' + id_type)
        print '## INFO: User selected succesfully!!!'


    except psycopg2.DatabaseError, e:
        print '## ERROR: %s' % e
        ##sys.exit(1)


    finally:

        if con:
            con.close()
