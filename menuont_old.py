#! /usr/bin/python3.5

import cgi
import sys
import MySQLdb
from htmlvar import *
from config import *
import os
import http.cookies
from pysnmp.entity.rfc3413.oneliner import cmdgen

cmdGen = cmdgen.CommandGenerator()

con = MySQLdb.connect(host='localhost', user='honeypon', passwd='pon', db='honeypon')
cursor = con.cursor()
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
            print("<script>$('#menuont').css('background-color','#FEA126');</script>")
            sqlontlist = "SELECT t1.SN, t1.`ONT ID`, t1.`ID Servicio`, t1.Estado, t2.Nombre, t2.Direccion, t4.Nombre, t3.Nombre, t2.DNI, t2.Telefono, t1.Modelo FROM ont AS t1, clientes AS t2, planes AS t3, olt AS t4 WHERE t1.`ID Servicio` = t2.ID AND t2.Plan = t3.ID AND t2.olt = t4.ID ORDER BY t1.`ONT ID`"
            cursor.execute(sqlontlist)
            resultont = cursor.fetchall()

            # Comienzo botón alta y menú de navegación

            print(modalont)

            print('<div class="col-md-4">')
            print('<h2 style="color:#1A5F82;margin-top:40px">Lista de ONT</h2>')
            print('</div>')
            #Boton alta de nueva ONT
            print("""<div class='col-md-1' style='float:right;margin-top:40px'>
                        <div class= 'row tooltip-demo'>
						<a style='cursor:pointer' class='quick-btn alta-btn' data-target='#myModal' data-toggle='modal'>
                             <i class='fa fa-2x fa-hdd-o' data-toggle='tooltip' data-placement='bottom' title='Nueva alta' data-original-title='Alta ONT'></i>
                        </a>
                        </div>
					</div>""")
            # Fin botón alta y menú de navegación


            print(tablaont)


            idm = 1
            for row in resultont:

                modalclient = """
                    <!-- Modal -->
                    <div id="myModal%s" class="modal fade" role="dialog">
                      <div class="modal-dialog">

                        <!-- Modal content-->
                        <div class="modal-content">
                          <div class="modal-header" style="text-align:center; background-color:#FEA126">
                            <button type="button" class="close" data-dismiss="modal">&times;</button>
                            <h4 class="modal-title" style="font-size:20px; color:white;">Datos del cliente</h4>
                          </div>
                          <div class="modal-body">
                            <p style="font-size:16px"><b>Nombre:&nbsp&nbsp</b>%s</p>
                            <p style="font-size:16px"><b>Dirección:&nbsp&nbsp</b>%s</p>
                            <p style="font-size:16px"><b>Teléfono:&nbsp&nbsp</b>%s</p>
                            <p style="font-size:16px"><b>DNI:&nbsp&nbsp</b>%s</p>
                            <p style="font-size:16px"><b>Plan de datos:&nbsp&nbsp</b>%s</p>
                            <p style="font-size:16px"><b>OLT:&nbsp&nbsp</b>%s</p>
                          </div>

                        </div>

                      </div>
                    </div>
                    """

                # Extrae la ip de la OLT asociada a la ont
                sqloltip = "SELECT IP FROM olt WHERE Nombre = '%s'" % row[6]
                cursor.execute(sqloltip)
                oltip = cursor.fetchone()

                # Extrae la información SIP del cliente asociado a la ont
                sqlsipdata = "SELECT Extension, Secret from sip WHERE `ID Sip` = %s" % row[2]



                if row[3] == 'Desactivada':
                    print('<tr class="danger" id="danger">')
                else:
                    print('<tr class="info" id="success">')
                print('<td align="center">',row[0],'</td>')
                print('<td align="center">',row[1],'</td>')
                print('<td align="center">',row[10],'</td>')
                print('<td align="center">',row[2],'</td>')
                print('<td align="center">',row[3],'</td>')


                # Se extrae información de linea de la base de datos
                idprintont = row[1]
                sqlrxread = "SELECT Linea FROM ont WHERE `ONT ID` = '%s'" % idprintont
                cursor.execute(sqlrxread)
                linea = cursor.fetchone()
                linea = linea[0]

                # Se imprime en el registro el estado de línea de los últimos 5 minutos

                if linea == "online":
                    print('<td align="center" style="color:green">',linea,'</td>')

                elif linea == "offline":
                    print('<td align="center" style="color:#C9302C">',linea,'</td>')

                elif linea == None:
                    print('<td align="center" style="color:#FEA126">Esperando datos</td>')

                print('<td align="center" style="color:#FEA126" class="hidden">',row[4],'</td>')

                if cursor.execute(sqlsipdata):
                    sipdata = cursor.fetchone()
                    print('<td align="center"><form action="/cgi-bin/ont.py" method="post"><input type="hidden" name="sn" value=',row[0],'/><input type="hidden" name="service" value=',row[2],'/><input type="hidden" name="oltip" value=',oltip[0],'/><input type="hidden" name="extensionsip" value=',sipdata[0],'/><input type="hidden" name="secretsip" value=',sipdata[1],'/><input type="hidden" name="ontid" value="%s" /><input type="hidden" name="clientname" value="%s" />' % (idprintont,row[4]))
                else:
                    print('<td align="center"><form action="/cgi-bin/ont.py" method="post"><input type="hidden" name="sn" value=',row[0],'/><input type="hidden" name="service" value=',row[2],'/><input type="hidden" name="oltip" value=',oltip[0],'/><input type="hidden" name="ontid" value="%s" /><input type="hidden" name="clientname" value="%s" />' % (idprintont,row[4]))
                if row[3] == 'Desactivada':
                    print('<button title="Reactivar" type="submit" value="Reactivar" class="btn btn-primary btn-xs" name="altaserv", text-align=center" style="margin-left:10px"><i class="glyphicon glyphicon-ok" ></i></button>')
                else:
                    print('<button title="Desactivar" type="submit" value="Desactivar"  class="btn btn-warning btn-xs" name="bajaserv",text-align=center" style="margin-left:10px"><i class="glyphicon glyphicon-remove"></i></button>')
                print('<button title="Baja ONT" type="button" href="#modal-borraront%s" data-toggle="modal" class="btn btn-danger btn-xs" text-align=center" style="margin-left:10px"><i class="glyphicon glyphicon-trash" style="margin-right:0.8px"></i></button>' %idm)

                """if cursor.execute(sqlsipdata):
                    print('<button formtarget="_blank" title="Aprovisionar SIP" type="submit" class="btn btn-primary btn-xs" name="syncsip" value="botonsip" style="margin-left:10px"><i class="glyphicon glyphicon-earphone"></i></button>')
                else:
                    print('<button title="SIP no asociado" type="submit" class="btn btn-primary btn-xs" name="syncsip" value="botonsip" style="margin-left:10px" disabled><i class="glyphicon glyphicon-earphone"></i></button>')"""
                print('<button title="Cliente asociado" type="button" class="btn btn-info btn-xs" data-target="#myModal%s" data-toggle="modal" style="margin-left:10px"><i class="glyphicon glyphicon-user"></i></button>' %idm)
                #print('<button title="Monitor" type="button" class="btn btn-success btn-xs" style="float:right;margin-left:10px"><i class="glyphicon glyphicon-stats"></i></button>')
                print('<a onclick=\'javascript:window.open( "http://" + window.location.hostname + "/cacti/graph_view.php?style=selective&action=preview&thumbnails=false&predefined_timespan=2&filter=%s-")\' title="Monitor" class="btn btn-default btn-xs" style="float:right"><i class="glyphicon glyphicon-signal"></i></a>' %row[1])
                if row[10] == "245H" or row[10] == "HG8245H":
                    print('<a onclick=\'javascript:window.open( "http://" + window.location.hostname + ":3000/devices/00259E-HG8245H-%s")\' title="Gestionar ONT" class="btn btn-default btn-xs" style="float:right"><i class="glyphicon glyphicon-cog"></i></a>' %row[0].upper())
                elif row[10] == "245U" or row[10] == "HG8245U":
                    print('<a onclick=\'javascript:window.open( "http://" + window.location.hostname + ":3000/devices/00259E-HG8245U-%s")\' title="Gestionar ONT" class="btn btn-default btn-xs" style="float:right"><i class="glyphicon glyphicon-cog"></i></a>' %row[0].upper())
                elif row[10] == "247H" or row[10] == "HG8247H":
                    print('<a onclick=\'javascript:window.open( "http://" + window.location.hostname + ":3000/devices/00259E-HG8247H-%s")\' title="Gestionar ONT" class="btn btn-default btn-xs" style="float:right"><i class="glyphicon glyphicon-cog"></i></a>' %row[0].upper())
                elif row[10] == "010H" or row[10] == "HG8010H":
                    print('<a onclick=\'javascript:window.open( "http://" + window.location.hostname + ":3000/devices/00259E-HG010H-%s")\' title="Gestionar ONT" class="btn btn-default btn-xs" style="float:right"><i class="glyphicon glyphicon-cog"></i></a>' %row[0].upper())
                elif row[10] == "110H" or row[10] == "HG8110H":
                    print('<a onclick=\'javascript:window.open( "http://" + window.location.hostname + ":3000/devices/00259E-HG010H-%s")\' title="Gestionar ONT" class="btn btn-default btn-xs" style="float:right"><i class="glyphicon glyphicon-cog"></i></a>' %row[0].upper())
                elif row[10] == "245Q2" or row[10] == "HG8245Q2":
                    print('<a onclick=\'javascript:window.open( "http://" + window.location.hostname + ":3000/devices/00259E-HG8245Q2-%s")\' title="Gestionar ONT" class="btn btn-default btn-xs" style="float:right"><i class="glyphicon glyphicon-cog"></i></a>' %row[0].upper())
                elif row[10] == "546V" or row[10] == "HS8546V":
                    print('<a onclick=\'javascript:window.open( "http://" + window.location.hostname + ":3000/devices/00259E-HS8546V-%s")\' title="Gestionar ONT" class="btn btn-default btn-xs" style="float:right"><i class="glyphicon glyphicon-cog"></i></a>' %row[0].upper())
                elif row[10] == "EG8245H":
                    print('<a onclick=\'javascript:window.open( "http://" + window.location.hostname + ":3000/devices/00259E-EG8245H-%s")\' title="Gestionar ONT" class="btn btn-default btn-xs" style="float:right"><i class="glyphicon glyphicon-cog"></i></a>' %row[0].upper())
                elif row[10] == "HG8311" or row[10] == "311":
                    print('<a onclick=\'javascript:window.open( "http://" + window.location.hostname + ":3000/devices/00259E-HG8311-%s")\' title="Gestionar ONT" class="btn btn-default btn-xs" style="float:right"><i class="glyphicon glyphicon-cog"></i></a>' %row[0].upper())
                else:
                    print('<a onclick=\'javascript:window.open( "http://" + window.location.hostname + ":3000/devices")\' title="Gestionar ONT" class="btn btn-default btn-xs" style="float:right"><i class="glyphicon glyphicon-cog"></i></a>')
                print('<button title="Programar tarea" type="submit" class="btn btn-default btn-xs" name="program" value="botonprogram" style="float:right;margin-left:10px"><i class="glyphicon glyphicon-time"></i></button>')

                # Se extrae información de pppoe si procede
                #idcliente = row[2]
                #sqlpppoe = "SELECT Usuario, Password FROM pppoe WHERE `ID Cliente` = '%s'" % idcliente


                # Se imprime el telefono en el modal si hay servicio, si no, se imprime como "Sin servicio"
                print(modalontborrado %idm)
                print('</form></td>')
                if row[9] != 'None':

                    print(modalclient %(idm, row[4], row[5], row[9], row[8], row[7], row[6]))

                else:
                    notelf = "Sin servicio"
                    print(modalclient %(idm, row[4], row[5], notelf, row[8], row[7], row[6]))

                print('</tr>')
                idm += 1

            print(tablaontfin)




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
print(javadatatableont)
print(javadatatablebuttonstyle)
print(HTMLFIN)
