#! /usr/bin/python3.5

import cgi
import sys
import MySQLdb
from htmlvar import *
import os
import http.cookies
from pysnmp.entity.rfc3413.oneliner import cmdgen

cmdGen = cmdgen.CommandGenerator()

con = MySQLdb.connect(host='localhost', user='honeypon', passwd='pon', db='honeypon')
cursor = con.cursor()


if 'HTTP_COOKIE' in os.environ:
    cookie_string=os.environ.get('HTTP_COOKIE')
    honeycookie = "honeypon=honeyponlogin"
    #if c['honeypon'].value == 'honeyponlogin':
    if honeycookie in cookie_string:
        print("content-type: text/html\n\n")
        print(HTMLHEADER)
        #c=http.cookies.SimpleCookie()
        #c.load(cookie_string)
        #c['honeypon']['expires']=1*1*7*60*60
        #print(c)
        print(HTML)
        sqlontlist = "SELECT t1.SN, t1.`ONT ID`, t1.`ID Servicio`, t1.Estado, t2.Nombre, t2.Direccion, t2.olt, t3.Nombre, t2.DNI, t2.Telefono, t1.Modelo FROM ont AS t1, clientes AS t2, planes AS t3 WHERE t1.`ID Servicio` = t2.ID AND t2.Plan = t3.ID ORDER BY t1.`ONT ID`"
        cursor.execute(sqlontlist)
        resultont = cursor.fetchall()

        # Comienzo botón alta y menú de navegación
        print('<div class="col-md-12">')
        print('<h2 style="color:#1A5F82;margin-top:40px">Lista de ONT</h2>')
        print('<button type="button" class="btn btn-primary" data-target="#myModal" data-toggle="modal" style="width:200px; margin-top:30px"><span>Nueva alta</span></button>')
        print('</div>')
        print(modalont)
        print('<div class="col-md-12" style="margin-top:50px">')
        print('<div id="pageNavPosition"></div>')
        print('</div>')
        # Fin botón alta y menú de navegación


        print(tablaont)

        idm = 1
        for row in resultont:
            modal3 = """
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
            #cursor.execute(sqlsipdata)
            #sipdata = cursor.fetchone()

            # Se saca el Slot, Puerto-PON e ID de ONT para captura de informacion de potencias(rx)
            idprintont = row[1]
            idslot = int(idprintont[2])
            idport = int(idprintont[4])
            idont = int(idprintont[6])


            if idslot == 0:
                port = -1
                for portsnmp in slot0:
                    port = port + 1
                    if port == idport:

                        errorIndication, errorStatus, errorIndex, snmppotencia = cmdGen.getCmd(cmdgen.CommunityData('honeypon1107'), cmdgen.UdpTransportTarget((oltip[0], 161)), '1.3.6.1.4.1.2011.6.158.1.1.1.2.1.22.%s.%s' % (portsnmp,idont))
                        strpotenciasnmp = str(snmppotencia)
                        strpotencia = strpotenciasnmp[-12:][:-5]
                        rx = strpotencia[:3] + '.' + strpotencia[3:]
                        break


            elif idslot == 1:
                port = -1
                for portsnmp in slot1:
                    port = port + 1
                    if port == idport:

                        errorIndication, errorStatus, errorIndex, snmppotencia = cmdGen.getCmd(cmdgen.CommunityData('honeypon1107'), cmdgen.UdpTransportTarget((oltip[0], 161)), '1.3.6.1.4.1.2011.6.158.1.1.1.2.1.22.%s.%s' % (portsnmp,idont))
                        strpotenciasnmp = str(snmppotencia)
                        strpotencia = strpotenciasnmp[-12:][:-5]
                        rx = strpotencia[:3] + '.' + strpotencia[3:]
                        break

            elif idslot == 2:
                port = -1
                for portsnmp in slot2:
                    port = port + 1
                    if port == idport:

                        errorIndication, errorStatus, errorIndex, snmppotencia = cmdGen.getCmd(cmdgen.CommunityData('honeypon1107'), cmdgen.UdpTransportTarget((oltip[0], 161)), '1.3.6.1.4.1.2011.6.158.1.1.1.2.1.22.%s.%s' % (portsnmp,idont))
                        strpotenciasnmp = str(snmppotencia)
                        strpotencia = strpotenciasnmp[-12:][:-5]
                        rx = strpotencia[:3] + '.' + strpotencia[3:]
                        break


            elif idslot == 3:
                port = -1
                for portsnmp in slot3:
                    port = port + 1
                    if port == idport:

                        errorIndication, errorStatus, errorIndex, snmppotencia = cmdGen.getCmd(cmdgen.CommunityData('honeypon1107'), cmdgen.UdpTransportTarget((oltip[0], 161)), '1.3.6.1.4.1.2011.6.158.1.1.1.2.1.22.%s.%s' % (portsnmp,idont))
                        strpotenciasnmp = str(snmppotencia)
                        strpotencia = strpotenciasnmp[-12:][:-5]
                        rx = strpotencia[:3] + '.' + strpotencia[3:]
                        break

            elif idslot == 4:
                port = -1
                for portsnmp in slot4:
                    port = port + 1
                    if port == idport:

                        errorIndication, errorStatus, errorIndex, snmppotencia = cmdGen.getCmd(cmdgen.CommunityData('honeypon1107'), cmdgen.UdpTransportTarget((oltip[0], 161)), '1.3.6.1.4.1.2011.6.158.1.1.1.2.1.22.%s.%s' % (portsnmp,idont))
                        strpotenciasnmp = str(snmppotencia)
                        strpotencia = strpotenciasnmp[-12:][:-5]
                        rx = strpotencia[:3] + '.' + strpotencia[3:]
                        break

            elif idslot == 5:
                port = -1
                for portsnmp in slot4:
                    port = port + 1
                    if port == idport:

                        errorIndication, errorStatus, errorIndex, snmppotencia = cmdGen.getCmd(cmdgen.CommunityData('honeypon1107'), cmdgen.UdpTransportTarget((oltip[0], 161)), '1.3.6.1.4.1.2011.6.158.1.1.1.2.1.22.%s.%s' % (portsnmp,idont))
                        strpotenciasnmp = str(snmppotencia)
                        strpotencia = strpotenciasnmp[-12:][:-5]
                        rx = strpotencia[:3] + '.' + strpotencia[3:]
                        break


            if row[3] == 'Desactivada':
                print('<tr class="danger" id="danger">')
            else:
                print('<tr class="info" id="success">')
            print('<td align="center">',row[0],'</td>')
            print('<td align="center">',row[1],'</td>')
            print('<td align="center">',row[10],'</td>')
            print('<td align="center">',row[2],'</td>')
            print('<td align="center">',row[3],'</td>')

            if rx[:1] == "-":
                if -27 <= float(rx):
                    print('<td align="center" style="color:green">',rx,'dBm</td>')
                elif -29 <= float(rx) <= -27:
                    print('<td align="center" style="color:#F99D0D">',rx,'dBm</td>')
                else:
                    print('<td align="center" style="color:#C9302C">',rx,'dBm</td>')
            else:
                print('<td align="center" style="color:#C9302C">Error de lectura</td>')

            if cursor.execute(sqlsipdata):
                sipdata = cursor.fetchone()
                print('<td align="center"><form action="/cgi-bin/ont.py" method="post" target="_blank" ><input type="hidden" name="sn" value=',row[0],'/><input type="hidden" name="service" value=',row[2],'/><input type="hidden" name="oltip" value=',oltip[0],'/><input type="hidden" name="extensionsip" value=',sipdata[0],'/><input type="hidden" name="secretsip" value=',sipdata[1],'/><input type="hidden" name="ontid" value="%s" /><input type="hidden" name="clientname" value="%s" />' % (idprintont,row[4]))
            else:
                print('<td align="center"><form action="/cgi-bin/ont.py" method="post" target="_blank" ><input type="hidden" name="sn" value=',row[0],'/><input type="hidden" name="service" value=',row[2],'/><input type="hidden" name="oltip" value=',oltip[0],'/><input type="hidden" name="ontid" value="%s" /><input type="hidden" name="clientname" value="%s" />' % (idprintont,row[4]))
            if row[3] == 'Desactivada':
                print('<button title="Reactivar" type="submit" value="Reactivar" class="btn btn-primary btn-xs" name="altaserv", text-align=center" style="margin-left:10px"><i class="glyphicon glyphicon-ok" ></i></button>')
            else:
                print('<button title="Desactivar" type="submit" value="Desactivar"  class="btn btn-warning btn-xs" name="bajaserv",text-align=center" style="margin-left:10px"><i class="glyphicon glyphicon-remove"></i></button>')
            print('<button title="Baja ONT" type="submit" value="Baja ONT" class="btn btn-danger btn-xs" name="bajaont",text-align=center" style="margin-left:10px"><i class="glyphicon glyphicon-trash"></i></button>')
            if cursor.execute(sqlsipdata):
                print('<button formtarget="_blank" title="Aprovisionar SIP" type="submit" class="btn btn-primary btn-xs" name="syncsip" value="botonsip" style="margin-left:10px"><i class="glyphicon glyphicon-earphone"></i></button>')
            else:
                print('<button title="SIP no asociado" type="submit" class="btn btn-primary btn-xs" name="syncsip" value="botonsip" style="margin-left:10px" disabled><i class="glyphicon glyphicon-earphone"></i></button>')
            print('<button title="Cliente asociado" type="button" class="btn btn-info btn-xs" data-target="#myModal%s" data-toggle="modal" style="margin-left:10px"><i class="glyphicon glyphicon-user"></i></button>' %idm)
            #print('<button title="Monitor" type="button" class="btn btn-success btn-xs" style="float:right;margin-left:10px"><i class="glyphicon glyphicon-stats"></i></button>')
            print('<a href="http://192.168.88.120/cacti/graph_view.php?style=selective&action=preview&thumbnails=false&predefined_timespan=2&filter=%s" target="_blank" title="Monitor" class="btn btn-default btn-xs" style="float:right"><i class="glyphicon glyphicon-signal"></i></a>' %row[1])
            if row[10] == "HG8245H":
                print('<a href="http://192.168.88.140:3000/devices/00259E-HG8245H-%s" target="_blank" title="Gestionar ONT" class="btn btn-default btn-xs" style="float:right"><i class="glyphicon glyphicon-cog"></i></a>' %row[0].upper())
            else:
                print('<a href="http://192.168.88.140:3000/devices" target="_blank" title="Gestionar ONT" class="btn btn-default btn-xs" style="float:right"><i class="glyphicon glyphicon-cog"></a>')
            print('<button formtarget="_blank" title="Programar tarea" type="submit" class="btn btn-default btn-xs" name="program" value="botonprogram" style="float:right;margin-left:10px"><i class="glyphicon glyphicon-time"></i></button></form></td>')

            # Se imprime el telefono en el modal si hay servicio, si no, se imprime como "Sin servicio"
            if row[9] != 'None':
                print(modal3 %(idm, row[4], row[5], row[9], row[8], row[7], row[6]))
            else:
                notelf = "Sin servicio"
                print(modal3 %(idm, row[4], row[5], notelf, row[8], row[7], row[6]))
            print('</tr>')
            idm += 1

        print(tablaontfin)


        print(HTML1)

        # Comienzo botón alta y menú de navegación
        print('<div class="col-md-12">')
        print('<h2 style="color:#1A5F82;margin-top:40px">Lista de clientes</h2>')
        print('<button type="button" class="btn btn-primary" data-target="#myModalcliente" data-toggle="modal" style="width:200px; margin-top:30px"><span>Nuevo cliente</span></button>')
        print('<a href="http://192.168.88.130" target="_blank"><button type="button" class="btn btn-info" style="width:200px; margin-top:30px; margin-left:10px"><span>Nuevo cliente SIP</span></button></a>')
        print('</div>')
        print(modalcliente)
        cursor.execute("SELECT Nombre FROM planes")
        result_set = cursor.fetchall()
        for row in result_set:
            print ('<option value="%s">%s</option>' %(row[0], row[0]) )
        print(modalcliente2)
        cursor.execute("SELECT Nombre FROM olt")
        result_set = cursor.fetchall()
        for row in result_set:
            print ('<option value="%s">%s</option>' %(row[0], row[0]) )
        print(modalcliente3)
        print('<div class="col-md-12" style="margin-top:50px">')
        print('<div id="pageNavPositionclient"></div>')
        print('</div>')
        # Fin botón alta y menú de navegación

        sqlclientlist = "SELECT t1.Nombre, t1.Direccion, t1.ID, t1.OLT, t2.Nombre, t1.DNI, t1.Telefono FROM clientes AS t1, planes AS t2 WHERE t1.Plan = t2.ID ORDER BY t1.ID"
        cursor.execute(sqlclientlist)
        resultclient = cursor.fetchall()

        sqlontverify = "SELECT `ID Servicio` FROM ont"
        cursor.execute(sqlontverify)
        resultont = cursor.fetchall()

        print(tablacliente2)
        idmc = 1


        for row in resultclient:
            sqlsipverify = "SELECT `ID SIP` FROM sip WHERE `ID SIP`= %s" %row[2]
            if str(row[2]) in str(resultont):
                ontdata = "SELECT t2.SN, t2.`ONT ID`, t2.Estado, t2.Modelo FROM ont AS t2, clientes AS t1 WHERE t1.ID = t2.`ID Servicio` AND t1.ID = %s" % row[2]
                cursor.execute(ontdata)
                resultontdata = cursor.fetchone()
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
                          </div>
                        </div>

                      </div>
                    </div>
                    """ %(idmc, resultontdata[0], resultontdata[1],resultontdata[3], row[3], resultontdata[2])

                print('<tr class="info" id="success">')
                print('<td align="center">',row[0],'</td>')
                print('<td align="center">',row[1],'</td>')
                print('<td align="center">',row[2],'</td>')

                if row[6] != 'None':
                    print('<td align="center">',row[4],'+','Voz','</td>')
                else:
                    print('<td align="center">',row[4],'</td>')

                print('<td align="center">',row[5],'</td>')
                if row[6] != 'None':
                    print('<td align="center">',row[6],'</td>')
                else:
                    print('<td align="center">Sin servicio</td>')
                print('<td align="center"><form action="/cgi-bin/manageclient.py" method="post" target="_blank">'+
                '<input type="hidden" name="nombrecliente" value="%s"/>'%row[0]+
                '<input type="hidden" name="dircliente" value="%s"/>'%row[1]+
                '<input type="hidden" name="idcliente" value="%s"/>'%row[2]+
                '<input type="hidden" name="plancliente" value="%s"/>'%row[4]+
                '<input type="hidden" name="oltcliente" value="%s"/>'%row[3]+
                '<input type="hidden" name="dnicliente" value="%s"/>'%row[5]+
                '<input type="hidden" name="telfcliente" value="%s"/>'%row[6])
                print('<button title="Modificar" type="submit" class="btn btn-primary btn-xs" name="modificarcliente" value="botonedit" style="margin-left:10px"><i class="glyphicon glyphicon-wrench"></i></button>')
                print('<button title="Baja no disponible" type="submit" class="btn btn-danger btn-xs" name="bajacliente" style="margin-left:10px" disabled><i class="glyphicon glyphicon-trash"></i></button>')
                if cursor.execute(sqlsipverify):
                    print('<button title="SIP Sincronizado" type="submit" class="btn btn-success btn-xs" name="syncsip" value="botonsip" style="margin-left:10px" disabled><i class="glyphicon glyphicon-earphone"></i></button>')
                else:
                    if row[6] != 'None':
                        print('<button formtarget="_blank" title="Sincronizar SIP" type="submit" class="btn btn-info btn-xs" name="syncsip" value="botonsip" style="margin-left:10px"><i class="glyphicon glyphicon-earphone"></i></button>')

                    else:
                        print('<button title="Sin servicio de voz" type="submit" class="btn btn-warning btn-xs" name="syncsip" value="botonsip" style="margin-left:10px" disabled><i class="glyphicon glyphicon-earphone"></i></button>')

                if resultontdata[2] == 'Activada':
                    print('<button title="ONT asociada" type="button" class="btn btn-success btn-xs" data-target="#myModalclient%s" data-toggle="modal" style="margin-left:10px"><span class="glyphicon glyphicon-hdd"></span></button></form></td>' %idmc)
                else:
                    print('<button title="ONT asociada" type="button" class="btn btn-warning btn-xs" data-target="#myModalclient%s" data-toggle="modal" style="margin-left:10px"><span class="glyphicon glyphicon-hdd"></span></button></form></td>' %idmc)

                print(modalontclient)
                print('</tr>')
                idmc += 1


            else:
                print('<tr class="danger" id="danger">')
                print('<td align="center">',row[0],'</td>')
                print('<td align="center">',row[1],'</td>')
                print('<td align="center">',row[2],'</td>')

                if row[6] != 'None':
                    print('<td align="center">',row[4],'+','Voz','</td>')
                else:
                    print('<td align="center">',row[4],'</td>')

                print('<td align="center">',row[5],'</td>')
                if row[6] != 'None':
                    print('<td align="center">',row[6],'</td>')
                else:
                    print('<td align="center">Sin servicio</td>')
                print('<td align="center"><form action="/cgi-bin/manageclient.py" method="post" target="_blank">'+
                '<input type="hidden" name="nombrecliente" value="%s"/>'%row[0]+
                '<input type="hidden" name="dircliente" value="%s"/>'%row[1]+
                '<input type="hidden" name="idcliente" value="%s"/>'%row[2]+
                '<input type="hidden" name="plancliente" value="%s"/>'%row[4]+
                '<input type="hidden" name="oltcliente" value="%s"/>'%row[3]+
                '<input type="hidden" name="dnicliente" value="%s"/>'%row[5]+
                '<input type="hidden" name="telfcliente" value="%s"/>'%row[6])
                print('<button title="Modificar" type="submit" class="btn btn-primary btn-xs" name="modificarcliente" value="botonedit" style="margin-left:10px"><i class="glyphicon glyphicon-wrench"></i></button>')
                print('<button title="Baja cliente" type="submit" class="btn btn-danger btn-xs" name="bajacliente" value="botonbaja" style="margin-left:10px"><i class="glyphicon glyphicon-trash"></i></button>')
                if cursor.execute(sqlsipverify):
                    print('<button title="SIP Sincronizado" type="submit" class="btn btn-success btn-xs" name="syncsip" value="botonsip" style="margin-left:10px" disabled><i class="glyphicon glyphicon-earphone"></i></button>')
                else:
                    if row[6] != 'None':
                        print('<button formtarget="_blank" title="Sincronizar SIP" type="submit" class="btn btn-info btn-xs" name="syncsip" value="botonsip" style="margin-left:10px"><i class="glyphicon glyphicon-earphone"></i></button>')

                    else:
                        print('<button title="Sin servicio de voz" type="submit" class="btn btn-warning btn-xs" name="syncsip" value="botonsip" style="margin-left:10px" disabled><i class="glyphicon glyphicon-earphone"></i></button>')

                print('<button title="ONT no asociada" type="button" class="btn btn-danger btn-xs" style="margin-left:10px" disabled> <span class="glyphicon glyphicon-hdd"></span></button></form></td>')
                print('</tr>')

        print(tablaclientefin)


        print(HTML2)

        sqloltlist = "SELECT Nombre, IP, `ID Cacti` FROM olt"
        cursor.execute(sqloltlist)
        resultolt = cursor.fetchall()

        # Comienzo botón alta y menú de navegación
        print('<div class="col-md-12">')
        print('<h2 style="color:#1A5F82;margin-top:40px">Lista de OLT</h2>')
        print('<button type="button" class="btn btn-primary" data-target="#myModalolt" data-toggle="modal" style="width:200px; margin-top:30px"><span>Nueva OLT</span></button>')
        print('</div>')
        print(modalolt)
        print('<div class="col-md-12" style="margin-top:50px">')
        print('<div id="pageNavPositionolt"></div>')
        print('</div>')
        # Fin botón alta y menú de navegación
        print(tablaolt)

        for row in resultolt:
            print('<tr class="info" id="success">')
            print('<td align="center">',row[0],'</td>')
            print('<td align="center">',row[1],'</td>')
            if row[2] is not None:
                print('<td align="center">',row[2],'</td>')
            else:
                print('<td align="center" style="color:red">Sin registrar</td>')

            print('<td align="center"><form action="/cgi-bin/olt.py" method="post" target="_blank"><input type="hidden" name="altaoltname" value=',row[0],'/><input type="hidden" name="inputip" value=',row[1],'/><input type="hidden" name="oltidcacti" value=',row[2],'/>')
            print('<button title="Modificar" type="submit" class="btn btn-primary btn-xs" name="modificarolt" value="botoneditolt" text-align=center" style="margin-left:10px"><i class="glyphicon glyphicon-wrench"></i></button>')
            print('<button title="Baja OLT" type="submit" value="Baja OLT" class="btn btn-danger btn-xs" name="bajaolt" text-align=center" style="margin-left:10px"><i class="glyphicon glyphicon-trash"></i></button>')
            print('<button title="Registrar en servidor NMS" type="submit" value="Alta Cacti" class="btn btn-success btn-xs" name="altacacti" text-align=center" style="margin-left:10px"><i class="glyphicon glyphicon-import"></i></button></form></td>')

        print('</tr>')
        print(tablaoltfin)

        print(HTML3)


    else:
        print("content-type: text/html\n\n")
        print(HTMLHEADER)
        print("""<script language="javascript">
        window.location.href = "/index.py"
        </script>""")

else:
    print("content-type: text/html\n\n")
    print(HTMLHEADER)
    print("""<script language="javascript">
    window.location.href = "/index.py"
    </script>""")

print(javacode)
print(HTMLFIN)
