from fastapi import APIRouter
from fastapi.responses import FileResponse
from starlette.responses import JSONResponse

from routes.utils.remision import generar_pdf

router = APIRouter(
    prefix='/remision',
    tags=['remision'],
)

@router.get("/ver/{id}")
def ver_pdf(id: str):
    ruta_pdf = 'reporte.pdf'

    try:
        generar_pdf(ruta_pdf, id)
        return FileResponse(ruta_pdf, media_type='application/pdf')
    except:

        return JSONResponse({'error': 'Remision no encontrada'}, status_code=500)