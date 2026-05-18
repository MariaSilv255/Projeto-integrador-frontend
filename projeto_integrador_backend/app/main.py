from fastapi import FastAPI
from app.routers import auth, irrigation

app = FastAPI(title="API do Sistema de Irrigação Inteligente")

app.include_router(auth.router)
app.include_router(irrigation.router)

@app.get("/", tags=["Root"])
async def root():
    return {"mensagem": "API do Sistema de Irrigação Inteligente no ar!"}
