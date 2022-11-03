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
            print("<script>$('#menuolt').css('background-color','#FEA126');</script>")

            sqloltlist = "SELECT Nombre, IP, `ID Cacti` FROM olt"
            cursor.execute(sqloltlist)
            resultolt = cursor.fetchall()

            # Comienzo botón alta y menú de navegación
            #print('<div class="col-md-12">')
            #print('<h2 style="color:#1A5F82;margin-top:40px">Lista de OLT</h2>')
            #print('<button type="button" class="btn btn-primary" data-target="#myModalolt" data-toggle="modal" style="width:200px; margin-top:30px"><span>Nueva OLT</span></button>')
            #print('</div>')
            print(modalolt)
            idm = 1
            #print('<div class="col-md-12" style="margin-top:50px">')
            #print('<div id="pageNavPosition"></div>')
            #print('</div>')
            print('<div class="col-md-4">')
            print('<h2 style="color:#1A5F82;margin-top:40px">Lista de OLT</h2>')
            print('</div>')
            #Boton alta de nueva ONT
            print("""<div class='col-md-1' style='float:right;margin-top:40px'>
                        <div class= 'row tooltip-demo'>
						<a style='cursor:pointer' class='quick-btn alta-btn' data-target='#myModalolt' data-toggle='modal'>
                             <i class='fa fa-2x fa-server' data-toggle='tooltip' data-placement='bottom' title='' data-original-title='Alta OLT'></i>
                        </a>
                        </div>
					</div>""")
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

                print('<td align="center"><form action="/cgi-bin/olt.py" method="post"><input type="hidden" name="altaoltname" value=',row[0],'/><input type="hidden" name="inputip" value=',row[1],'/><input type="hidden" name="oltidcacti" value=',row[2],'/>')
                #print('<div class="btn-group">')
                print('<button title="Modificar" id="oltedit" type="submit" class="btn btn-primary" name="modificarolt" value="botoneditolt"><span id="olticonedit" class="glyphicon glyphicon-wrench"></span></button>')
                print('<button title="Baja OLT" href="#modal-borrarolt%s" data-toggle="modal" id="oltbaja" type="button" class="btn btn-danger" name="bajaolt"><span class="glyphicon glyphicon-trash" id="olticonbaja"></span></button>' %idm)
                print(modaloltborrado %idm)
                print('<button title="Registrar en servidor Cacti" type="submit" id="oltcacti" value="Alta Cacti" class="btn btn-success" name="altacacti"><span class="glyphicon glyphicon-import" id="olticoncacti"></span></button></form></td>')

                #print('</div>')
                print('</tr>')
                idm += 1
            print(tablaoltfin)


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


print(HTMLFIN)
