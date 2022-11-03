#! /usr/bin/python3.5

import cgi
import sys
from config import *
import os
import http.cookies
from pysnmp.entity.rfc3413.oneliner import cmdgen

cmdGen = cmdgen.CommandGenerator()




if 'HTTP_COOKIE' in os.environ:
    cookie_string=os.environ.get('HTTP_COOKIE')
    honeycookie = "honeypon=honeyponlogin"
    #if c['honeypon'].value == 'honeyponlogin':
    if honeycookie in cookie_string:



        print("content-type: text/html\n\n")
        #print(HTMLHEADER)

        print(header_css_scripts) # HP2.0

        print(pestañas_navegacion) # HP2.0

        print("<script>$('#menuont').css('background-color','#01bfb9');</script>")






        #Boton alta de nueva ONT => Modal apunta a nuevo archivo config.py
        print("""<div class='col-md-offset-10' style='margin-top: 60px;'>
                    <a style='cursor:pointer' class='quick-btn alta-btn' data-target='#modal_alta_cliente' data-toggle='modal'>
                         <i class='fa fa-2x fa-user-plus' data-toggle='tooltip' data-placement='bottom' title='Alta de cliente' data-original-title='Alta Cliente'></i>
                    </a>
					<a style='cursor:pointer' class='quick-btn alta-btn' data-target='#modal_alta_ont' data-toggle='modal'>
                         <i class='fa fa-2x fa-upload' data-toggle='tooltip' data-placement='bottom' title='Alta de servicio' data-original-title='Alta ONT'></i>
                    </a>

				</div>""")


        # Fin botón alta y menú de navegación

        print(filtros_ont) # HP2.0
        print(script_list_resources) # HP2.0
        print(script_multiselect) # HP2.0
        print(modal_cliente_asociado) # HP2.0

        print(modal_alta_cliente)  # HP2.0
        print(modal_baja_cliente) # HP2.0
        print(modal_reactivar_cliente) # HP2.0
        print(modal_borrar_cliente) # HP2.0
        print(modal_editar_cliente) # HP2.0
        print(modal_baja_servicio) # HP2.0
        print(modal_resultado) # HP2.0
        print(modalont)




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
