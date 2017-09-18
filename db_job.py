## Emily Van Laarhoven and Marissa Okoli
## db_job.py
## Last modified: 5/10/2017
## Contains functions which interact with db to insert job

import dbconn2
import MySQLdb
import os
from oddjobs_dsn import DSN

## global variables
DATABASE = 'oddjobs_db'
DEBUG = False

def create_job(cursor,form_info):
    '''inserts a new job into the db and returns True when successful'''
    ## insert new job into db with None jid
    q1 = "Insert into job values (%s,%s,%s,%s,%s,%s,%s,%s,1);" #1 = available
    cursor.execute(q1,getInputs(form_info))
    ## update jid
    new_jid = cursor.lastrowid
    q2 = "Update job set jid=%s where jid is null;"
    cursor.execute(q2,[new_jid])
    ## check if insertion was successful and return boolean
    q3 = "Select count(*) from job where jid=%s;"
    cursor.execute(q3,[new_jid])
    return int(cursor.fetchone()['count(*)']) == 1

def getInputs(form_info):
    '''returns list of inputs for query from form'''
    jid = None
    title = form_info['title']
    description = form_info['description']
    location = form_info['location']
    dt = form_info['dt']
    pay = form_info['pay']
    poster = form_info['poster']
    skills_required = form_info['skills_required']
    inputs = [jid,title,description,location,dt,pay,poster,skills_required]
    return inputs








