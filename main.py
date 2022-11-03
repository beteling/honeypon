#! /usr/bin/python3.5

import cgi
import sys
import MySQLdb
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



        print("content-type: text/html\n\n")
        print(header_css_scripts) # HP2.0

        print(pestañas_navegacion) # HP2.0
        print("<script>$('#main').css('background-color','#01bfb9');</script>")

        sqlontlist = "SELECT t1.SN, t1.`ONT ID`, t1.`ID Servicio`, t1.Estado, t2.Nombre, t2.Direccion, t2.olt, t3.Nombre, t2.DNI, t2.Telefono, t1.Modelo FROM ont AS t1, clientes AS t2, planes AS t3 WHERE t1.`ID Servicio` = t2.ID AND t2.Plan = t3.ID ORDER BY t1.`ONT ID`"
        cursor.execute(sqlontlist)
        resultont = cursor.fetchall()

        print(modal_cliente_asociado) # HP2.0

        print(modal_alta_cliente)  # HP2.0
        print(modal_baja_cliente) # HP2.0
        print(modal_reactivar_cliente) # HP2.0
        print(modal_borrar_cliente) # HP2.0
        print(modal_editar_cliente) # HP2.0
        print(modal_baja_servicio) # HP2.0
        print(modal_resultado) # HP2.0
        print(modalont)



        print("""<div class='col-md-6'>
                        <h2 style="color:#1A5F82;margin-top:40px;margin-bottom:40px">Pendientes de aprovisionamiento</h2>
                        </div>""");


        print("<span id='spantablaont'></span>")

        print("""<script language="javascript">
        consultar_registros("consulta_pendientes");
        </script>""");
    else:
        print("content-type: text/html\n\n")
        print(header_css_scripts)
        print("""<script language="javascript">
        window.location.href = "/honeypon/index.py"
        </script>""")

else:
    print("content-type: text/html\n\n")
    print(header_css_scripts)
    print("""<script language="javascript">
    window.location.href = "/honeypon/index.py"
    </script>""")

print(javacode)


print(HTMLFIN)
