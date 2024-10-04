from fastapi import FastAPI

from routes.detenido import router as detenido_router
from routes.remision import router as remision_router

app = FastAPI()
app.include_router(detenido_router)
app.include_router(remision_router)



