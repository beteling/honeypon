#! /usr/bin/python3.5

import cgi
import sys
from htmlvar import *
from config import *
import os
import http.cookies
from pysnmp.entity.rfc3413.oneliner import cmdgen

cmdGen = cmdgen.CommandGenerator()
licenseverify = "SELECT Validacion FROM licencia WHERE Validacion = 1"


if 'HTTP_COOKIE' in os.environ:
    cookie_string=os.environ.get('HTTP_COOKIE')
    honeycookie = "honeypon=honeyponlogin"
    #if c['honeypon'].value == 'honeyponlogin':
    if honeycookie in cookie_string:

        if cursor.execute(licenseverify):

            print("content-type: text/html\n\n")
            print(header_css_scripts) # HP2.0

            print(pestañas_navegacion) # HP2.0

            #c=http.cookies.SimpleCookie()
            #c.load(cookie_string)
            #c['honeypon']['expires']=1*1*7*60*60
            #print(c)
            #print(HTML)
            print("<script>$('#menuplanes').css('background-color','#FEA126');</script>")

            #print('<div class="col-md-12">')
            #print('<div id="pageNavPosition"></div>')
            #print('</div>')
            print('<div class="col-md-4">')
            print('<h2 style="color:#1A5F82;margin-top:40px">Planes de datos</h2>')
            print('</div>')

            #Boton alta de nuevo cliente
            print("""<div class='col-md-3' style='float:right;margin-top:40px'>
                        <div class= 'row tooltip-demo'>
                         <a style='cursor:pointer;float:right;' class='quick-btn alta-btn' data-target='#myModalplanes' data-toggle='modal'>
                             <i class='fa fa-2x fa-sort-amount-desc' data-toggle='tooltip' data-placement='bottom' title='' data-original-title='Declarar Tabla de Tráfico'></i>
                        </a>
						<a style='cursor:pointer;float:right;' class='quick-btn alta-btn' data-target='#myModalplanes' data-toggle='modal'>
                             <i class='fa fa-2x fa-plus' data-toggle='tooltip' data-placement='bottom' title='' data-original-title='Nuevo Plan'></i>
                        </a>

                        </div>

					</div>""")


            # Fin botón alta y menú de navegación

            # COMIENZO TABLA PLANES
            sqlplanlist = "SELECT t1.Nombre, t2.CIR, t2.PIR, t4.Subida, t3.Nombre, t1.ID, t1.OLT FROM planes AS t1, tablatrafico AS t2, olt AS t3, dba AS t4 WHERE t1.Subida = t4.Subida AND t1.tabla = t2.ID AND t1.OLT = t3.ID"
            cursor.execute(sqlplanlist)
            resultplan = cursor.fetchall()

            print(tablaplanes)

            idmc = 1


            for row in resultplan:

                cir = row[1]/1024
                pir = row[2]/1024
                dba = row[3]/1024
                print('<tr id="%s" class="active">' %row[5])
                print('<td align="center">',row[0],'</td>')
                print('<td align="center">',cir,'Mbps</td>')
                print('<td align="center">',pir,'Mbps</td>')
                print('<td align="center">',dba,'Mbps</td>')
                print('<td align="center">',row[4],'</td>')



                print('<td align="center"><form action="/cgi-bin/editarplan.py" method="post">'+
                '<input type="hidden" name="nombreplan" value="%s"/>'%row[0]+
                '<input type="hidden" name="CIR" value="%s"/>'%row[1]+
                '<input type="hidden" name="PIR" value="%s"/>'%row[2]+
                '<input type="hidden" name="plansubida" value="%s"/>'%row[3]+
                '<input type="hidden" name="oltid" value="%s"/>'%row[6]+
                '<input type="hidden" name="idplan" value="%s"/>'%row[5])

                print('<button title="Modificar" type="submit" class="btn btn-primary btn-xs" name="modificarplan" value="botonedit" style="margin-left:10px"><i class="glyphicon glyphicon-wrench"></i></button>')
                print('<button title="Borrar plan" type="button" href="#modal-borrarplan%s" data-toggle="modal" class="btn btn-danger btn-xs" style="margin-left:10px"><i class="glyphicon glyphicon-trash" style="margin-right:0.8px"></i></button></form></td>' %idmc)

                print('</tr>')



            print(tablaplanesfin)

			# COMIENZO TABLA DBA
            sqldbalist = "SELECT t1.Nombre, t1.Subida, t1.OLT, t2.Nombre, t1.ID FROM dba AS t1, olt AS t2 WHERE t2.ID = t1.OLT"
            cursor.execute(sqldbalist)
            resultdba = cursor.fetchall()

            print('<div class="col-md-4"><h2 style="color:#1A5F82;margin-top:40px">DBA</h2></div>')
            print(tabladba)

            idmc = 1


            for row in resultdba:


                print('<tr id="%s" class="active">' %row[4])
                print('<td align="center">',row[0],'</td>')
                print('<td align="center">',row[1],'Kbps</td>')
                print('<td align="center">',row[3],'</td>')

                print('<td align="center"><form action="/cgi-bin/editarplan.py" method="post">'+
                '<input type="hidden" name="nombredba" value="%s"/>'%row[0]+
                '<input type="hidden" name="subida" value="%s"/>'%row[1]+
                '<input type="hidden" name="oltid" value="%s"/>'%row[2]+
                '<input type="hidden" name="idplan" value="%s"/>'%row[4])

                print('<button title="Modificar" type="submit" class="btn btn-primary btn-xs" name="modificarplan" value="botonedit" style="margin-left:10px"><i class="glyphicon glyphicon-wrench"></i></button>')
                print('<button title="Borrar plan" type="button" href="#modal-borrarplan%s" data-toggle="modal" class="btn btn-danger btn-xs" style="margin-left:10px"><i class="glyphicon glyphicon-trash" style="margin-right:0.8px"></i></button></form></td>' %idmc)

                print('</tr>')



            print(tabladbafin)

			# COMIENZO TABLA TABLAS DE TRAFICO

            sqltraficolist = "SELECT t1.Nombre, t1.CIR, t1.PIR, t2.Nombre, t1.ID, t1.OLT FROM tablatrafico AS t1, olt AS t2 WHERE t2.ID = t1.OLT"
            cursor.execute(sqltraficolist)
            resulttrafico = cursor.fetchall()

            print('<div class="col-md-4"><h2 style="color:#1A5F82;margin-top:40px">Tablas de tráfico</h2></div>')

            print(tablatrafico)

            for row in resulttrafico:


                print('<tr id="%s" class="active">' %row[4])
                print('<td align="center">',row[0],'</td>')
                print('<td align="center">',row[1],'kbps</td>')
                print('<td align="center">',row[2],'kbps</td>')
                print('<td align="center">',row[3],'</td>')




                print('<td align="center"><form action="/cgi-bin/editarplan.py" method="post">'+
                '<input type="hidden" name="nombretrafico" value="%s"/>'%row[0]+
                '<input type="hidden" name="CIR" value="%s"/>'%row[1]+
                '<input type="hidden" name="PIR" value="%s"/>'%row[2]+
                '<input type="hidden" name="oltid" value="%s"/>'%row[5]+
                '<input type="hidden" name="idplan" value="%s"/>'%row[4])

                print('<button title="Modificar" type="submit" class="btn btn-primary btn-xs" name="modificarplan" value="botonedit" style="margin-left:10px"><i class="glyphicon glyphicon-wrench"></i></button>')
                print('<button title="Borrar plan" type="button" href="#modal-borrarplan%s" data-toggle="modal" class="btn btn-danger btn-xs" style="margin-left:10px"><i class="glyphicon glyphicon-trash" style="margin-right:0.8px"></i></button></form></td>' %idmc)

                print('</tr>')


            idmc += 1
            print(tablatraficofin)


        else:
            print("content-type: text/html\n\n")
            print(HTMLHEADER)
            print(LICENSEHEADER)
            print('<div class="col-md-12">')
            print('<div class="alert alert-danger alert-dismissable">')
            print('<h4>Error!</h4>La licencia del software no es compatible con el hardware actual')
            print('</div>')
            print('</div>')

    else:
        print("content-type: text/html\n\n")
        print(HTMLHEADER)
        print("""<script language="javascript">
        window.location.href = "/honeypon/index.py"
        </script>""")

else:
    print("content-type: text/html\n\n")
    print(HTMLHEADER)
    print("""<script language="javascript">
    window.location.href = "/honeypon/index.py"
    </script>""")

print(javacode)
print(javadatatableplanes)
print(HTMLFIN)
