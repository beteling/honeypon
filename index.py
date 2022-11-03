#! /usr/bin/python3.5

from htmlvar import *
import os
import http.cookies

honeycookie = "honeypon=honeyponlogin"

print("content-type: text/html\n\n")

if 'HTTP_COOKIE' in os.environ and honeycookie in os.environ.get('HTTP_COOKIE'):
	cookie_string=os.environ.get('HTTP_COOKIE')
	c=http.cookies.SimpleCookie()
	c.load(cookie_string)
	print(HTMLHEADER)
	print("""<script language="javascript">
	window.location.href = "/honeypon/main.py"
        </script>""")
	print(HTMLFIN)


else:
	print(HTMLHEADER)
	print("""
	<div class="container-fluid">
	<div class="col-md-12">
	<div class="page-header">
	<h1>
	<img alt="honeypon logo" src="/honeypon/images/honeyponbete.png" />
	</h1>
	</div>
	</div>
	</br>
	</br>
	<div class="row">
	
		<div class="col-md-12">
		<div class="testbox">
			<form role="form" method="post" action="/honeypon/login.py">
				<div class="form-group" style="width:200px; margin-left:auto; margin-right:auto; color:#195F82">

				<label for="InputUser" style="margin-top:35px">
						<span class="glyphicon glyphicon-user"></span> Usuario
					</label>
					<input type="text" id="username" name="username" class="form-control" required="required" autofocus="autofocus" />
				</div>
				<div class="form-group" style="width:200px; margin-left:auto; margin-right:auto; color:#195F82">

					<label for="InputPassword1">
						<span class="glyphicon glyphicon-lock"></span> Contraseña
					</label>
					<input type="password" id="password" name="password" class="form-control" required="required" />
				</div>
				<div style="text-align:center">
				<button class="btn btn-md btn-primary" style="width:200px;border-radius:0" type="submit" name="login" value="login">Login</button>
				</div>
				<br/>
				<br/>
			</form>
			</div>
		</div>
	</div>
	</div>
	</BODY>
	</HTML>""")
