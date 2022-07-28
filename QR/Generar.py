from cgitb import html
from email.mime import image
from turtle import fillcolor
from urllib.error import URLError
import jinja2
import pdfkit
import qrcode
from PIL import Image

def Hacer_QR():
    Logo_link="HTML/COFIDI.jpg"
    logo=Image.open(Logo_link)
    basewidth=100

    wpercent=(basewidth/float(logo.size[0]))
    hsize=int((float(logo.size[1])*float(wpercent)))
    logo= logo.resize((basewidth,hsize),Image.ANTIALIAS)
    QRCODE= qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H
    )
    url="Hola"
    QRCODE.add_data(url)
    QRCODE.make()
    QRCOLOR="Green"
    Qrimg= QRCODE.make_image(
        fillcolor=QRCOLOR,back_color='white'
    ).convert('RGB')
    
    pos=((Qrimg.size[0]-logo.size[0])//2,
        (Qrimg.size[1]-logo.size[1])//2)
    Qrimg.paste(logo,pos)
    Qrimg.save("QR_GUARDADO.png")
    print("Se hizo el QR")

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

Hacer_QR()
if __name__=="__main__":
    ruta_template="HTML/index.html"
    info = {"ID":"1241241","Nombre":"Gabriel Valdez"}
    crear_pdf(ruta_template,info)