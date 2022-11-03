#! /usr/bin/python3.5

import cgi
import sys
import MySQLdb
from htmlvar import *
import os
import http.cookies

con = MySQLdb.connect(host='localhost', user='honeypon', passwd='pon', db='honeypon')
cursor = con.cursor()

form = cgi.FieldStorage()
clientename =  form.getvalue('nombrecliente')
clientedir =  form.getvalue('dircliente')
clienteid =  form.getvalue('idcliente')
plancliente = form.getvalue('plancliente')
boton = 0

if ("bajacliente") in form:
	boton = 'bajabutton'


if boton == 'bajabutton':
	sqldeleteclient = "DELETE FROM clientes WHERE ID = %s" % clienteid
	cursor.execute(sqldeleteclient)
	con.commit()
	

sqlclientlist = "SELECT t1.Nombre, t1.Direccion, t1.ID, t1.OLT, t2.Nombre FROM clientes AS t1, planes AS t2 WHERE t1.Plan = t2.ID ORDER BY t1.ID"
cursor.execute(sqlclientlist)
resultclient = cursor.fetchall()

sqlontverify = "SELECT `ID Servicio` FROM ont"
cursor.execute(sqlontverify)
resultont = cursor.fetchall()

print("content-type: text/html\n\n")
print(HTMLHEADER)

if 'HTTP_COOKIE' in os.environ:
	cookie_string=os.environ.get('HTTP_COOKIE')
	c=http.cookies.SimpleCookie()
	c.load(cookie_string)
	if c['honeypon'].value == "honeyponlogin":
		print("""
			<div class="container-fluid">
				<div class="row">
					<div class="col-md-12">
						<div class="page-header">
			<h1>
				<img alt="honeypon logo" src="/images/honeyponbete.png" />
			</h1>
						</div>
					</div>
				</div>
			</div>
			""")


		print("""<div class="col-md-12">
					<a href="/main.py" style="text-decoration: none;font-size: 15px;">Volver&nbsp;<span class="glyphicon glyphicon-log-out"></span></a>
				</div>""")

		# Comienzo menú de navegación
		print('<div class="col-md-12" style="margin-top:50px">')
		print('<div id="pageNavPosition"></div>')
		print('</div>')
		# Fin menú de navegación

		print(tablacliente)
		idm = 1

		for row in resultclient:
			if str(row[2]) in str(resultont):
				ontdata = "SELECT t2.SN, t2.`ONT ID`, t2.Estado FROM ont AS t2, clientes AS t1 WHERE t1.ID = t2.`ID Servicio` AND t1.ID = %s" % row[2]
				cursor.execute(ontdata)
				resultontdata = cursor.fetchone()
				modal3 = """
					<!-- Modal -->
					<div id="myModal%s" class="modal fade" role="dialog">
					  <div class="modal-dialog">

						<!-- Modal content-->
						<div class="modal-content">
						  <div class="modal-header" style="text-align:center; background-color:#FEA126">
							<button type="button" class="close" data-dismiss="modal">&times;</button>
							<h4 class="modal-title" style="font-size:20px; color:white;">Datos de la ONT</h4>
						  </div>
						  <div class="modal-body">
							<p style="font-size:16px"><b>Número de serie:&nbsp&nbsp</b>%s</p>
							<p style="font-size:16px"><b>ONT ID:&nbsp&nbsp</b>%s</p>
							<p style="font-size:16px"><b>Estado:&nbsp&nbsp</b>%s</p>
						  </div>
						</div>

					  </div>
					</div>
					""" %(idm, resultontdata[0], resultontdata[1], resultontdata[2])

				print('<tr class="success" id="success">')
				print('<td align="center">',row[0],'</td>')
				print('<td align="center">',row[1],'</td>')
				print('<td align="center">',row[2],'</td>')
				print('<td align="center">',row[4],'</td>')
				print('<td align="center">',row[3],'</td>')
				print('<td align="center">662445285</td>')
				print('<td align="center"><form method="post" action="/cgi-bin/altacliente.py"><button type="submit" class="btn btn-primary btn-xs" name="modificarcliente" style="margin-left:10px"><i class="glyphicon glyphicon-wrench"></i></button>'+
				'<button type="submit" class="btn btn-danger btn-xs" name="bajacliente" style="margin-left:10px"><i class="glyphicon glyphicon-remove"></i></button>')
				if resultontdata[2] == 'Activada':
					print('<button type="button" class="btn btn-success btn-xs" data-target="#myModal%s" data-toggle="modal" style="margin-left:6px"><span class="glyphicon glyphicon-hdd"></span></button></form></td>' %idm)
				else:
					print('<button type="button" class="btn btn-warning btn-xs" data-target="#myModal%s" data-toggle="modal" style="margin-left:6px"><span class="glyphicon glyphicon-hdd"></span></button></form></td>' %idm)
				print(modal3)
				print('</tr>')
				idm += 1

			else:
				print('<tr class="danger" id="danger">')
				print('<td align="center">',row[0],'</td>')
				print('<td align="center">',row[1],'</td>')
				print('<td align="center">',row[2],'</td>')
				print('<td align="center">',row[4],'</td>')
				print('<td align="center">',row[3],'</td>')
				print('<td align="center">662445285</td>')
				print('<td align="center"><form method="post" action="/cgi-bin/altacliente.py"><button type="submit" class="btn btn-primary btn-xs" name="modificarcliente" style="margin-left:10px"><i class="glyphicon glyphicon-wrench"></i></button>'+
				'<button type="submit" class="btn btn-danger btn-xs" name="bajacliente" style="margin-left:10px"><i class="glyphicon glyphicon-remove"></i></button>'+
				'<button type="button" class="btn btn-danger btn-xs" style="margin-left:10px" disabled> <span class="glyphicon glyphicon-hdd"></span></button></form></td>')
				print('</tr>')



		print(tablaclientefin)

		print(javacode)

	else:
		print("""<script language="javascript">
		window.location.href = "/index.py"
		</script>""")

else:
	print("""<script language="javascript">
	window.location.href = "/index.py"
	</script>""")


print(HTMLFIN)
