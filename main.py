from fastapi import FastAPI
from fastapi.responses import FileResponse

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

from sql.databases.detenidos import engine
from sql.models import detenidos
from routes.detenido import router as detenido_router


detenidos.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_route(detenido_router)


def myFirstPage(canvas, doc):
    page_width, page_height = letter
    
    canvas.saveState()
    canvas.drawImage("LOGO.png", 60, 650, width=200, height=100)
    canvas.setFont('Helvetica-Bold', 8)
    departamentos = [
        'SECRETARÍA DE SEGURIDAD PÚBLICA MUNICIPAL',
        'DIRECCIÓN DE ASUNTOS JURÍDICOS',
        'COORDINACIÓN DE PUESTAS A DISPOSICIÓN'
    ]
    y_position = 730
    for line in departamentos:
        text_width = canvas.stringWidth(line, 'Helvetica-Bold', 8)
        x_position = page_width - 50 - text_width
        canvas.drawString(x_position, y_position, line) 
        y_position -= 10
    canvas.restoreState()


def generar_pdf(ruta):
    doc = SimpleDocTemplate(ruta, pagesize=letter)

    # Estilos predefinidos
    estilos = getSampleStyleSheet()
    story = [Spacer(1,70)]

    # story.append(Paragraph(f"FOLIO: {'EDITAR'}" , estilos['Heading5']))
    texto = 'EDITAR'
    html_text = f"""
        <b>FOLIO: </b><span> {texto} </span>
        <br/><br/>
        <b>ELABORÓ: </b><span> {texto} </span>
        <br/><br/>
        <b>UNIDAD: </b><span> {texto} </span>
        <b>SECTOR: </b><span> {texto} </span>
        <b>DEPARTAMENTO: </b><span> {texto} </span>
        <b>NUM. REMISION</b>
        <br>
        
    """
    story.append(Paragraph(html_text, estilos['Normal']))
    
    

    # Generar el PDF con los story añadidos
    doc.build(story, onFirstPage=myFirstPage)


@app.get("/ver")
def ver_pdf():
    ruta_pdf = 'reporte.pdf'
    generar_pdf(ruta_pdf)
    
    return FileResponse(ruta_pdf, media_type='application/pdf')