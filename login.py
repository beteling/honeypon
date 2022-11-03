#! /usr/bin/python3.5

import cgi
import os
import hashlib
import MySQLdb
from htmlvar import *
import http.cookies

form = cgi.FieldStorage()
user =  form.getvalue('username')
password = form.getvalue('password')

hash = hashlib.md5()
hash.update(password.encode())
hashpassword = hash.hexdigest()

con = MySQLdb.connect(host='localhost', user='honeypon', passwd='pon', db='honeyponv2')
cursor = con.cursor()
sqluser = "SELECT USERNAME, PASSWORD FROM users WHERE USERNAME = '%s' AND PASSWORD = '%s'" % (user, hashpassword)


if cursor.execute(sqluser):
	# create the cookie
	c=http.cookies.SimpleCookie()
	# assign a value
	c['honeypon']='honeyponlogin'
	# set the xpires time
	c['honeypon']['expires']=1*1*3*60*60
	print(c)
	print("content-type: text/html\n\n")
	print(HTMLHEADER)
	print("""<script language="javascript">
    window.location.href = "/honeypon/main.py"
	</script>""")


else:
	print("content-type: text/html\n\n")
	print(HTMLHEADER)
	print("""<div class="container-fluid">
	<div class="col-md-12">
	<div class="page-header">
	<h1>
	<img alt="honeypon logo" src="/honeypon/images/honeyponbete.png" />
	</h1>
	</div>
	</div>""")
	print('<div class="col-md-12">')
	print('<div class="alert alert-danger alert-dismissable">')
	print('<h4>Error!</h4>Usuario o contraseña incorrectos. <a href="/honeypon/index.py" class="alert-link">Volver</a>')
	print('</div>')
	print('</div>')

print(HTMLFIN)
