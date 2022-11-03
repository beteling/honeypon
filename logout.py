#! /usr/bin/python3.5

import cgi
import os
import MySQLdb
from htmlvar import *
import http.cookies

# set the cookie to expire
c=http.cookies.SimpleCookie()
c['honeypon']=''
c['honeypon']['expires']='Thu, 01 Jan 1970 00:00:00 GMT'
print(c)
print("content-type: text/html\n\n")
print(HTMLHEADER)
print("""<script language="javascript">
window.location.href = "/honeypon/index.py"
</script>""")


print(HTMLFIN)
