import json
import jinja2
import pdfkit
from datetime import datetime
from sqlalchemy import text

from sql.databases.detenidos import engine


def salto_linea(texto:str):
    """
    Remplaza todos los saltos de carro \n de un texto por dos etiquetas html <br/> para que pueda hacer los saltos de linea en un documento pdf
    :param texto: Texto original
    :return: Texto modificado con los <br/>
    """
    return texto.replace('\n', '<br/><br/>')


def load_json(path:str) -> dict:
    """
    Lee un documento Json
    :param path: Nombre del archivo sin la extencion
    :return: dict con la informacion del fichero json
    """
    with open(path, 'r') as f:
        data = json.load(f)
    return data


def convert_json(data):
    for registro in data:
        try:
            with open(f'remisiones/{registro}.json', 'w') as f:
                json.dump(data[registro], f, indent=4)
        except:
            pass


def to_day() -> str:
    """
    Toma la fecha del dia actual
    :return: str en el formato YYYY/MM/DD
    """
    date = datetime.today()
    date = f'{date.year}/{date.month}/{date.day}'
    return date


def search_news():
    with open('remisiones/__date__.txt', 'r') as f:
        query_date = f.read()

    with open('remisiones/__date__.txt', 'w') as f:
        f.write(to_day())

    with engine.connect() as conn:
        result = conn.execute(text(
                f"""
                select json from actuaciones_det
                where id_actuacion_cat = 12
                and fecha >= to_date('{query_date}', 'YYYY/MM/DD')
            """
        ))

    datos = {}
    for registro in result:
        datos_str = registro.json.decode('utf-8')
        aux = json.loads(datos_str)

        try:
            id = aux['detenidos'][0]['numRemision']
            datos[id] = aux
        except:
            pass

    convert_json(datos)


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