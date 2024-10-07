import base64

from fastapi import APIRouter
from fastapi.responses import FileResponse
from starlette.responses import JSONResponse

from routes.utils.remision import crea_pdf, search_news, load_json, salto_linea

router = APIRouter(
    prefix='/remision',
    tags=['remision'],
)

@router.get("/ver/{id}")
def ver_pdf(id: str):
    with open("assets/documentos/LOGO.png", "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

    ruta_template = 'assets/documentos/remision.html'
    ruta_css = 'assets/documentos/remision.css'
    try:
        data = load_json(f'remisiones/' + id + '.json')
        data['hechos'] = salto_linea(data['hechos'])
        data['logo'] = encoded_string
        crea_pdf(ruta_template, data, ruta_css)
        return FileResponse('test.pdf', media_type='application/pdf')
    except:
        try:
            search_news()
            data = load_json(f'remisiones/' + id + '.json')
            data['hechos'] = salto_linea(data['hechos'])
            data['logo'] = encoded_string
            crea_pdf(ruta_template, data, ruta_css)
            return FileResponse('test.pdf', media_type='application/pdf')
        except:
            return JSONResponse({'error': 'Remision no encontrada'}, status_code=500)
