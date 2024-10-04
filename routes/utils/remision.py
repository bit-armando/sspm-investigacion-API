import json
from datetime import datetime

from sqlalchemy import text

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, TableStyle, Table

from sql.databases.detenidos import engine


def salto_linea(text:str):
    return text.replace('\n', '<br/><br/>')


def load_json(path:str) -> dict:
    with open(f'remisiones/{path}.json', 'r') as f:
        data = json.load(f)
    return data


def convert_json(data):
    for registro in data:
        print(data[registro])
        try:
            with open(f'/remisiones/{registro}.json', 'w') as f:
                json.dump(data[registro], f, indent=4)
        except:
            pass


def to_day() -> str:
    date = datetime.today()
    date = f'{date.year}/{date.month}/{date.day}'
    return date


def search_news(date: str):
    datos = {}

    with engine.connect() as conn:
        result = conn.execute(text(
            f"""
                select json from actuaciones_det
                where id_actuacion_cat = 12
                and fecha >= to_date('{to_day()}', 'YYYY/MM/DD')
            """
        ))

        for i in result:
            datos_str = i.json.decode('utf-8')
            aux = json.loads(datos_str)

            try:
                id = aux['detenidos'][0]['numRemision']
                datos[id] = aux
            except:
                pass

    convert_json(datos)



def myFirstPage(canvas, doc):

    page_width, page_height = letter

    canvas.saveState()
    canvas.drawImage('assets/LOGO.png', 60, 650, width=200, height=100)
    canvas.setFont('Helvetica-Bold', 8)
    departamentos = [
        'SECRETARÍA DE SEGURIDAD PÚBLICA MUNICIPAL',
        'DIRECCIÓN DE ASUNTOS JURÍDICOS',
        'COORDINACIÓN DE PUESTAS A DISPOSICIÓN',
    ]
    y_position = 730
    for line in departamentos:
        text_width = canvas.stringWidth(line, 'Helvetica-Bold', 8)
        x_position = page_width - 50 - text_width
        canvas.drawString(x_position, y_position, line)
        y_position -= 10


    canvas.drawString(60, 620, 'ELABORÓ:')  # -- FECHA ALINEADA
    canvas.drawString(60, 600, 'UNIDAD:')
    canvas.drawString(180, 600, 'SECTOR:')
    canvas.drawString(300, 600, 'DEPARTAMENTO:')

    canvas.drawString(60, 580, 'REMISIÓN:')
    canvas.drawString(60, 570, 'CLASIFICACIÓN:')

    canvas.drawString(60, 550, 'I. LUGAR DE LOS HECHOS:')
    canvas.drawString(60, 500, 'II. INFRACTOR (ES):')

    canvas.restoreState()


def generar_pdf(ruta, remision):
    contenido = load_json(remision)
    doc = SimpleDocTemplate(ruta, pagesize=letter)

    styles = getSampleStyleSheet()
    normal = ParagraphStyle(name='normal', parent=styles['Normal'],
                            fontName='Helvetica', fontSize=8,
                            leftIndent=-18, rightIndent=-18, spaceBefore=-10)

    resaltado = ParagraphStyle(name='resaltado', parent=styles['Normal'],
                               fontName='Helvetica-Bold', fontSize=8,
                               leftIndent=-18)
    styles.alignment = 'justify'
    styles.add(normal)
    styles.add(resaltado)

    detenidos = [["NOMBRE", "SEXO", "EDAD", "DOMICILIO"]]

    for detenido in contenido['detenidos']:
        aux = [
            detenido['nombre'],
            detenido['sexo'],
            detenido['edad'],
            detenido['domicilio']
        ]
        detenidos.append(aux)

    table = Table(detenidos)
    table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),  # Fuente
        ('FONTSIZE', (0, 0), (-1, -1), 8),  # Tamaño de fuente
    ]))

    story = [Spacer(1, 220)]
    story.append(table)
    story.append(Paragraph("III. HECHOS:", resaltado))
    story.append(Paragraph(salto_linea(contenido['hechos'])))

    doc.build(story, onFirstPage=myFirstPage)