#! /usr/bin/python3.5

import cgi
import sys
import MySQLdb, MySQLdb.cursors # importa cursor para array asociativo
from htmlvar import *
import os
import http.cookies
from pysnmp.entity.rfc3413.oneliner import cmdgen

cmdGen = cmdgen.CommandGenerator()

con = MySQLdb.connect(host='localhost', user='honeypon', passwd='pon', db='honeypon', cursorclass=MySQLdb.cursors.DictCursor) # cursorclass para array asociativo
cursor = con.cursor()