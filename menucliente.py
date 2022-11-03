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
            print("<script>$('#menucliente').css('background-color','#FEA126');</script>")

            print(modalcliente)
            cursor.execute("SELECT Nombre FROM planes GROUP BY Nombre")
            result_set = cursor.fetchall()
            for row in result_set:
                print ('<option value="%s">%s</option>' %(row[0], row[0]) )
            print(modalcliente2)
            print(modalcliente3)
            cursor.execute("SELECT Dominio FROM serversip ORDER BY Dominio")
            result_set = cursor.fetchall()
            for row in result_set:
                print ('<option value="%s">%s</option>' %(row[0], row[0]) )
            print(modalcliente4)
            #print('<div class="col-md-12">')
            #print('<div id="pageNavPosition"></div>')
            #print('</div>')
            print('<div class="col-md-4">')
            print('<h2 style="color:#1A5F82;margin-top:40px">Lista de clientes</h2>')
            print('</div>')

            #Boton alta de nuevo cliente
            print("""<div class='col-md-1' style='float:right;margin-top:40px'>
                        <div class= 'row tooltip-demo'>
						<a style='cursor:pointer' class='quick-btn alta-btn' data-target='#myModalcliente' data-toggle='modal'>
                             <i class='fa fa-2x fa-user-plus' data-toggle='tooltip' data-placement='bottom' title='' data-original-title='Alta Cliente'></i>
                        </a>
                        </div>
					</div>""")


            # Fin botón alta y menú de navegación

            sqlclientlist = "SELECT t1.Nombre, t1.Direccion, t1.ID, t3.Nombre, t2.Nombre, t1.DNI, t1.Telefono, t1.CGNAT, t3.ID FROM clientes AS t1, planes AS t2, olt AS t3 WHERE t1.Plan = t2.ID AND t1.OLT = t3.ID ORDER BY t1.Fecha DESC"
            cursor.execute(sqlclientlist)
            resultclient = cursor.fetchall()
            sqlontverify = "SELECT `ID Servicio` FROM ont"
            cursor.execute(sqlontverify)
            resultont = cursor.fetchall()

            print(tablacliente)

            idmc = 1


            for row in resultclient:
                sqlsipverify = "SELECT `ID SIP` FROM sip WHERE `ID SIP`= %s" %row[2]
                sqlpppoeverify = "SELECT t1.`ID Cliente`, t1.Usuario, t1.Password FROM pppoe AS t1, clientes AS t2 WHERE t1.`ID Cliente` = '%s' AND t1.`ID Cliente` = t2.`ID`" %row[2]
                if str(row[2]) in str(resultont):
                    ontdata = "SELECT t2.SN, t2.`ONT ID`, t2.Estado, t2.Modelo FROM ont AS t2, clientes AS t1 WHERE t1.ID = t2.`ID Servicio` AND t1.ID = %s" % row[2]
                    cursor.execute(ontdata)
                    resultontdata = cursor.fetchone()
                    if cursor.execute(sqlpppoeverify):
                        pppoedata = cursor.fetchone()
                        usuariopppoe = pppoedata[1]
                        contraseñapppoe = pppoedata[2]
                    else:
                        usuariopppoe = "No disponible"
                        contraseñapppoe = "No disponible"

                    modalontclient = """
                        <!-- Modal -->
                        <div id="myModalclient%s" class="modal fade" role="dialog">
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
                                <p style="font-size:16px"><b>Modelo:&nbsp&nbsp</b>%s</p>
                                <p style="font-size:16px"><b>OLT:&nbsp&nbsp</b>%s</p>
                                <p style="font-size:16px"><b>Estado:&nbsp&nbsp</b>%s</p>
								<p style="font-size:16px"><b>Usuario PPPOE:&nbsp&nbsp</b>%s</p>
								<p style="font-size:16px"><b>Contraseña PPPOE:&nbsp&nbsp</b>%s</p>
                              </div>
                            </div>

                          </div>
                        </div>
                        """ %(idmc, resultontdata[0], resultontdata[1],resultontdata[3], row[3], resultontdata[2], usuariopppoe, contraseñapppoe)

                    print('<tr id="%s" class="info">' %row[2])
                    print('<td align="center">',row[0],'</td>')
                    print('<td align="center">',row[1],'</td>')
                    print('<td align="center">',row[2],'</td>')
                    print('<td align="center">',row[4],'</td>')

                    print('<td align="center">',row[5],'</td>')
                    if row[6] != 'None':
                        print('<td align="center">',row[6],'</td>')
                    else:
                        print('<td align="center"><i style="color:#FEA126" class="glyphicon glyphicon glyphicon-remove-sign"></i></td>')

                    sqlpppoeverify = "SELECT `ID Cliente` FROM pppoe WHERE `ID Cliente`= %s" %row[2]
                    if cursor.execute(sqlpppoeverify):
                        print('<td align="center">PPPOE</td>')
                    else:
                        print('<td align="center">DHCP</td>')
                    if row[7] == "si":
                        print('<td align="center" style="color:#FEA126"><b>CG-NAT</b></td>')
                    else:
                        print('<td align="center" style="color:#4CAE4C"><b>NAT</b></td>')

                    print('<td align="center"><form action="/cgi-bin/manageclient.py" method="post">'+
                    '<input type="hidden" name="nombrecliente" value="%s"/>'%row[0]+
                    '<input type="hidden" name="dircliente" value="%s"/>'%row[1]+
                    '<input type="hidden" name="idcliente" value="%s"/>'%row[2]+
                    '<input type="hidden" name="plancliente" value="%s"/>'%row[4]+
                    '<input type="hidden" name="oltcliente" value="%s"/>'%row[8]+
                    '<input type="hidden" name="dnicliente" value="%s"/>'%row[5]+
                    '<input type="hidden" name="telfcliente" value="%s"/>'%row[6]+
					'<input type="hidden" name="cgnat" value="%s"/>'%row[7])
                    print('<button title="Modificar" type="submit" class="btn btn-primary btn-xs" name="modificarcliente" value="botonedit" style="margin-left:10px"><i class="glyphicon glyphicon-wrench"></i></button>')
                    print('<button title="Baja no disponible" type="submit" class="btn btn-danger btn-xs" name="bajacliente" style="margin-left:10px" disabled><i class="glyphicon glyphicon-trash" style="margin-right:0.8px"></i></button>')

                    if resultontdata[2] == 'Activada':
                        print('<button title="ONT asociada" type="button" class="btn btn-success btn-xs" data-target="#myModalclient%s" data-toggle="modal" style="margin-left:10px"><span class="glyphicon glyphicon-hdd"></span></button>' %idmc)
                    else:
                        print('<button title="ONT asociada" type="button" class="btn btn-warning btn-xs" data-target="#myModalclient%s" data-toggle="modal" style="margin-left:10px"><span class="glyphicon glyphicon-hdd"></span></button>' %idmc)

                    if cursor.execute(sqlsipverify):
                        print('<i style="margin-left:10px;color:#449D44;float: right;padding: 10px;" title="SIP Activado" class="glyphicon glyphicon-earphone"></i></form></td>')
                    else:
                        print('<i style="margin-left:10px;color:#D9534F;float: right;padding: 10px;" title="Sin servicio SIP" class="glyphicon glyphicon-earphone"></i></form></td>')
                    print(modalontclient)
                    print('</tr>')
                    idmc += 1


                else:
                    print('<tr id="%s" class="danger">'%row[2])
                    print('<td align="center">',row[0],'</td>')
                    print('<td align="center">',row[1],'</td>')
                    print('<td align="center">',row[2],'</td>')
                    print('<td align="center">',row[4],'</td>')

                    print('<td align="center">',row[5],'</td>')
                    if row[6] != 'None':
                        print('<td align="center">',row[6],'</td>')
                    else:
                        print('<td align="center"><i style="color:#FEA126" class="glyphicon glyphicon glyphicon-remove-sign"></i></td>')

                    sqlpppoeverify = "SELECT `ID Cliente` FROM pppoe WHERE `ID Cliente`= %s" %row[2]
                    if cursor.execute(sqlpppoeverify):
                        print('<td align="center">PPPOE</td>')
                    else:
                        print('<td align="center">DHCP</td>')

                    if row[7] == "si":
                        print('<td align="center" style="color:#FEA126"><b>CG-NAT</b></td>')
                    else:
                        print('<td align="center" style="color:#4CAE4C"><b>NAT</b></td>')

                    print('<td align="center"><form action="/cgi-bin/manageclient.py" method="post">'+
                    '<input type="hidden" name="nombrecliente" value="%s"/>'%row[0]+
                    '<input type="hidden" name="dircliente" value="%s"/>'%row[1]+
                    '<input type="hidden" name="idcliente" value="%s"/>'%row[2]+
                    '<input type="hidden" name="plancliente" value="%s"/>'%row[4]+
                    '<input type="hidden" name="oltcliente" value="%s"/>'%row[8]+
                    '<input type="hidden" name="dnicliente" value="%s"/>'%row[5]+
                    '<input type="hidden" name="telfcliente" value="%s"/>'%row[6]+
					'<input type="hidden" name="cgnat" value="%s"/>'%row[7])
                    print('<button title="Modificar" type="submit" class="btn btn-primary btn-xs" name="modificarcliente" value="botonedit" style="margin-left:10px"><i class="glyphicon glyphicon-wrench"></i></button>')
                    print('<button title="Baja cliente" type="button" href="#modal-borrarcliente%s" data-toggle="modal" class="btn btn-danger btn-xs" style="margin-left:10px"><i class="glyphicon glyphicon-trash" style="margin-right:0.8px"></i></button>' %idmc)

                    print('<button title="ONT no asociada" type="button" class="btn btn-danger btn-xs" style="margin-left:10px" disabled> <span class="glyphicon glyphicon-hdd"></span></button>')
                    if cursor.execute(sqlsipverify):
                        print('<i style="margin-left:10px;color:#31B0D5;float: right;padding: 10px;" title="SIP Activado" class="glyphicon glyphicon-earphone"></i></form></td>')
                    else:
                        print('<i style="margin-left:10px;color:#D9534F;float: right;padding: 10px;" title="Sin servicio SIP" class="glyphicon glyphicon-earphone"></i></form></td>')
                    print('</tr>')
                    print(modalclienteborrado %(idmc,row[0],row[2])) # Modal de borrado de cliente (Ejecuta funcion "bajacliente" de archivo script.js)
                    idmc += 1

            print(tablaclientefin)


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
print(javadatatablecliente)
print(javadatatablebuttonstyle)
print(HTMLFIN)
