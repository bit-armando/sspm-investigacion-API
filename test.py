import jinja2
import pdfkit
import base64

from routes.utils.remision import load_json, salto_linea

def crea_pdf(ruta_template, info, rutacss=''):
    nombre_template = ruta_template.split('/')[-1]
    ruta_template = ruta_template.replace(nombre_template, '')

    env = jinja2.Environment(loader=jinja2.FileSystemLoader(ruta_template))
    template = env.get_template(nombre_template)
    html = template.render(info)

    options = {
        'page-size': 'Letter',
        'margin-top': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'margin-right': '0.75in',
        'encoding': 'utf-8',
    }


    # config = pdfkit.configuration(wkhtmltopdf='/usr/bin/wkhtmltopdf')
    ruta_salida ='test.pdf'
    pdfkit.from_string(html, ruta_salida, css=rutacss, options=options)




with open("assets/documentos/LOGO.png", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

data = load_json('remisiones/1D-007096-24.json')
data['hechos'] = salto_linea(data['hechos'])
data['logo'] = encoded_string

crea_pdf('assets/documentos/remision.html',data, 'assets/documentos/remision.css')