from fastapi import FastAPI
from app.routes import router


app = FastAPI(title="Test Shop API")
app.include_router(router, prefix="/api")


@app.get("/health")
async def health():
    return {"status": "ok"}
