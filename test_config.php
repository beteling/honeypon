#! /usr/bin/python3.5


 # Copyright 2016-2017  Beteling Consultoría e Ingeniería
 #
 # Este fichero es parte de honeypon
 #
 # Honeypon es un software propietario propiedad de "Beteling Consultoría e Ingeniería",
 # que abarca el programa informático su código fuente y la estructura de su base de datos.
 # No se podrá efectuar cualquier modificiación o manipulación de sus estructuras
 # sin la autorización expresa del propietario.
 #
 # El software es objeto de licencia para su uso en un único servidor físico o virtual
 # dedicado para ello, por lo que queda expresamente prohibido por parte del LICENCIANDO
 # la reproducción, transmisión a otro equipo informático, modificación, adaptación,
 # mantenimiento, corrección de errores, cesión, venta, ariendo, préstamo,
 # cesión de uso ni parcial ni total, transmisión del derecho de uso, divulgación,
 # publicación, etc., del programa, con la lógica exepción del uso por parte de
 # los empleados directos del LICENCIADO

# <--Script para gestion de altas y bajas de ont-->

import cgi
import sys
import json
import requests
import os
import time
import telnetlib
import MySQLdb
import subprocess
from cgivar import *
from snmpvar import *
from pymongo import MongoClient

# Conexión con la base de datos de honeypon
con = MySQLdb.connect(host='localhost', user='honeypon', passwd='pon', db='honeyponv2')
cursor = con.cursor()


form = cgi.FieldStorage()
ontservice = form.getvalue('idservicio_para_alta')
ontsn = form.getvalue('sn_ont')
sys.stdout.write("Content-Type: application/json")

sys.stdout.write("\n")
sys.stdout.write("\n")

# Recoge la IP del servidor
sqlserverip = "SELECT IP FROM servidor"
if cursor.execute(sqlserverip):
    fetchserverip = cursor.fetchone()
    serverip = fetchserverip[0];

# Recoge la IP de la OLT para bajas, desactivaciones y reactivaciones
#olt = form.getvalue('oltip')
sql_olt_ip = "SELECT t1.IP FROM olt AS t1, clientes AS t2 WHERE t1.ID = t2.olt AND t2.ID = %s" % ontservice
if cursor.execute(sql_olt_ip):
    fetcholtip = cursor.fetchone()
    olt = fetcholtip[0];


def telnetconnect(olt):
    tn = telnetlib.Telnet(olt,1313, timeout=2)
    tn.read_until(b'name:')
    tn.write('honeypon'.encode('ascii') + b'\n')
    tn.read_until(b':')
    tn.write('honeypon1107'.encode('ascii') + b'\n')
    tn.read_until(b'>')
    tn.write('enable'.encode('ascii') + b'\n')
    tn.read_until(b'#')
    tn.write('config'.encode('ascii') + b'\n')
    tn.read_until(b'#')
    return (tn)

def altaservicio(tn):
    global msg
    tn.write('display ont autofind all'.encode('ascii') + b'\n' + b'\n')
    time.sleep(2)
    tn2 = tn.read_very_eager()
    while not tn2.find(ontsn.encode('ascii')) >= 0:
        if tn2.find(b'(config)#') >= 0:
            msg="""

                <div class="alert alert-warning alert-dismissable">
                <p>El numero de serie no ha sido reconocido por la OLT. Revise los campos y asegurese de que haya comunicacion entre la ONT y la cabecera</p>
                </div>

            """
            tn.close()
            break
        else:
            tn.write('n'.encode('ascii'))
            time.sleep(2)
            tn2 = tn.read_very_eager()


    if tn2.find(ontsn.encode('ascii')) >= 0:
        tel = tn2.split(ontsn.encode('ascii'))
        telid = tel[0].split()
        idencode = telid[-4]
        telmodel = tel[1].split()
        if not 'Ont EquipmentID'.encode('ascii') in tel[1]:
            tn.write('n'.encode('ascii'))
            time.sleep(2)
            tn3 = tn.read_very_eager()
            modelencode=tn3.split('Ont EquipmentID'.encode('ascii'))[1].split()[1]
        else:
            modelencode=tel[1].split('Ont EquipmentID'.encode('ascii'))[1].split()[1]

        #modelencode = telmodel[22]
        #if modelencode == 'Press'.encode('ascii'):
            #modelencode = telmodel[32]


        # Decodifica el modelo de ONT, ID y saca el Frame, Slot y Puerto
        modelhw = modelencode.decode('ascii')
        modelo = modelhw
        idprint = idencode.decode('ascii')
        idframe = idprint[0]
        idslot = idprint[2]
        idport = idprint[4:]
        idframeslot = idprint[0] + idprint[1] + idprint[2]
        if tn2.find(b'The number of GPON autofind ONT is') == -1:
            tn.write('q'.encode('ascii'))
            time.sleep(1)
            tn.read_until(b'#')
        time.sleep(1)
        tn.write(b'\n')
        tn.read_until(b'#')
        # Extrae informacion de la base de datos
        sqlplan = "SELECT t1.Nombre, t3.Nombre AS 'RX', t4.Nombre AS 'TX' FROM planes AS t1, clientes AS t2, tablatrafico AS t3, tablatrafico AS t4 WHERE t1.ID = t2.Plan AND t2.ID= %s AND t3.ID = t1.RX AND t4.ID = t1.TX" % ontservice

        cursor.execute(sqlplan)
        fetchplan = cursor.fetchone()
        fetchup = fetchplan[1]
        fetchdown = fetchplan[2]

        sqlclienttable = "SELECT Nombre, Direccion, ID, DNI, CGNAT FROM clientes WHERE ID = %s" % ontservice
        cursor.execute(sqlclienttable)
        feclient = cursor.fetchone()
        bridgemode = "false"

        # Comprueba si el servicio tiene configurado el modo bridge
        sqlbridgeverify = "SELECT `ID Cliente` FROM bridge WHERE `ID Cliente`= %s" % ontservice
        if cursor.execute(sqlbridgeverify):
            bridgemode = "true"

        # Se registra la ont
        desc = ontsn
        iface = "interface gpon %s" % idframeslot
        ontadd = 'ont confirm %s sn-auth %s omci ont-lineprofile-name "FTTH" ont-srvprofile-name Adaptive desc "%s"' % (idport,ontsn,desc)
        tn.write(iface.encode('ascii') + b'\n')
        tn.read_until(b'#')
        tn.write(ontadd.encode('ascii') + b'\n')
        time.sleep(3)


        # Extrae el ID asignado a la ont y se crea ID para honeypon "idprintont"

        idtn = tn.read_very_eager()
        time.sleep(1)
        try:
            idontread = idtn.decode('ascii').split('ONTID :')[1]
        except:
            tn.write(b'\n')
            tn.write('quit'.encode('ascii') + b'\n')
            tn.read_until(b'#')
            ontinfo = "display ont info by-sn %s" % ontsn
            tn.write(ontinfo.encode('ascii') + b'\n')
            time.sleep(2)
            tnreadinfo = tn.read_very_eager()
            time.sleep(1)
            idonterror = tnreadinfo.decode('ascii').split('ONT-ID')[1].split()[1]
            tn.write('q'.encode('ascii'))
            tn.write(iface.encode('ascii') + b'\n')
            time.sleep(1)
            tn.read_until(b'#')
            ontdel = 'ont delete %s %s' % (idport,idonterror)
            tn.write(ontdel.encode('ascii') + b'\n')
            msg="""

                <div class="alert alert-warning alert-dismissable">
                <p>Error en el registro. Por favor vuelva a intentarlo</p>
                </div>

            """
            sys.exit("Error de registro")

        idontstr = idontread.split()
        idont = int(idontstr[0])
        idprintont = idprint + ' ' + str(idont)

        # Se actualiza la descripcion de la ONT para Cacti
        ontdesc = 'ont modify %s %s desc "%s"' %(idport,idont,idprintont)
        tn.write(ontdesc.encode('ascii') + b'\n')
        tn.read_until(b'#')

####################################################################################
################## CONFIGURACION SIP, TR069 y PUERTOS DE SERVICIO ##################
####################################################################################

        # Se declaran los service ports
        serviceport = "service-port vlan 101 gpon %s ont %s gemport 1 multi-service user-vlan 100 inbound traffic-table name %s outbound traffic-table name %s" % (idprint, idont, fetchdown, fetchup)

        serviceportpublicip = "service-port vlan 100 gpon %s ont %s gemport 1 multi-service user-vlan 100 inbound traffic-table name %s outbound traffic-table name %s" % (idprint, idont, fetchdown, fetchup)
        serviceportvoip = "service-port vlan 70 gpon %s ont %s gemport 3 multi-service user-vlan 70 inbound traffic-table name 1M outbound traffic-table name 1M" % (idprint, idont)


        # Se configura la interfaz WAN para Voz y TR069
        ipconfig = "ont ipconfig %s %s ip-index 1 dhcp vlan 70 priority 6" % (idport, idont)
        tn.write(ipconfig.encode('ascii') + b'\n')
        tn.read_until(b'#')
        #print(tn.read_very_eager().decode('ascii'),file=open("debug.txt", "a",encoding='utf8'))
        # Se configura el bridge si procede
        if bridgemode == "true":
            nativevlan = "ont port native-vlan %s %s eth 1 vlan 100" %(idport,idont)
            tn.write(nativevlan.encode('ascii') + b'\n')
            tn.read_until(b':')
            tn.write(b'\n')
            tn.read_until(b'#')

        # Se configura el perfil "honeyacs" para TR069 a la ont
        tr069 = "ont tr069-server-config %s %s profile-name honeyacs" % (idport, idont)
        tn.write(tr069.encode('ascii') + b'\n')
        tn.read_until(b'#')

        # Se configura el perfil "SIP" a la ont si existe un sip asociado
        sqlsip = "SELECT t1.`ID SIP`, t1.Extension, t1.Secret, t3.Dominio FROM sip AS t1, clientes AS t2, serversip AS t3 WHERE t1.`ID SIP` = t2.ID AND t3.ID = t1.servidor AND t2.ID= %s" % ontservice
        if (cursor.execute(sqlsip)):
            sip=cursor.fetchone()

            ifsip = "if-sip add %s %s 1 ip-index 1 sipagent-profile profile-name %s" % (idport, idont, sip[3])
            tn.write(ifsip.encode('ascii') + b'\n')
            tn.read_until(b':')
            tn.write(b'\n')
            tn.read_until(b'#')
            #sippstn = "sippstnuser add %s %s 1 mgid 1" % (idport,idont)
            #tn.write(sippstn.encode('ascii') + b'\n')
            #tn.read_until(b':')
            #tn.write(b'\n')
            #tn.read_until(b'#')
            sippstnuser = "sippstnuser add %s %s 1 mgid 1 username %s password %s telno %s" % (idport,idont,sip[1],sip[2],sip[1])
            tn.write(sippstnuser.encode('ascii') + b'\n')
            tn.write(b'\n')
            tn.read_until(b'#')

            time.sleep(1)

        tn.write('quit'.encode('ascii') + b'\n')





        if feclient[4] == "si": # Si usa CG-NAT
            tn.write(serviceport.encode('ascii') + b'\n')

            tn.write(serviceportvoip.encode('ascii') + b'\n')

        else: # Si usa NAT
            tn.write(serviceportpublicip.encode('ascii') + b'\n')
            tn.write(serviceportvoip.encode('ascii') + b'\n')

            time.sleep(3)
            #print(tn.read_very_eager().decode('ascii'),file=open("debug.txt", "a",encoding='utf8'))


####################################################################################
################## CONFIGURACION SIP, TR069 y PUERTOS DE SERVICIO ##################
####################################################################################

        sqlinsert = "INSERT INTO `ont`(`SN`, `ONT ID`, frame, slot, port, ont_id, `Modelo`,`ID Servicio`, `Estado`) VALUES ('%s','%s', '%s', %s, '%s','%s', '%s', %s, 'Activada')" % (ontsn, idprintont, idframe, idslot, idport, str(idont), modelo, ontservice)
        cursor.execute(sqlinsert)
        con.commit()
        msg="""

            <div class="alert alert-success alert-dismissable">
            <p>ONT registrada con éxito</p>
            </div>

        """

        tn.close()

    else:
        msg="""

            <div class="alert alert-warning alert-dismissable">
            <p>El numero de serie no ha sido reconocido por la OLT. Revise los campos y asegurese de que haya comunicacion entre la ONT y la cabecera</p>
            </div>

        """
        tn.close()

try:
    tn = telnetconnect(olt)
    altaservicio(tn)
    success = True
except:
    sqlinsert = "INSERT INTO `ont`(`SN`, `ONT ID`, frame, slot, port, ont_id, `Modelo`,`ID Servicio`, `Estado`) VALUES ('%s','%s', '%s', %s, '%s','%s', '%s', %s, 'Activada')" % (ontsn, idprintont, idframe, idslot, idport, str(idont), modelo, ontservice)
    cursor.execute(sqlinsert)
    con.commit()

    success = False
    msg="""

            <div class="alert alert-danger alert-dismissable">
            <h4>Error!</h4> No se ha podido completar el registro.
            </div>

    """

#tn.write(iface.encode('ascii') + b'\n')
#read = tn.read_until(b'#')
#tn.close();

# Resultado baja del servicio
result = {}

result['success'] = success
#result['keys'] = ",".join(fs.keys())
#result['keys'] = fs.getvalue('idservicioparabaja')
result['message'] = msg


d = {}
for k in form.keys():
    d[k] = form.getvalue(k)

result['data'] = d

sys.stdout.write(json.dumps(result,indent=1))
sys.stdout.write("\n")

sys.stdout.close()
