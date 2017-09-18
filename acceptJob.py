#!/usr/local/bin/python2.7

'''Author: Emily Van Laarhoven Marissa Okoli
   CS 304 OddJobs Beta
   Last modified: 5/12/2017
   acceptJob.py
Helper module for flask application for user to accept job, creating a row in the ratings
table and removing the job from the jobs table
Contains functions for connecting to the database and executing prepared queries port:7332	
'''

import sys
import MySQLdb
import dbconn2
import db_curs
from oddjobs_dsn import DSN

def acceptJob(cursor, uid, jid):
	'''Marks job from the job table as unavailable and adds info to the rating table.'''
	cursor.execute('select poster from job where jid= %s', (jid,))
	res = cursor.fetchone()
	eid = '{poster}'.format(**res)
	cursor.execute('update job set available=0 where jid= %s', (jid,))
	cursor.execute('insert into rating values (%s, %s, %s, Null, Null, Null, Null)', (jid,uid, eid))
	cursor.execute('select * from rating where jid= %s', (jid,))
	rating = cursor.fetchone()
	return (rating is not None)

def main(uid, jid):
	'''Checks if actor is in database, if not inserts actor and returns success message,
    else returns message saying actor is already in the database'''
	if int(uid) != 0:
		return acceptJob(db_curs.cursor(), uid, jid)
	else:
		print "only enter 0 to confirm a deletion"
		return False

if __name__ == '__main__':
	print main(1, 4)
