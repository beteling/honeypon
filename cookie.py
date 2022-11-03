#! /usr/bin/python3.5

import os
import http.cookies

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
window.location.href = "/main.py"
</script>""")

print(HTMLFIN)
