#!/usr/bin/python3

from MySQLdb import connect

db = connect(host='127.0.0.1', user='python', passwd='4linux123', db='python')


cursor = db.cursor()
