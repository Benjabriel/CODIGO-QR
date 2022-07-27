from cgitb import html
import jinja2
import pdfkit

def crear_pdf(ruta_template,info):
    nombre_template= ruta_template.split('/')[-1]
    ruta_template= ruta_template.replace(nombre_template,"")
    env= jinja2.Environment(loader=jinja2.FileSystemLoader(ruta_template))
    template= env.get_template(nombre_template)
    html= template.render(info)
    
    option={'page-size' :'Letter',
            'margin-top':'0.05in',
            'margin-right':'0.05in',
            'margin-left':'0.05in',
            'margin-bottom':'0.05in',
            'encoding' :'UTF-8',
            'enable-local-file-access': None ,
            'orientation':'landscape'
    }
    config= pdfkit.configuration(wkhtmltopdf='wkhtmltopdf/bin/wkhtmltopdf.exe')
    ruta_salida="r.pdf"
    pdfkit.from_string(html,ruta_salida,css="",options=option,configuration=config)


if __name__=="__main__":
    ruta_template="HTML/index.html"
    info = {"ID":"1241241","Nombre":"Gabriel Valdez"}
    crear_pdf(ruta_template,info)